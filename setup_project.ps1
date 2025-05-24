# PowerShell script to automate the setup of the Make Sense Bot project

# Function to set up the frontend
function Setup-Frontend {
    Write-Host "Setting up the frontend..."
    cd frontend
    npm install
    npm run dev
    cd ..
}

# Function to set up the backend
function Setup-Backend {
    Write-Host "Setting up the backend..."
    if (Test-Path rebuild_venv.bat) {
        Write-Host "Running rebuild_venv.bat to set up the backend..."
        ./rebuild_venv.bat
    } else {
        Write-Host "Manual setup required. Please follow the instructions in the README.md."
    }
}

# Main script execution
Write-Host "Starting project setup..."

# Check for Node.js
if (-not (Get-Command node -ErrorAction SilentlyContinue)) {
    Write-Host "Node.js is not installed. Please install Node.js and try again."
    exit 1
}

# Check for Python
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python is not installed. Please install Python 3.8+ and try again."
    exit 1
}

# Run setup functions
Setup-Frontend
Setup-Backend

Write-Host "Project setup complete!"
