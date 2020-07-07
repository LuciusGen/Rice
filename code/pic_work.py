from create_pics import find_dirs
import cv2
import os


def create_dir():
    """Create dir for treatment pictures"""
    code_dir = os.path.abspath(os.curdir)
    tmp = code_dir.split("\\")
    tmp.pop()
    main_dir = "\\".join(tmp)
    dir = main_dir + "\\" + "plants_treat_photo"

    try:
        os.mkdir(dir)
    except FileExistsError:
        pass

    return dir


def pic_treatment(pic_name, dir):
    """Picture treat, use mask"""
    image = cv2.imread(pic_name) #  use BGR colors
    MASK_CONST_G = 155 #  bigger then 140 because of noises
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #  change colors to RGB

    for i in range(len(image)):
        for j in range(len(image[i])):
            if (image[i][j][1] >= MASK_CONST_G) & (image[i][j][0] < image[i][j][1]) \
                    & (image[i][j][2] < image[i][j][1]): #  use mask
                pass
            else:
                image[i][j] = [0, 0, 0] #  black color
    tmp = pic_name.split("\\")
    pic_name = tmp.pop()

    cv2.imwrite(dir + "\\" + pic_name, image) #  save pic


def treat_all_pics():
    """Treat all pictures in director with photos"""
    _, pic_dir = find_dirs()
    treat_dir = create_dir()

    for dirs in os.listdir(pic_dir):
        main_dir = treat_dir + "\\" + dirs
        try:
            os.mkdir(main_dir)
        except FileExistsError:
            pass

        for pic_name in os.listdir(pic_dir + "\\" + dirs):
            pic_treatment(pic_dir + "\\" + dirs + "\\" + pic_name, main_dir)


if __name__ == '__main__':
    treat_all_pics()
