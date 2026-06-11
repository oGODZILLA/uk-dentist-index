"use client";
import { useState } from "react";

export default function Home() {
  const [q, setQ] = useState("");
  const [results, setResults] = useState([]);

  async function search(value) {
    setQ(value);
    const r = await fetch(`/api/search?q=${value}`);
    const data = await r.json();
    setResults(data);
  }

  return (
    <div style={{ padding: 40 }}>
      <h1>UK Dentist Intelligence</h1>

      <input 
        value={q}
        onChange={(e) => search(e.target.value)}
        placeholder="Search dentists..." 
        style={{ padding: 10, width: 300 }}
      />

      <div style={{ marginTop: 20 }}>
        {results.map((d, i) => (
          <div key={i} style={{ marginBottom: 10 }}>
            <strong>{d.name}</strong><br />
            {d.address}<br />
            {d.website}
          </div>
        ))}
      </div>
    </div>
  );
}
