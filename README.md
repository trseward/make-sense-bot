# Make Sense Bot

A fullstack application that summarizes subject prompts for different school-age groups using a Vue.js frontend and a Python FastAPI backend with LangChain, OpenAI, and a vector database for RAG.

## Project Structure

- `frontend/` — Vue.js app (Vite)
- `backend/` — FastAPI app (Python)

## Setup Instructions

### Prerequisites
- Node.js (for frontend)
- Python 3.8+ (for backend)

### Frontend Setup
```powershell
cd frontend
npm install
npm run dev
```

### Backend Setup
You can use the provided script to rebuild the backend virtual environment and install dependencies automatically:

```powershell
./rebuild_venv.bat
```

#### To update dependencies:
1. Edit `backend/requirements.txt` as needed.
2. Re-run the script above to install the updated dependencies.

#### Manual steps (if needed):
```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Environment Variables
- Store API keys and secrets in a `.env` file in the backend directory (not committed to git).

## Usage
- Open the frontend in your browser (default: http://localhost:5173)
- The backend runs on http://localhost:8000

## Features
- Select age group and enter a subject prompt
- Summarizes and explains the prompt for the selected age group
- Uses RAG with reputable sources for up-to-date information

## Contributing
- See `copilot-instructions.md` for project guidelines

## License
MIT
