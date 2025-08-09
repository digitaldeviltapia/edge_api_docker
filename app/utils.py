
import io
import cv2
import numpy as np
from PIL import Image


def canny_bytes(img_bytes: bytes, t1: int = 100, t2: int = 200) -> bytes:
    if not img_bytes:
        raise ValueError("empty file")

    arr = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError("could not decode image")

    edges = cv2.Canny(img, t1, t2)
    pil = Image.fromarray(edges)
    buf = io.BytesIO()
    pil.save(buf, format="PNG")
    return buf.getvalue()
