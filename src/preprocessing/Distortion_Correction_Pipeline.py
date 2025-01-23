# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] id="iKPNtZXXPTB-"
# # Distortion Correction Pipeline
#
#

# %% [markdown] id="hbqLcYSvRj1x"
# ## Load Libraries

# %% id="PeqRA7Ok3NyR"
import cv2
import numpy as np
from matplotlib import pyplot as plt

# %% [markdown] id="glFbOKzuP7DH"
# ## Visualize Test Image

# %% colab={"base_uri": "https://localhost:8080/", "height": 435} id="tXMYnCoo3Pe2" outputId="5c49f5ed-c95d-452c-bf97-05c91f8019c1"
im = cv2.imread("../../img/test/Rusted_Ventral.JPG").astype(float)
im = im[:, :, ::-1]

plt.imshow(im.astype(np.uint8))
plt.show()

# %% [markdown] id="43eu-7UFQLaW"
# ## Create a Redness Grayscale Map  

# %% [markdown] id="Jl5Z2rxhQUZ3"
# ### Create a measure of redness

# %% id="oug0h_-0uzjL"
redness = im[:,:,0] / (im[:,:,1] + im[:,:,2] + 1)

# %% colab={"base_uri": "https://localhost:8080/"} id="YYXnBz5uQuJe" outputId="e96e41e7-e8be-4102-caf2-195384a3c090"
print(np.max(redness), np.min(redness), np.median(redness))

# %% [markdown] id="2-al1Pu6Qj-d"
# ### Create a redness matrix

# %% id="Hu5FWKnnQoAC"
red_clip = 2
redness[redness>red_clip] = red_clip

# %% [markdown] id="QvIo7LvOQo0K"
# ### Display the redness map

# %% colab={"base_uri": "https://localhost:8080/", "height": 435} id="Qo6br5Xy4wcU" outputId="14bc5d15-3b30-41e9-d1f4-388bdafa67d8"
r_display = redness / red_clip * 255

plt.gray()
plt.imshow(r_display.astype(np.uint8))
plt.show()

# %% [markdown] id="DKr1H5ePQzuy"
# ## Identify the Redness Threshold

# %% [markdown] id="h_4QBYZFQ24-"
# ### Display the Redness Histogram for the Test Image
#
#

# %% colab={"base_uri": "https://localhost:8080/", "height": 792} id="8sSDBsma4VPq" outputId="e29411aa-db1d-4afd-e808-c61661a11982"
flat_display = r_display.flatten()
plt.hist(flat_display, bins=50)


# %% [markdown] id="SKo4YLhpROTy"
# ### Assign a threshold based on the analysis of the histogram

# %% id="ath626FkRVpW"
thresh = 120

# %% [markdown] id="BCOhSgmiRXh4"
# ### Create a binary matrix

# %% id="H4zk3ikP4mY3"
_, thresholded_image = cv2.threshold(r_display, 120, 255, cv2.THRESH_BINARY)


# %% [markdown] id="YE0EzHZ3Rctn"
# ### Display the binary matrix

# %% colab={"base_uri": "https://localhost:8080/", "height": 435} id="Uyar3LbVRpJ3" outputId="4016ff02-6be2-4d78-d8e4-0d453bff40e6"
plt.gray()
plt.imshow(thresholded_image.astype(np.uint8))
plt.show()

# %% [markdown] id="cSA0tfmtR1d0"
# ## Apply morphological transformations to highlight the red dots

# %% [markdown] id="fqPNVc5DSBZG"
# ### Apply a Close then Open Transform

# %% id="NyIVokHEBFzp"
kernel = np.ones((5,5),np.uint8)

after_close = cv2.morphologyEx(thresholded_image,cv2.MORPH_CLOSE,kernel)
im_close_first = cv2.morphologyEx(after_close,cv2.MORPH_OPEN,kernel)


# %% [markdown] id="aVDWZ8puSVa-"
# ### Visualize the Transformation

# %% colab={"base_uri": "https://localhost:8080/", "height": 552} id="u3G3TrI_BOPR" outputId="e4fd7e85-ffa8-4a42-a311-5f9042e8ba6a"

plt.figure(figsize=(15,15))
plt.subplot(121)
plt.axis("off")
plt.imshow(thresholded_image)
plt.title("Before Transform")
plt.subplot(122)
plt.axis("off")
plt.imshow(im_close_first)
plt.title("After Transform")
plt.show()

# %% [markdown] id="ed-O2-ruSl19"
# ## Cluster the pixels through connected components

# %% [markdown] id="X8WLb2HzS7yl"
# ### Run Connected Components Labeling on the Morphologically Transformed Image

# %% colab={"base_uri": "https://localhost:8080/"} id="xBeHmpdW5GGM" outputId="31ce4de3-1ae7-44e3-ffe9-43635709f3b3"
connectivity = 8
num_labels, labels, stats, centroids = \
    cv2.connectedComponentsWithStats(im_close_first.astype(np.uint8), connectivity, cv2.CV_32S)
