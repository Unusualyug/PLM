"""Core YOLO detection helpers (model loading, image/video inference)."""
from __future__ import annotations

import csv
import os
import time
from collections import Counter
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent
MODELS_DIR = BASE_DIR / "models"
RESULTS_DIR = BASE_DIR / "static" / "results"
LOG_FILE = BASE_DIR / "static" / "results" / "detections_log.csv"

# Set CUSTOM_MODEL env var (or drop best.pt in models/) to use your trained model.
DEFAULT_WEIGHTS = os.environ.get("YOLO_WEIGHTS", "yolo11n.pt")

_model_cache: dict[str, Any] = {}


def get_model(weights: str | None = None):
    """Load (and cache) a YOLO model. Downloads pretrained weights on first use."""
    weights = weights or DEFAULT_WEIGHTS
    if weights in _model_cache:
        return _model_cache[weights]

    from ultralytics import YOLO  # imported lazily so the web UI boots instantly

    local = MODELS_DIR / weights
    path = str(local) if local.exists() else weights
    model = YOLO(path)
    _model_cache[weights] = model
    return model


def class_names(weights: str | None = None) -> dict[int, str]:
    return get_model(weights).names


def _summarise(result) -> list[dict]:
    names = result.names
    out = []
    for box in result.boxes:
        cls_id = int(box.cls[0])
        x1, y1, x2, y2 = (float(v) for v in box.xyxy[0])
        out.append(
            {
                "class_id": cls_id,
                "label": names[cls_id],
                "confidence": round(float(box.conf[0]), 4),
                "box": [round(x1, 1), round(y1, 1), round(x2, 1), round(y2, 1)],
            }
        )
    return out


def log_detections(source: str, detections: list[dict]) -> None:
    """Append every detection to a CSV so the project produces real analytics."""
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    new = not LOG_FILE.exists()
    with LOG_FILE.open("a", newline="") as fh:
        writer = csv.writer(fh)
        if new:
            writer.writerow(["timestamp", "source", "label", "confidence", "x1", "y1", "x2", "y2"])
        ts = time.strftime("%Y-%m-%d %H:%M:%S")
        for d in detections:
            writer.writerow([ts, source, d["label"], d["confidence"], *d["box"]])


def detect_image(
    image_path: str | Path,
    conf: float = 0.25,
    iou: float = 0.45,
    classes: list[int] | None = None,
    weights: str | None = None,
) -> dict:
    """Run detection on one image, save the annotated copy, return a JSON-ready dict."""
    model = get_model(weights)
    t0 = time.perf_counter()
    result = model.predict(
        source=str(image_path), conf=conf, iou=iou, classes=classes, verbose=False
    )[0]
    elapsed = (time.perf_counter() - t0) * 1000

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    out_name = f"det_{int(time.time() * 1000)}_{Path(image_path).stem}.jpg"
    out_path = RESULTS_DIR / out_name
    result.save(filename=str(out_path))

    detections = _summarise(result)
    log_detections(Path(image_path).name, detections)
    return {
        "output_image": f"results/{out_name}",
        "detections": detections,
        "counts": dict(Counter(d["label"] for d in detections)),
        "total": len(detections),
        "inference_ms": round(elapsed, 1),
        "image_size": [result.orig_shape[1], result.orig_shape[0]],
    }


def detect_video(
    video_path: str | Path,
    conf: float = 0.25,
    iou: float = 0.45,
    classes: list[int] | None = None,
    weights: str | None = None,
    track: bool = True,
    frame_stride: int = 1,
) -> dict:
    """Detect (and optionally track) through a video, writing an annotated MP4."""
    import cv2

    model = get_model(weights)
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        raise ValueError(f"Could not open video: {video_path}")

    fps = cap.get(cv2.CAP_PROP_FPS) or 25
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    out_name = f"det_{int(time.time() * 1000)}_{Path(video_path).stem}.mp4"
    writer = cv2.VideoWriter(
        str(RESULTS_DIR / out_name), cv2.VideoWriter_fourcc(*"avc1"), fps, (w, h)
    )

    totals: Counter = Counter()
    unique_ids: set[tuple[str, int]] = set()
    frames = 0
    t0 = time.perf_counter()
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        frames += 1
        if frame_stride > 1 and frames % frame_stride:
            continue
        if track:
            res = model.track(
                frame, conf=conf, iou=iou, classes=classes, persist=True, verbose=False
            )[0]
        else:
            res = model.predict(frame, conf=conf, iou=iou, classes=classes, verbose=False)[0]

        for box in res.boxes:
            label = res.names[int(box.cls[0])]
            totals[label] += 1
            if track and box.id is not None:
                unique_ids.add((label, int(box.id[0])))
        writer.write(res.plot())

    cap.release()
    writer.release()
    return {
        "output_video": f"results/{out_name}",
        "frames": frames,
        "seconds": round(time.perf_counter() - t0, 1),
        "detections_per_class": dict(totals),
        "unique_objects": dict(Counter(lbl for lbl, _ in unique_ids)) if track else {},
    }
