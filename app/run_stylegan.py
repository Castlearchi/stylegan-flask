import os

# このスクリプトのディレクトリのパスを取得
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(SCRIPT_DIR, "src")

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import torch


def run_stylegan(seed: int, savepath: str):
    torch.manual_seed(seed)
    load_model = torch.jit.load(os.path.join(SRC_DIR, "stylegan_ffhq1024.pt")).eval()
    test_sample_input_trace = torch.randn(1, 512)
    result = load_model(test_sample_input_trace)
    img = ARGB2image(result.detach().numpy())
    img.save("app/static/result.png")
    return


def ARGB2image(data):
    # データをARGB形式に変換する
    a = (data >> 24) & 0xFF
    r = (data >> 16) & 0xFF
    g = (data >> 8) & 0xFF
    b = data & 0xFF

    # PIL Imageを作成する
    rgb_data = np.dstack((r, g, b)).astype(np.uint8)
    image = Image.fromarray(rgb_data)
    return image


if __name__ == "__main__":
    run_stylegan(100, "result_img/test.png")
