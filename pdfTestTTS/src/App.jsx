import { useEffect, useRef, useState } from "react";
import { getDocument } from "pdfjs-dist";
import { split } from "sentence-splitter";
import "./App.css";
import workerSrc from "pdfjs-dist/build/pdf.worker?url";
import { GlobalWorkerOptions } from "pdfjs-dist/build/pdf";

// Set the worker path
GlobalWorkerOptions.workerSrc = workerSrc;
GlobalWorkerOptions.standardFontDataUrl = "/pdfjs/standard_fonts/";

function App() {
  const [count, setCount] = useState(0);
  const [pdfText, setPdfText] = useState("");
  const [showViewer, setShowViewer] = useState(false);
  const [viewerUrl, setViewerUrl] = useState("");
  const [pdfFile, setPdfFile] = useState(null);
  const [sentences, setSentences] = useState([]);
  const fileInputRef = useRef(null);

  const handleButtonClick = () => fileInputRef.current?.click();

  const handleFileChange = async (ev) => {
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
    setSentences(
      document
        .filter((node) => node.type === "Sentence")
        .map((node) => node.raw.trim()),
    );

    setPdfText(fullText);
    setPdfFile(uint8ArrayForViewer);
    setShowViewer(true);
  };

  useEffect(() => {
    if (!pdfFile) return;

    const blob = new Blob([pdfFile], { type: "application/pdf" });
    const url = URL.createObjectURL(blob);
    setViewerUrl(url);

    return () => URL.revokeObjectURL(url);
  }, [pdfFile]);

  return (
    <>
      <h1>PDF TEST</h1>
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
