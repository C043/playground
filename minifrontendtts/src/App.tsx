import React, { useEffect, useRef, useState } from "react";
import "./App.css";

function App() {
  const connection = useRef<WebSocket | null>(null);
  const mediaSource = useRef<MediaSource | null>(null);
  const sourceBuffer = useRef<SourceBuffer | null>(null);
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const [text, setText] = useState("");

  const sendText = (e: React.FormEvent) => {
    e.preventDefault();

    if (connection.current?.readyState === WebSocket.OPEN) {
      connection.current.send(JSON.stringify({ text }));
      setText("");

      if (mediaSource.current?.readyState === "open" && sourceBuffer.current) {
        try {
          sourceBuffer.current?.abort();
          sourceBuffer.current?.remove(0, sourceBuffer.current.buffered.end(0));
        } catch (err) {
          console.error(`There was an error playing the audio: ${err}`);
        }
      }
    } else {
      window.alert("WebSocket is not open.");
    }
  };

  useEffect(() => {
    const socket = new WebSocket("ws://localhost:8000/ws");
    socket.binaryType = "arraybuffer";

    socket.addEventListener("message", (ev) => {
      if (ev.data instanceof ArrayBuffer && sourceBuffer.current) {
        const buffer = new Uint8Array(ev.data);
        sourceBuffer.current.appendBuffer(buffer);

        audioRef.current?.play().catch((err) => {
          console.warn(`Autoplay failed: ${err}`);
        });
      }
    });

    connection.current = socket;

    mediaSource.current = new MediaSource();
    if (audioRef.current && mediaSource.current) {
      audioRef.current.src = URL.createObjectURL(mediaSource.current);

      mediaSource.current.addEventListener("sourceopen", () => {
        if (mediaSource.current && !sourceBuffer.current) {
          sourceBuffer.current =
            mediaSource.current.addSourceBuffer("audio/mpeg");
        }
      });
    }

    return () => {
      socket.close();
    };
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
