import React, { useEffect, useRef, useState } from "react";
import "./App.css";

function App() {
  const connection = useRef<WebSocket | null>(null);
  const mediaSource = useRef<MediaSource | null>(null);
  const sourceBuffer = useRef<SourceBuffer | null>(null);
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const [text, setText] = useState("");
  const [isReconnecting, setReconnecting] = useState(false);

  const audioQueue: Uint8Array[] = [];

  const reconnectToWs = () => {};

  const sendText = (e: React.FormEvent) => {
    e.preventDefault();

    if (connection.current?.readyState === WebSocket.OPEN) {
      connection.current.send(JSON.stringify({ text }));
      setText("");
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

          sourceBuffer.current.addEventListener("updateend", processQueue);
        }
      });
    }
  }, []);

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
    </>
  );
}

export default App;
