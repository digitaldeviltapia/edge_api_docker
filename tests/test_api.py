
from fastapi.testclient import TestClient
from app.main import app
import numpy as np
import cv2

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_infer_png():
    # Make a tiny black image and encode as PNG bytes
    img = np.zeros((10, 10, 3), dtype=np.uint8)
    ok, buf = cv2.imencode(".png", img)
    assert ok
    files = {"file": ("test.png", buf.tobytes(), "image/png")}
    r = client.post("/infer", files=files)
    assert r.status_code == 200
    assert r.headers["content-type"] == "image/png"
