import os
path = os.path.abspath('.')
print(path)
data_path = path + "\\train_data\\train_data"
print(data_path)
os.listdir(data_path)
#picture size
img_rows, img_cols = 320, 320
img_channels = 3
def get_lable_imgpath(train_data_path):
    label = []
    img_path = []
    for i in os.listdir(train_data_path):
        a = i.split('.')
        if a[1]=='txt':
    #print(i)
            with open(train_data_path+'\\'+str(i)) as f:
                f = f.readline()
                f = f.split(',')
                if random.random() < 0.7 :
                    label.append(f[1].strip())
                    img_path.append(f[0])
    return label,img_path

from numpy import *
import cv2 as cv
def process_imgdata(_img_path):
    x_train = []
    for i in _img_path:
        pic = cv.imread(i)
        pic = cv.resize(pic,(320,320),interpolation=cv.INTER_CUBIC)
        x_train.append(pic.astype('float32'))
    return array(x_train)

label,img_path = get_lable_imgpath(data_path)
X_train = process_imgdata(img_path)