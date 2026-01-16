import { useState } from "react";
import api from "../api/api";

export default function ChatInput({ onResult }) {
  const [text, setText] = useState("");
  const [loading, setLoading] = useState(false);

  const submitInteraction = async () => {
    if (!text.trim()) return;

    setLoading(true);
    try {
      const response = await api.post("/chat", { text });
      onResult(response.data);
      setText("");
    } catch (error) {
      alert("Error submitting interaction");
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <textarea
        className="textarea"
        rows={4}
        placeholder="Describe interaction with HCP..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />

      <button
        className="button"
        onClick={submitInteraction}
        disabled={loading}
      >
        {loading ? "Processing..." : "Log Interaction"}
      </button>
    </>
  );
}
