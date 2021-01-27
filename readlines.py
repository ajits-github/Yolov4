import os, os.path

def function():
    TRAIN_DIR = "/home/ajit/Desktop/master_project/coco128/images/train2017"
    TEST_DIR = "/home/ajit/Desktop/master_project/coco128/images/test2017"
    count_train = len(open("/home/ajit/Desktop/master_project/pytorch-YOLOv4/data/train.txt").readlines())
    count_test = len(open("/home/ajit/Desktop/master_project/pytorch-YOLOv4/data/val.txt").readlines())
    print("count_train in train.txt:",count_train)
    print("count_test in val.txt:",count_test)
    print("Number of training images",len([name for name in os.listdir(TRAIN_DIR) if os.path.isfile(os.path.join(TRAIN_DIR, name))]))
    print("Number of test images",len([name for name in os.listdir(TEST_DIR) if os.path.isfile(os.path.join(TEST_DIR, name))]))
function()