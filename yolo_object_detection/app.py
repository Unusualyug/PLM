"""YOLO Object Detection Studio - Flask web app.

Run:  python app.py   ->  http://127.0.0.1:5001
"""
from __future__ import annotations

import base64
import csv
import io
import os
import time
from collections import Counter
from pathlib import Path

from flask import Flask, jsonify, render_template, request, send_file
from werkzeug.utils import secure_filename

import detector

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "static" / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
(BASE_DIR / "static" / "results").mkdir(parents=True, exist_ok=True)

IMAGE_EXT = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}
VIDEO_EXT = {".mp4", ".avi", ".mov", ".mkv", ".webm"}

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 200 * 1024 * 1024  # 200 MB


def _parse_classes(raw: str | None) -> list[int] | None:
    if not raw:
        return None
    ids = [int(x) for x in raw.split(",") if x.strip().isdigit()]
    return ids or None


@app.route("/")
def index():
    return render_template("index.html")


@app.get("/api/classes")
def api_classes():
    """Class list of the active model, so the UI can offer a class filter."""
    try:
        names = detector.class_names()
        return jsonify({"ok": True, "classes": [{"id": i, "name": n} for i, n in names.items()]})
    except Exception as exc:  # weights not downloaded yet / offline
        return jsonify({"ok": False, "error": str(exc)}), 503


@app.post("/api/detect")
def api_detect():
    """Image or video upload -> annotated output + stats."""
    file = request.files.get("file")
    if not file or not file.filename:
        return jsonify({"ok": False, "error": "No file uploaded"}), 400

    conf = float(request.form.get("conf", 0.25))
    iou = float(request.form.get("iou", 0.45))
    classes = _parse_classes(request.form.get("classes"))
    track = request.form.get("track", "true") == "true"

    name = secure_filename(file.filename)
    ext = Path(name).suffix.lower()
    saved = UPLOAD_DIR / f"{int(time.time() * 1000)}_{name}"
    file.save(saved)

    try:
        if ext in IMAGE_EXT:
            data = detector.detect_image(saved, conf=conf, iou=iou, classes=classes)
            data["kind"] = "image"
        elif ext in VIDEO_EXT:
            data = detector.detect_video(saved, conf=conf, iou=iou, classes=classes, track=track)
            data["kind"] = "video"
        else:
            return jsonify({"ok": False, "error": f"Unsupported file type: {ext}"}), 400
    except Exception as exc:
        return jsonify({"ok": False, "error": str(exc)}), 500

    data["ok"] = True
    return jsonify(data)


@app.post("/api/detect_frame")
def api_detect_frame():
    """Live webcam: browser posts a base64 JPEG frame, gets boxes back as JSON."""
    payload = request.get_json(silent=True) or {}
    raw = payload.get("image", "")
    if "," in raw:
        raw = raw.split(",", 1)[1]
    if not raw:
        return jsonify({"ok": False, "error": "No frame"}), 400

    import numpy as np
    import cv2

    buf = np.frombuffer(base64.b64decode(raw), dtype=np.uint8)
    frame = cv2.imdecode(buf, cv2.IMREAD_COLOR)
    if frame is None:
        return jsonify({"ok": False, "error": "Bad frame"}), 400

    conf = float(payload.get("conf", 0.35))
    classes = payload.get("classes") or None

    try:
        model = detector.get_model()
        t0 = time.perf_counter()
        res = model.predict(frame, conf=conf, classes=classes, verbose=False)[0]
        dets = [
            {
                "label": res.names[int(b.cls[0])],
                "confidence": round(float(b.conf[0]), 3),
                "box": [round(float(v), 1) for v in b.xyxy[0]],
            }
            for b in res.boxes
        ]
    except Exception as exc:
        return jsonify({"ok": False, "error": str(exc)}), 500

    return jsonify(
        {
            "ok": True,
            "detections": dets,
            "counts": dict(Counter(d["label"] for d in dets)),
            "inference_ms": round((time.perf_counter() - t0) * 1000, 1),
            "frame_size": [frame.shape[1], frame.shape[0]],
        }
    )


@app.get("/api/log")
def api_log():
    """Summary of everything detected so far (powers the analytics panel)."""
    path = detector.LOG_FILE
    if not path.exists():
        return jsonify({"ok": True, "rows": 0, "counts": {}})
    with path.open() as fh:
        rows = list(csv.DictReader(fh))
    return jsonify(
        {"ok": True, "rows": len(rows), "counts": dict(Counter(r["label"] for r in rows).most_common(15))}
    )


@app.get("/api/log.csv")
def api_log_csv():
    path = detector.LOG_FILE
    if not path.exists():
        return jsonify({"ok": False, "error": "No detections logged yet"}), 404
    return send_file(path, as_attachment=True, download_name="detections_log.csv")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)
