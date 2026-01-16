import { useState } from "react";
import Header from "../components/Header";
import ChatInput from "../components/ChatInput";
import InteractionResult from "../components/InteractionResult";

export default function LogInteractionPage() {
  const [result, setResult] = useState(null);

  return (
    <>
      <Header />
      <div className="container">
        <ChatInput onResult={setResult} />
        <InteractionResult data={result} />
      </div>
    </>
  );
}
