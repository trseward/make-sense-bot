// src/services/api.js
// Handles API requests to the FastAPI backend

const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:8000';

export async function submitPrompt(ageGroup, prompt) {
  const response = await fetch(`${API_BASE}/summarize`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ context: ageGroup, explain: prompt })
  });
  if (!response.ok) {
    throw new Error('Failed to fetch summary');
  }
  return response.json();
}
