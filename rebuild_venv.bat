@echo off
REM Script to rebuild the backend .venv environment
cd backend
if exist .venv rmdir /s /q .venv
python -m venv .venv
call .venv\Scripts\activate && pip install -r requirements.txt
cd ..
echo Backend virtual environment rebuilt and dependencies installed.
