"""Fine-tune YOLO on your own dataset.

1. Label images (Roboflow / LabelImg / CVAT) and export in "YOLOv8" format.
2. Put them in dataset/ following the structure in dataset/data.yaml.
3. python train_custom.py --epochs 80 --model yolo11n.pt
4. Copy runs/detect/train/weights/best.pt into models/ and run:
       YOLO_WEIGHTS=best.pt python app.py
"""
import argparse
from pathlib import Path

BASE = Path(__file__).resolve().parent


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--model", default="yolo11n.pt", help="base weights (n/s/m/l/x)")
    p.add_argument("--data", default=str(BASE / "dataset" / "data.yaml"))
    p.add_argument("--epochs", type=int, default=80)
    p.add_argument("--imgsz", type=int, default=640)
    p.add_argument("--batch", type=int, default=16)
    p.add_argument("--device", default="", help="'0' for GPU, 'cpu' for CPU")
    p.add_argument("--name", default="custom")
    args = p.parse_args()

    from ultralytics import YOLO

    model = YOLO(args.model)
    model.train(
        data=args.data,
        epochs=args.epochs,
        imgsz=args.imgsz,
        batch=args.batch,
        device=args.device or None,
        name=args.name,
        patience=20,
        plots=True,
    )
    metrics = model.val()
    print("mAP50-95:", metrics.box.map, "| mAP50:", metrics.box.map50)
    model.export(format="onnx")  # handy for deployment


if __name__ == "__main__":
    main()
