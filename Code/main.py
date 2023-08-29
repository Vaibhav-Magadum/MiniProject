import cv2,os
import pandas as pd
from ultralytics import YOLO
from tracker import*
model=YOLO('yolov8s.pt')
def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        colorsBGR = [x, y]
cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)
cap=cv2.VideoCapture(0)
my_file = open("coco.txt", "r")
data = my_file.read()
class_list = data.split("\n") 
count=0
tracker=Tracker()
cy1=0
cy2=0
offset=6
while True:    
    ret,frame = cap.read()
    if not ret:
        break
    count += 1
    if count % 3 != 0:
        continue
    frame=cv2.resize(frame,(480,360))
    results=model.predict(frame)
    a=results[0].boxes.boxes
    px=pd.DataFrame(a).astype("float")
    list=[]    
    for index,row in px.iterrows():
        x1=int(row[0])
        y1=int(row[1])
        x2=int(row[2])
        y2=int(row[3])
        d=int(row[5])
        c=class_list[d]
        if 'car' or 'bus' or 'motorcycle' or 'truck' in c:
            list.append([x1,y1,x2,y2])
        os.system('cls')
    bbox_id=tracker.update(list)
    for bbox in bbox_id:
        x3,y3,x4,y4,id=bbox
        cx=int((x3+x4)//2)+2
        cy=int((y3+y4)//2)+2
        cv2.circle(frame,(cx,cy),4,(0,0,255),-1)
        cv2.putText(frame,str("Vehicle"),(cx,cy),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,255),2)
    print(len(list))
    cv2.imshow("RGB", frame)
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()