import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def load_image(path: str) -> np.ndarray:
    img = Image.open(path).convert("RGB")  # garantit 3 canaux
    return np.array(img, dtype=np.uint8)   # shape (H,W,3), dtype uint8

img = load_image("pokeball.png")
original = img.copy()
current = original.copy()

def showImage(img: np.ndarray):
    plt.imshow(img)
    plt.xlabel("axis 1 (x / colonnes)")
    plt.ylabel("axis 0 (y / lignes)")
    plt.show()

showImage(current)