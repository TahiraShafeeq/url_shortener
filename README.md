# FastAPI URL Shortener 🐳

A high-performance RESTful URL shortener API built with **Python** and **FastAPI**, containerized using **Docker**, and published to **Docker Hub**.

---

## 🛠️ Tech Stack

* **Language & Framework:** Python 3.11, FastAPI
* **ASGI Server:** Uvicorn
* **Data Validation:** Pydantic
* **Containerization:** Docker Engine, Docker Hub
* **API Documentation:** Interactive Swagger UI & ReDoc

---

## 📦 Docker Hub Repository

The pre-built public container image is hosted on Docker Hub:

👉 **Image Tag:** `tahirashafeeq/url_shortener:latest`

---

## 🚀 How to Run the Project

Choose one of the three options below to run the application on your system:

### Option 1: Run via Public Docker Image (Recommended)
Run the application directly using the public Docker Hub image without needing Python installed locally:

```bash
# 1. Pull the image from Docker Hub
docker pull tahirashafeeq/url_shortener:latest

# 2. Start the container on port 8000
docker run -d -p 8000:8000 --name url-shortener-app tahirashafeeq/url_shortener:latest

# 3. Verify container status
docker ps
```


### Option 2: Build & Run Docker Image Locally
Build the Docker image directly from your local clone of the repository:

```bash
# 1. Clone the repository
git clone [https://github.com/TahiraShafeeq/url_shortener.git](https://github.com/TahiraShafeeq/url_shortener.git)
cd url_shortener

# 2. Build the Docker image
docker build -t fastapi-url-shortener .

# 3. Run the container on port 8000
docker run -d -p 8000:8000 --name url-shortener-app fastapi-url-shortener
```

### Option 3: Local Python Development (Without Docker)
Run the application using Python and a virtual environment:
# 1. Clone the repository
git clone [https://github.com/TahiraShafeeq/url_shortener.git](https://github.com/TahiraShafeeq/url_shortener.git)
cd url_shortener

# 2. Create and activate a virtual environment
python -m venv venv

# Windows PowerShell:
.\venv\Scripts\Activate.ps1

# Linux / macOS / WSL:
source venv/bin/activate

# 3. Install required dependencies
pip install -r requirements.txt

# 4. Start the Uvicorn development server
uvicorn main:app --reload