print('Number of connected components:', num_labels-1)  # the background is one of the "labels"
print('\nHere are the stats:')
print('Upper left and lower right pixel, plus area')
print(stats)
print('\nHere are the centroids')
print(centroids)


# %% [markdown] id="rp7xYZ_QS6Hc"
# ### Sort the clusters by size

# %% id="DNXLPh3o9lqX"
sizes = stats[:, cv2.CC_STAT_AREA]

ind = np.argsort(sizes)
sizes = sizes[ind]
centroids = centroids[ind]

# %% colab={"base_uri": "https://localhost:8080/"} id="Pi8GqaUa-8mT" outputId="bbe7467d-4d93-42de-c3dc-98c5f1af17f9"
centroids

# %% [markdown] id="Fz19edwFTWzY"
# ### Concatenate the Centroids Coordinates Matrix with the Area Array

# %% id="Bks4IO-f_rxm"
sizes = sizes.reshape((sizes.shape[0], 1))
concat_array = np.concatenate((centroids, sizes), axis=1)
concat_array = concat_array[::-1]

# %% [markdown] id="ATUSlY5cTmOc"
# ### Filter the Clusters by Size

# %% id="0S7PD_V-AfJG"
condition = concat_array[:, 2] > 1000
filtered_data = concat_array[condition]

# %% [markdown] id="lTLd3eBgTyyx"
# ### Extract the four red dots

# %% id="8lUlS-S5NlZu"
right_point = filtered_data[np.argmax(filtered_data[:, 0])]
left_point = filtered_data[np.argmin(filtered_data[:, 0])]
lower_point = filtered_data[np.argmax(filtered_data[:, 1])]
upper_point = filtered_data[np.argmin(filtered_data[:, 1])]

point_A = [upper_point[0], upper_point[1]]  # Top point
point_B = [lower_point[0], lower_point[1]]  # Bottom point
point_C = [left_point[0], left_point[1]]  # Left point
point_D = [right_point[0], right_point[1]]  # Right point

# %% [markdown] id="yy27I3DxT1nb"
# ### Visualize the red dots

# %% colab={"base_uri": "https://localhost:8080/", "height": 435} id="6LvF2z0aASng" outputId="de432ec1-00fb-42bb-9007-7d7d53378bc8"
plt.gray()
plt.imshow(thresholded_image.astype(np.uint8))
plt.scatter(point_A[0], point_A[1], color='cyan')
plt.scatter(point_B[0], point_B[1], color='lime')
plt.scatter(point_C[0], point_C[1], color='fuchsia')
plt.scatter(point_D[0], point_D[1], color='red')
plt.show()


# %% [markdown] id="QvULbK6LT6f5"
# ## Correct the Distortion in the Image

# %% [markdown] id="9Jl8Nq2TUCJT"
# ### Utility function

# %% id="lvnhYyQzUAWv"
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


# %% [markdown] id="2qu3iKQ7Ui0R"
# ### Define the Input Points

# %% id="_zlrL5k_UlNO"
input_points = np.array([point_A, point_B, point_C, point_D], dtype='float32')

# %% [markdown] id="0yj5QEAEUEPv"
# ### Define the Destination Points

# %% id="v-AB_moBjeh2"
rect_width = int(euclidean_distance(point_C, point_D))
rect_height = int(euclidean_distance(point_A, point_B))

output_points = np.array([
    [rect_width // 2, 0],           # Top middle
    [rect_width // 2, rect_height], # Bottom middle
    [0, rect_height // 2],          # Left middle
    [rect_width, rect_height // 2]  # Right middle
], dtype='float32')

# %% [markdown] id="REHb1TiPUud7"
# ### Compute the Perspective Transform Matrix

# %% id="zbQwWQVAUwve"
matrix = cv2.getPerspectiveTransform(input_points, output_points)

# %% [markdown] id="65NzAVXpUzEH"
# ### Apply the Transformation to obtain the Transformed Image

# %% id="u9jYa-6xU65m"
transformed_image = cv2.warpPerspective(im, matrix, (rect_width, rect_height))


# %% [markdown] id="J1Akm-fMU9cG"
# ### Visualize the result

# %% colab={"base_uri": "https://localhost:8080/", "height": 574} id="HJgRN0bVVLZK" outputId="cd474072-0087-4957-812f-e47eafa13251"
plt.figure(figsize=(15,15))
plt.subplot(121)
plt.axis("off")
plt.imshow(im.astype(np.uint8))
plt.title("Before Distortion Correction")
plt.subplot(122)
plt.axis("off")
plt.imshow(transformed_image.astype(np.uint8))
plt.title("After Distortion Correction")
plt.show()
