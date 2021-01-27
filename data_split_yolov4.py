import os.path
import pandas
from os import listdir
from os.path import isfile, join
import numpy
import cv2
import os
from PIL import Image
import numpy as np
import sys

# iterate through each csv file and write the data to txt file
def dfiteration(df,a):
  for x,y in df.iterrows():
      # print (y[0])
      # func(y[0],a)
    list1 = y[0].split(';') 

    x1_min = int(list1[3])
    y1_min = int(list1[4])
    x2_min = int(list1[5])
    y2_min = int(list1[6])
    classId = list1[len(list1)-1]

    SOURCE_Train = "/home/ajit/Desktop/master_project/coco128/images/train2017"
    SOURCE_Test = "/home/ajit/Desktop/master_project/coco128/images/test2017"

    filename_Train = a+"_"+(list1[0].split('.')[0])+".jpg"
    image_path_train = SOURCE_Train +'/'+ filename_Train
    image_path_test = SOURCE_Test +'/'+ filename_Train

    
    if os.path.isfile(image_path_train):
        data = f'{image_path_train} {x1_min},{y1_min},{x2_min},{y2_min},{classId}'
        # writedata("train",data)
        print("dfdddsf",data)
        path ="/home/ajit/Desktop/master_project/pytorch-YOLOv4/data/train.txt"
        with open(path, "a") as file_object:
        # Append 'hello' at the end of file
          # file_object.write(data)
            if("42_00005_00029.jpg 6,5,56,54,42" in data):
              file_object.write(data)
            else:
              file_object.write(data+"\n")
              # file_object.close()
    elif os.path.isfile(image_path_test):
        data = f'{image_path_test} {x1_min},{y1_min},{x2_min},{y2_min},{classId}'
        print("kkkkkkkk",data)
        path ="/home/ajit/Desktop/master_project/pytorch-YOLOv4/data/val.txt"
        with open(path, "a") as file_object:
            # Append 'hello' at the end of file
            # file_object.write(data)
            if("42_00005_00025.jpg 6,6,44,44,42" in data):
              file_object.write(data)
            else:
              file_object.write(data+"\n")
            # file_object.write(data+"\n")
              # file_object.close()
    else:
      print("file not found: ", image_path_train)



# delete the existing txt files
def delete_existing_file():
  train_label_path_file ="/home/ajit/Desktop/master_project/pytorch-YOLOv4/data/train.txt"
  val_label_path_file ="/home/ajit/Desktop/master_project/pytorch-YOLOv4/data/val.txt"
  if os.path.isfile(train_label_path_file):
    os.remove(train_label_path_file)
    if os.path.isfile(train_label_path_file)==False:
      print("deleted train.txt")
  if os.path.isfile(val_label_path_file):
    os.remove(val_label_path_file)
    if os.path.isfile(val_label_path_file)==False:
      print("deleted val.txt")

# read csv files 
def read_csv_files():
  for i in range(43):
    # i= i + 11
      if i < 10:
        a = '0' + str(i)
      else:
        a = str(i)
      print("a",a)
  # a =  '01'
      Input_dir = "/home/ajit/Desktop/master_project/YOLO_format_data/Annotations/"       
      # output_dir = "/content/drive/MyDrive/Annotations/"       

      Input_dir = os.path.join(Input_dir, 'GT-000%s.csv' % a)
      df = pandas.read_csv(Input_dir)
      dfiteration(df,a) 
    # print(df)

def rr():
  # filename = "./data/tr.txt"
  # with open('./data/train.txt', 'r', encoding='utf-8') as inFile,\
  #    open('./data/train1.txt', 'w', encoding='utf-8') as outFile:
  #   for line in inFile:
  #       if line.strip():
  #           outFile.write(line)

  # with open(filename) as filehandle:
  #       lines = filehandle.readlines()
  # with open(filename, 'w') as filehandle:
  #       lines = filter(lambda x: x.strip(), lines)
  #       filehandle.writelines(lines) 

  # with open(filename) as f:
  #   for line in f:
  #       if not line.isspace():
  #           sys.stdout.write(line)

  fh = open("./data/train1.txt", "r")
  lines = fh.readlines()
  fh.close()

  # Weed out blank lines with filter
  lines = filter(lambda x: not x.isspace(), lines)

  # Write
  fh = open("./data/tr.txt", "w")
  fh.write("".join(lines))
  # should also work instead of joining the list:
  # fh.writelines(lines)
  fh.close()

def check_duplicates():
    # os.remove('./data/tr.txt')
    lines_seen_train = set()  # holds lines already seen
    lines_seen_val = set()  # holds lines already seen
    # outfile = open('./data/tr.txt', "w")
    infile_train = open('./data/train.txt', "r")
    infile_val = open('./data/val.txt', "r")
    i=0
    for line1,line2 in zip(infile_train,infile_val):
        # print line
        if line1 not in infile_train:  # not a duplicate
            # outfile.write(line)
          lines_seen_train.add(line1)
        else:
          i+=1
          print("the duplicate in train.txt: ",line)

        if line2 not in infile_val:  # not a duplicate
            # outfile.write(line)
          lines_seen_val.add(line2)
        else:
          i+=1
          print("the duplicate in val.txt: ",line)
    infile_train.close()
    infile_val.close()
    if(i==0):
      print ("No duplicates found in txt files")



delete_existing_file()
read_csv_files()
check_duplicates()
# rr()