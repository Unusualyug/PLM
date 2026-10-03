# YOLO Object Detection Studio

A complete, submission-ready object detection project built on **Ultralytics YOLO11** with a Flask web interface.

## Features
- **Image detection** — upload a photo, get an annotated result, per-object table (class, confidence, bounding box) and class counts.
- **Video detection + tracking** — upload a clip, YOLO + ByteTrack annotates every frame, reports total detections *and* unique tracked objects per class.
- **Live webcam detection** — browser camera frames are streamed to the server and boxes are drawn on a canvas overlay in real time, with live inference latency.
- **Tunable inference** — confidence threshold, IoU/NMS threshold and class filtering, all from the UI.
- **Analytics** — every detection is appended to `static/results/detections_log.csv`; the Analytics tab charts the most frequent classes and the log is downloadable.
- **Custom training** — `train_custom.py` fine-tunes YOLO on your own labelled dataset and exports ONNX.

## Setup
```bash
cd yolo_object_detection
pip install -r requirements.txt
python app.py
# open http://127.0.0.1:5001
```
The first run downloads `yolo11n.pt` (~5 MB) automatically — you need internet once.
Out of the box it detects the 80 COCO classes (person, car, bottle, laptop, dog, …).

## Using your own model
1. Collect and label images (Roboflow, LabelImg or CVAT), export in **YOLOv8** format into `dataset/`.
2. Edit `dataset/data.yaml` with your class names.
3. Train:
   ```bash
   python train_custom.py --model yolo11s.pt --epochs 100 --device 0
   ```
4. Copy `runs/detect/custom/weights/best.pt` into `models/` and run:
   ```bash
   YOLO_WEIGHTS=best.pt python app.py
   ```

## Project structure
```
yolo_object_detection/
├── app.py              # Flask routes / REST API
├── detector.py         # model loading, image & video inference, CSV logging
├── train_custom.py     # fine-tuning + validation + ONNX export
├── templates/index.html
├── static/app.js, style.css
├── dataset/data.yaml   # custom dataset template
└── models/             # drop best.pt here
```

## API
| Endpoint | Method | Purpose |
|---|---|---|
| `/api/classes` | GET | class list of the active model |
| `/api/detect` | POST | multipart image/video upload → annotated output + stats |
| `/api/detect_frame` | POST | JSON `{image: base64}` → detections (webcam loop) |
| `/api/log` | GET | aggregated detection counts |
| `/api/log.csv` | GET | download full detection log |

## How it works (for the report)
1. **Backbone/Neck/Head** — YOLO11 is a single-stage detector: a CSP-style backbone extracts features, a PANet-like neck fuses multi-scale features, and an anchor-free decoupled head predicts boxes + classes in one forward pass.
2. **Post-processing** — confidence filtering followed by Non-Maximum Suppression (IoU threshold) removes duplicate boxes.
3. **Tracking** — ByteTrack associates detections across frames by IoU + confidence so each object keeps a stable ID, enabling unique-object counting.
4. **Metrics to report** — precision, recall, mAP@0.5, mAP@0.5:0.95 (printed by `train_custom.py`), plus FPS/latency shown live in the UI.

## Suggested extensions
- Line-crossing counter (people/vehicle in-out counting)
- Alerting (Telegram/email) when a target class appears
- Export to ONNX / TensorRT and deploy on Raspberry Pi or Jetson Nano
- Swap in a domain dataset: PPE safety, traffic, waste segregation, number plates
