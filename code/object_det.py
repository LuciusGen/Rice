import cv2
import os
import functions as fp
import sys
treshould = 50 # pixel treshould
funcs = [fp.EXY_YIQ, fp.R_n, fp.ExG_RGB, fp.CIVE_RGB]
counter = 0
sys.setrecursionlimit(1000000)


def main(pic, neural):
    n_counter = 0
    for i in range(len(pic)):
        for j in range(len(pic[0])):
            if (pic[i][j][1] >= 155) & (pic[i][j][0] < pic[i][j][1]) \
                    & (pic[i][j][2] < pic[i][j][1]):
                object = list()
                global counter
                counter = 0
                find_obj(pic, object, i, j)
                if counter > treshould:
                    neural.append(list())
                    for k in funcs:
                        tmp = 0
                        for l in range(0, counter):
                            tmp += k(object[l])
                        neural[n_counter].append(tmp / (counter + 1))
                    n_counter += 1


def find_obj(pic, obj, i, j):
    if not (pic[i][j][1] >= 155) & (pic[i][j][0] < pic[i][j][1]) \
                    & (pic[i][j][2] < pic[i][j][1]):
        return
    obj.append([i for i in pic[i][j]])
    global counter
    counter += 1
    pic[i][j] = [0, 0, 0]

    if (i + 1) < len(pic):
        find_obj(pic, obj, i + 1, j)

    if (i - 1) >= 0:
        find_obj(pic, obj, i - 1, j)

    if (j + 1) < len(pic[0]):
        find_obj(pic, obj, i, j + 1)

    if (j - 1) >= 0:
        find_obj(pic, obj, i, j - 1)
