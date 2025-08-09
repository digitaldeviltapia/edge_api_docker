
# CV API (FastAPI + Docker)

A tiny, production-minded demo: a FastAPI service exposes a Canny edge detector. 
Use it locally or in Docker. Great as a first MLOps step (service + container).

## 1) Local (no Docker)
```bash
python -m venv .venv
# On Windows: .venv\Scripts\activate
# On macOS/Linux: source .venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
# open http://127.0.0.1:8000/docs
```

## 2) Docker
```bash
docker build -t cv-api .
docker run -p 8000:8000 cv-api
# open http://127.0.0.1:8000/docs
```

## 3) Use the API
```bash
curl -X POST -F "file=@your_image.jpg" http://127.0.0.1:8000/infer --output edges.png
```

## 4) Dev tools
```bash
pip install -r requirements-dev.txt
pytest -q
flake8 app
```

## Endpoints
- `GET /health` -> {"status":"ok"}
- `POST /infer` -> send a PNG/JPEG, returns edge map as PNG

## Notes
- `opencv-python-headless` avoids GUI deps; the Dockerfile adds minimal libs just in case.

