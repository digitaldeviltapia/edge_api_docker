
from fastapi import FastAPI, File, UploadFile, Query
from fastapi.responses import Response, JSONResponse
from app.utils import canny_bytes


app = FastAPI(
    title="CV API Tapia",
    version="0.1.1",
    description="Edge and thresholds",
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/infer")
async def infer(
    file: UploadFile = File(...),
    t1: int = Query(100, ge=0, le=1000, description="Lower Canny threshold"),
    t2: int = Query(200, ge=0, le=1000, description="Upper Canny threshold"),
):
    # Accept common image types
    if file.content_type not in ("image/png", "image/jpeg"):
        return JSONResponse({"error": "send a PNG or JPEG"}, status_code=415)

    data = await file.read()

    try:
        png = canny_bytes(data, t1=t1, t2=t2)
    except ValueError as e:
        return JSONResponse({"error": str(e)}, status_code=400)

    return Response(content=png, media_type="image/png")
