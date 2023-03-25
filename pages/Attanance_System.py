import streamlit as st
import os
import cv2
import pickle
import face_recognition
import numpy as np
import mediapipe as mp
from imutils.video import VideoStream
import pickle

st.title("Attanance_System!!!")

image_list =  st.image([])

encoding_list = []

mp_draw = mp.solutions.drawing_utils
mp_styles = mp.solutions.drawing_styles
my_face = mp.solutions.face_detection
pose = my_face.FaceDetection()

# to load all images


# get the path/directory
folder_dir = r"E:\vs code projects\Attanance_system_face_detection\employ_images"
for images in os.listdir(folder_dir): 
    # check if the image ends with png or jpg or jpeg
    if (images.endswith(".png") or images.endswith(".jpg") or images.endswith(".jpeg") or images.endswith(".jfif") ):
        # display
        known_image1 = face_recognition.load_image_file("employ_images" + "/" + images)
        biden_encoding1 = face_recognition.face_encodings(known_image1)[0]
        encoding_list.append(biden_encoding1)
        
    
names_list = pickle.load(open("employ_name_list.pickle","rb"))

face_location = []
face_encoding = []
face_names = []
s = True

video = VideoStream(src=0).start()

while True:
    
    frame = video.read()
    
    # to create bounding box in image  
    results = pose.process(frame)
    
    if results.detections:
        for detection in results.detections:
            mp_draw.draw_detection(frame,detection)
    
    
    # this is for compare known image and unknown image 
    name = ""
    if s: 
        
        unknown_location = face_recognition.face_locations(frame)
        unknown_encoding = face_recognition.face_encodings(frame,unknown_location)
        face_names = []
        
        for face in unknown_encoding:
            results = face_recognition.compare_faces(encoding_list,face)
            
            face_distance = face_recognition.face_distance(encoding_list,face)
            best_match = np.argmin(face_distance)
            
            if results[best_match]:
                name = names_list[best_match]
                
                
        
        cv2.putText(frame,name,(100,300),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),3,cv2.LINE_AA)
        cv2.putText(frame,"{} entered!!!".format(name),(100,350),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),3,cv2.LINE_AA)          

    

    image_list.image(frame)

            

