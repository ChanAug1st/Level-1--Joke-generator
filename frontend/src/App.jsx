import { useState } from "react";
import axios from "axios";

function App() {
  const [theme, setTheme] = useState("programming");
  const [type, setType] = useState("joke");
  const [result, setResult] = useState("");

  const generate = async () => {
    try {
      console.log("clicked");
  
      const res = await axios.post("http://127.0.0.1:8000/generate", {
        theme,
        type
      });
  
      console.log(res.data);
      setResult(res.data.result);
    } catch (err) {
      console.error("ERROR:", err);
      setResult("Error calling backend");
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>😂 Joke Generator</h1>

      <select onChange={(e) => setTheme(e.target.value)}>
        <option value="dad jokes">dad jokes</option>
        <option value="programming">programming</option>
        <option value="dark humor">dark humor</option>
      </select>

      <select onChange={(e) => setType(e.target.value)}>
        <option value="joke">joke</option>
        <option value="story">story</option>
      </select>

      <button onClick={generate}>Generate</button>

      <p style={{ marginTop: 20 }}>{result}</p>
    </div>
  );
}

export default App;