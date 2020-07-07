import cv2
import time
import os


def find_dirs():
    """Find dir with video data and create dir with pictures"""
    code_dir = os.path.abspath(os.curdir)
    tmp = code_dir.split("\\")
    tmp.pop()
    main_dir = "\\".join(tmp)

    video_dir = main_dir + "\\" + "plants_videos"
    photo_dir = main_dir + "\\" + "plants_photo"

    try:
        os.mkdir(photo_dir)
    except FileExistsError:
        pass

    return video_dir, photo_dir


def find_all_pics():
    """Find frames foreach video in dir"""
    TIME_DELTA = 0.04
    video_dir, photo_dir = find_dirs()

    for video in os.listdir(video_dir):  # foreach video in dir
        video_name = video.split(".")[0]  # find video name without format
        try:
            os.mkdir(photo_dir + "\\" + video_name)  # create photo dir foreach video
        except FileExistsError:
            pass
        cap = cv2.VideoCapture(video_dir + "\\" + video)  # open video

        t = time.time()
        counter = 0
        success = True

        while success:
            success, img = cap.read()  # read video data

            if time.time() - t >= TIME_DELTA:  # time delta that we need
                t = time.time()
                cv2.imwrite(photo_dir + "\\" + video_name + "\\" + str(counter) + ".jpg", img)  # create pic
                counter += 1


if __name__ == "__main__":
    find_all_pics()
