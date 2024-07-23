import streamlit as sl
import cv2
import time
import glob
import os
from threading import Thread
from sendmail import send_email

sl.title("Motion Detector")
start = sl.button(label="Start Camera", 
                  key="camerabutton")

def clear_folder():
    images = glob.glob("images/*.png")
    for i in images:
        os.remove(i)

if start:
    streamlit_image = sl.image([])
    camera = cv2.VideoCapture(0)
    time.sleep(1)
    first_frame = None
    status_list = []
    count = 0
    email_limit = 0

    while True:
        status = 0
        check, frame = camera.read()
        cv2.putText(img = frame, text = f"{time.strftime('%A')}",
                    org = (50,50), fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=2, color=(255,255,255),
                    thickness=2, lineType=cv2.LINE_AA)
        cv2.putText(img = frame, text = f"{time.strftime('%H:%M:%S')}",
                    org = (50,100), fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=2, color=(255,0,0),
                    thickness=2, lineType=cv2.LINE_AA)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_frame_gau = cv2.GaussianBlur(gray_frame, (21,21), 0)
        
        if first_frame is None:
            first_frame = gray_frame_gau
        
        delta_frame = cv2.absdiff(first_frame, gray_frame_gau)

        thresh_frame = cv2.threshold(delta_frame, 60, 255, 
                                    cv2.THRESH_BINARY) [1]
        dil_frame = cv2.dilate(thresh_frame, None, iterations=2)

        contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for contour in contours:
            if cv2.contourArea(contour) < 5000:
                continue
            
            x, y, w, h = cv2.boundingRect(contour)
            rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3)

            if rectangle.any():
                status = 1
                cv2.imwrite(f"images/image{count}.png",frame)
                count += 1
                all_images = glob.glob("images/*.png")
                index = int(len(all_images)/2)
                object_image = all_images[index]
        status_list.append(status)
        status_list = status_list[-2:]
        #cv2.imshow("Video", frame)
        streamlit_image.image(frame)

        if status_list[0] == 1 and status_list[1] == 0:
            #email_thread = Thread(target=send_email, args = (object_image, ))
            #email_thread.daemon = True
            #email_thread.start()
            print("Email SENT")
            sl.image(object_image)
            email_limit += 1

        if email_limit>3:
            break

    print("SESSION ENDED....")
    clear_folder()
    camera.release()
