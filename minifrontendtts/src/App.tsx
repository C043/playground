import "./App.css";
import React, { useEffect, useRef, useState } from "react";
import { split } from "sentence-splitter";
import { getDocument } from "pdfjs-dist";
import workerSrc from "pdfjs-dist/build/pdf.worker?url";
import { GlobalWorkerOptions } from "pdfjs-dist/build/pdf";

// Set the worker path
GlobalWorkerOptions.workerSrc = workerSrc;
GlobalWorkerOptions.standardFontDataUrl = "/pdfjs/standard_fonts/";

function App() {
  const connection = useRef<WebSocket | null>(null);
  const mediaSource = useRef<MediaSource | null>(null);
  const sourceBuffer = useRef<SourceBuffer | null>(null);
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const [text, setText] = useState("");
  let sentencesToSend: string[] = [];
  const [pdfText, setPdfText] = useState("");
  const [viewerUrl, setViewerUrl] = useState("");
  const [pdfFile, setPdfFile] = useState<Uint8Array | null>(null);
  const [showViewer, setShowViewer] = useState(false);
  const fileInputRef = useRef<HTMLInputElement | null>(null);

  const audioQueue: Uint8Array[] = [];

  const handleButtonClick = () => fileInputRef.current?.click();

  const handleFileChange = async (ev: React.ChangeEvent<HTMLInputElement>) => {
    const file = ev.target.files?.[0];
    if (!file || file.type !== "application/pdf") return;

    const arrayBuffer = await file.arrayBuffer();

    const uint8ArrayForViewer = new Uint8Array(arrayBuffer); // used for blob + Viewer
    const uint8ArrayForPdfJS = new Uint8Array(arrayBuffer); // used for text extraction

    const uint8Array = new Uint8Array(uint8ArrayForPdfJS);

    const pdf = await getDocument(uint8Array).promise;

    let fullText = "";
    for (let i = 1; i <= pdf.numPages; i++) {
      const page = await pdf.getPage(i);
      const content = await page.getTextContent();
      const pageText = content.items
        .map((item) => ("str" in item ? item.str : ""))
        .join(" ");
      fullText += pageText + "\n";
    }

    const document = split(fullText);
    const sentences = document
      .filter((node) => node.type === "Sentence")
      .map((node) => node.raw.trim());

    sentencesToSend = sentences;
    sendTextFromPdf();
    setPdfText(fullText);
    setPdfFile(uint8ArrayForViewer);
    setShowViewer(true);
  };

  const sendText = (ev: React.FormEvent) => {
    ev.preventDefault();

    if (connection.current?.readyState === WebSocket.OPEN) {
      connection.current.send(JSON.stringify({ text }));
      setText("");
    } else {
      window.alert("WebSocket is not open.");
    }
  };

  const sendTextFromPdf = () => {
    if (connection.current?.readyState === WebSocket.OPEN) {
      const sentence = sentencesToSend.shift();
      connection.current.send(JSON.stringify({ text: sentence }));
    } else {
      window.alert("WebSocket is not open.");
    }
  };

  const processQueue = () => {
    if (!sourceBuffer.current || sourceBuffer.current.updating) return;
    const chunk = audioQueue.shift();
    if (chunk) {
      sourceBuffer.current.appendBuffer(chunk);

      const isPlaying =
        audioRef.current &&
        !audioRef.current.paused &&
        !audioRef.current.ended &&
        audioRef.current.readyState > 2;

      if (!isPlaying) {
        audioRef.current?.play().catch((err) => {
          console.warn(`Autoplay failed: ${err}`);
        });
      }
    }
  };

  const connectToWs = () => {
    const socket = new WebSocket("ws://localhost:8000/ws");
    socket.binaryType = "arraybuffer";

    socket.addEventListener("message", (ev) => {
      if (ev.data instanceof ArrayBuffer && sourceBuffer.current) {
        const buffer = new Uint8Array(ev.data);
        audioQueue.push(buffer);

        processQueue();
      }
    });

    socket.addEventListener("close", () => {
      console.log("Disconnected, reconnecting...");
      setTimeout(connectToWs, 1000);
    });

    socket.addEventListener("error", () => {
      socket.close();
    });

    connection.current = socket;
  };

  useEffect(() => {
    connectToWs();

    mediaSource.current = new MediaSource();
    if (audioRef.current && mediaSource.current) {
      audioRef.current.src = URL.createObjectURL(mediaSource.current);

      mediaSource.current.addEventListener("sourceopen", () => {
        if (mediaSource.current && !sourceBuffer.current) {
          sourceBuffer.current =
            mediaSource.current.addSourceBuffer("audio/mpeg");

          sourceBuffer.current.addEventListener("updateend", () => {
            processQueue();
            sendTextFromPdf();
          });
        }
      });
    }
  }, []);

  useEffect(() => {
    if (!pdfFile) return;

    const blob = new Blob([pdfFile], { type: "application/pdf" });
    const url = URL.createObjectURL(blob);
    setViewerUrl(url);

    return () => URL.revokeObjectURL(url);
  }, [pdfFile]);

  useEffect(() => {}, [pdfText]);

  return (
    <>
      <h1>WebSocket with Python Test</h1>
      <form onSubmit={sendText}>
        <input
          value={text}
          onChange={(ev) => setText(ev.target.value)}
          type="text"
        />
        <button type="submit">Send</button>
      </form>
      <audio ref={audioRef} muted={false} autoPlay hidden />
      <input
        onChange={handleFileChange}
        type="file"
        accept="application/pdf"
        hidden
        ref={fileInputRef}
      />
      <button onClick={handleButtonClick}>Upload pdf</button>
      {showViewer && viewerUrl && (
        <iframe
          src={viewerUrl}
          style={{
            position: "fixed",
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            width: "100%",
            height: "100%",
            border: "none",
            zIndex: 9999,
          }}
        />
      )}
    </>
  );
}

export default App;
