from PIL import Image
import numpy as np
import cv2
import pandas as pd

def getmask(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.medianBlur(gray, 3)
    (T, threshInv) = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    return (threshInv)


proportions = []
idx_image = []
tags = []
for test_img in range(1, 16):
    before_path = f"ground_truths_imgs/image_{test_img}_raw.png_0.png"
    for idx in range(1, 11):
        after_path = f"/Users/cathv/Desktop/PhD/Side Projects/GANS/HerbiEstim/imgs_standardized/test/image_{test_img}_damage_{idx}.png_0.png"
        
        imagereal = cv2.imread(after_path)
        mask = getmask(imagereal)
        d1 = np.count_nonzero(mask)

        imagefake = cv2.imread(before_path)
        mask2 = getmask(imagefake)
        d2 = np.count_nonzero(mask2)

        proportion = (d2 - d1) / d2
        proportions.append(proportion)
        tags.append(f"image_{test_img}_damage_{idx}.png")

df = pd.DataFrame.from_dict({"img.tag":tags, "proportion":proportions})
df.to_csv("ground_truths.csv", index=False)
