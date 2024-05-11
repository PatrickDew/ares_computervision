#!pip install roboflow

from roboflow import Roboflow
from ultralytics import YOLO
rf = Roboflow(api_key="JYslEMeQ30KTekAFx872")
project = rf.workspace("teambased-engineering-invention").project("ares")
dataset = project.version(2).download("yolov8")

#yolo task=detect mode=train  model=yolov8s.pt  data="C:\ARES Project - Tohoku University\Python Code\ARES-2\data.yaml"  epochs=20 imgsz=640