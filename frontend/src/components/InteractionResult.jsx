export default function InteractionResult({ data }) {
  if (!data) return null;

  const result = data.result;

  return (
    <div className="result-card">
      <h3>AI Processed Interaction</h3>

      <div className="result-row"><b>HCP Name:</b> {result.interaction.hcp_name}</div>
      <div className="result-row"><b>Summary:</b> {result.interaction.summary}</div>
      <div className="result-row"><b>Sentiment:</b> {result.interaction.sentiment}</div>
      <div className="result-row"><b>Follow-up:</b> {result.follow_up}</div>
      <div className="result-row"><b>Material:</b> {result.material}</div>
    </div>
  );
}
