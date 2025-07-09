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
  const [sentenceRects, setSentenceRects] = useState([]);

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
    const positionMap = [];

    for (let pageNum = 1; pageNum <= pdf.numPages; pageNum++) {
      const page = await pdf.getPage(pageNum);
      const content = await page.getTextContent();

      let pageText = "";

      for (const item of content.items) {
        if (!item.str.trim()) continue;

        const startIndex = fullText.length + pageText.length;
        const itemText = item.str;

        pageText += itemText + " ";

        positionMap.push({
          index: startIndex,
          length: itemText.length,
          item: {
            str: itemText,
            transform: item.transform,
            width: item.width,
            height: item.height,
            page: pageNum,
          },
        });
      }
      fullText += pageText + "\n";
    }

    const sentencesSplitted = split(fullText).filter(
      (node) => node.type === "Sentence",
    );

    const sentencesWithPositions = sentencesSplitted.map((sentence) => {
      const sentenceStart = sentence.range[0];
      const sentenceEnd = sentence.range[1];

      const items = positionMap.filter(
        ({ index, length }) =>
          index + length > sentenceStart && index < sentenceEnd,
      );
      return {
        text: sentence.raw.trim(),
        items,
      };
    });

    const scale = 2;
    const canvasContainer = document.getElementById("canvas-container");
    canvasContainer.innerHTML = "";
    const sentencesRects = [];
    for (let pageNum = 1; pageNum <= pdf.numPages; pageNum++) {
      const page = await pdf.getPage(pageNum);
      const viewport = page.getViewport({ scale });
      const outputScale = window.devicePixelRatio || 1;

      const canvas = document.createElement("canvas");
      canvasContainer.appendChild(canvas);
      const context = canvas.getContext("2d");
      canvas.width = Math.floor(viewport.width * outputScale);
      canvas.height = Math.floor(viewport.height * outputScale);
      canvas.style.width = Math.floor(viewport.width) + "px";
      canvas.style.height = Math.floor(viewport.height) + "px";
      const transform =
        outputScale !== 1 ? [outputScale, 0, 0, outputScale, 0, 0] : null;

      const renderContext = {
        canvasContext: context,
        transform: transform,
        viewport: viewport,
      };

      await page.render(renderContext).promise;

      // draw sentence highlights
      context.save();
      context.globalAlpha = 0.3;
      context.fillStyle = "yellow";

      // find all sentences that belong to this page
      for (const sentence of sentencesWithPositions) {
        const itemsOnPage = sentence.items.filter(
          (item) => item.item.page === pageNum,
        );

        if (!itemsOnPage.length) continue;

        for (const entry of itemsOnPage) {
          const padding = 2;
          const textItem = entry.item;

          const [x, y] = viewport.convertToViewportPoint(
            textItem.transform[4],
            textItem.transform[5],
          );

          const h = textItem.height * outputScale * scale;
          const w = textItem.width * outputScale * scale;

          sentenceRects.push({
            x: x + 25,
            y: y - textItem.height / scale,
            w: textItem.width * scale,
            h: textItem.height,
            text: sentence.text,
            page: pageNum,
          });
        }
      }
      setSentences(sentenceRects);
      context.restore();
    }

    setPdfFile(uint8ArrayForViewer);
  };

  useEffect(() => {
    if (!pdfFile) return;

    const scale = 1;
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
      <div id="canvas-container">
        {sentenceRects.map((rect, i) => (
          <div
            key={i}
            className="highlight-box"
            style={{
              position: "absolute",
              top: `${rect.y}px`,
              left: `${rect.x}px`,
              width: `${rect.w}px`,
              height: `${rect.h}px`,
            }}
            title={rect.text}
          />
        ))}
      </div>
    </>
  );
}

export default App;
