import numpy as np
import cv2
import os
import cvxpy as cp

path = "Final/Data/paper/"


def row_location(left, imgs):
    scores = inWhichRow(left, imgs)
    print(scores)
    return scores


def inWhichRow(left, imgs):
    scores = np.zeros([19, 209])
    for i in range(len(left)):
        element_location_left = start_end(left[i])
        for j in range(len(imgs)):
            scores[i, j] = compare_start_end(element_location_left, imgs[j])
    return scores


def compare_start_end(element_location_left, img1):
    element_location = start_end(img1)
    return np.sum(np.abs(element_location_left - element_location))


def getC(img0, img1):
    element_location_left = img0[:, -1]
    element_location_right = img1[:, 0]
    return np.sum(np.abs(element_location_left - element_location_right))


def getSim(imgs, left_img, right):
    c = np.zeros([len(right), 1])
    for i in range(len(right)):
        c[i] = getC(left_img, imgs[right[i]])
    index = np.argmin(c)
    return index, right[i]


def start_end(img0):
    element_location = np.zeros([180, 1])
    for i in range(180):
        if (img0[i, :] - 255).any():
            element_location[i] = 1
    return element_location


def read_img(path):
    file_name = os.listdir(path)
    imgs = []
    m = 0
    n = 0
    for i in file_name:
        name = path + i
        img = cv2.imread(name, cv2.IMREAD_GRAYSCALE)
        t, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
        imgs.append(img)
    return imgs, file_name


imgs, file_name = read_img(path)
M = 19
N = 0
dictionary = dict()
base = imgs[0]
for img, name in zip(imgs, file_name):
    temp = (img[:, 0] - 255)
    n_nonzero = np.count_nonzero(temp)
    dictionary[name] = n_nonzero
    if not temp.any():
        N = N + 1
        base = np.concatenate([base, img], axis=0)
print(N)

cv2.imshow("title", base)
cv2.imwrite("img.jpg", base)
cv2.waitKey(0)

test = np.concatenate([imgs[0], imgs[7]], axis=1)
cv2.imshow("title", test)
cv2.imwrite("img.jpg", test)
cv2.waitKey(0)

left = []
new_sys2 = sorted(dictionary.items(), key=lambda d: d[1], reverse=False)
for i in range(19):
    index = int(new_sys2[i][0][:3])
    left.append(imgs[index])

scores = row_location(left, imgs)
print(scores.shape)

row_answer = []
for i in range(19):
    row_answer.append([])
    row_answer[i] = []

for i in range(209):
    data = scores[:, i]
    for j in range(1, 19):
        index = np.argsort(data)[j]
        if len(row_answer[index]) == 11:
            continue
        else:
            row_answer[index].append(i)
            break

print(row_answer)
# test = imgs[row_answer[15][0]]
# for i in range(1, 11):
#     test = np.concatenate([test, imgs[row_answer[15][i]]], axis=1)
# cv2.imshow("title", test)
# cv2.imwrite("img.jpg", test)
# cv2.waitKey(0)

col_answer = []
for i in range(19):
    col_answer.append([])
    col_answer[i] = []

for i in range(19):
    left_cur = left[i]
    while len(row_answer[i]) != 0:
        index, right = getSim(imgs, left_cur, row_answer[i])
        col_answer[i].append(row_answer[i][index])
        left_cur = imgs[row_answer[i].pop(index)]
print(len(col_answer[17]))
col_answer[17].append(col_answer[17][3])
for i in range(19):
    test = imgs[col_answer[i][0]]
    temp = col_answer[i]
    for j in range(1, 11):
        print(i, j)
        index = col_answer[i][j]
        test = np.concatenate([test, imgs[index]], axis=1)
    if i == 0:
        base = test
    else:
        base = np.concatenate([base, test], axis=0)

cv2.imshow("title", base)
cv2.imwrite("img.jpg", base)
cv2.waitKey(0)