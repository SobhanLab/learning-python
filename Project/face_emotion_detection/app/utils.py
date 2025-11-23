from pathlib import Path
from typing import Dict, Tuple
import json
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

TRANSFORM = transforms.Compose([
    transforms.Resize(64),
    transforms.CenterCrop((64, 64)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.5, 0.5, 0.5],
        std=[0.5, 0.5, 0.5]
    ),
])

def load_class_mapping(path: str = "models/class_mapping.json") -> Dict[int, str]:
    mapping_path = Path(path)
    if not mapping_path.exists():
        return {
            0: "Angry",
            1: "Disgust",
            2: "Fear",
            3: "Happy",
            4: "Sad",
            5: "Surprise",
            6: "Neutral"
        }
    with mapping_path.open("r", encoding="utf-8") as f:
        raw = json.load(f)
    return {int(k): v for k, v in raw.items()}

def build_model(num_classes: int, weights_path: str = "models/emotion_model.pth") -> nn.Module:
    weights_path = Path(weights_path)
    if not weights_path.exists():
        raise FileNotFoundError(str(weights_path))
    model = models.resnet18(weights=None)
    in_features = model.fc.in_features
    model.fc = nn.Linear(in_features, num_classes)
    state_dict = torch.load(weights_path, map_location=DEVICE)
    model.load_state_dict(state_dict)
    model.to(DEVICE)
    model.eval()
    return model

def preprocess_image(image: Image.Image) -> torch.Tensor:
    if image.mode != "RGB":
        image = image.convert("RGB")
    tensor = TRANSFORM(image)
    tensor = tensor.unsqueeze(0)
    return tensor.to(DEVICE)

def predict_emotion(
    input_tensor: torch.Tensor,
    model: nn.Module,
    class_mapping: Dict[int, str]
) -> Tuple[str, float]:
    with torch.no_grad():
        logits = model(input_tensor)
        probs = torch.softmax(logits, dim=1)
        conf, pred_idx = torch.max(probs, dim=1)
    idx = int(pred_idx.item())
    emotion_name = class_mapping.get(idx, f"Unknown ({idx})")
    confidence = float(conf.item())
    return emotion_name, confidence
