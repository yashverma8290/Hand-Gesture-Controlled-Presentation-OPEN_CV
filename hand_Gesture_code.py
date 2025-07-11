import os
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
#vairables
width,height=960,500
folderPath="pictures"
#camera setup
cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

cap.set(3,width)
cap.set(4,height)

#Get the list of presentation images
pathImages=sorted(os.listdir(folderPath),key=len)
#print(pathImages)

#Variables
imgNumber=0
hs,ws=int(120*1),int(213*1)
gestureThreshold=200

buttonPressed=False
buttonCounter=0
buttonDelay=40


annotations=[[]]
annotationNumber=0
annotationStart=False


# Hand Detector
detector=HandDetector(detectionCon=0.8,maxHands=1)

while True:
    # Import images
    success,imgFrame=cap.read()
    imgFrame=cv2.flip(imgFrame,1)

    pathFullImages=os.path.join(folderPath,pathImages[imgNumber])
    imgCurrent=cv2.imread(pathFullImages)
    imgCurrent = cv2.resize(imgCurrent, (width, height))  # Resize slide to match webcam resolution

    hands,img=detector.findHands(imgFrame,flipType=1)
    actual_width=imgFrame.shape[1]
    cv2.line(imgFrame,(0,gestureThreshold),(actual_width,gestureThreshold),(0,255,0),4)

    if hands and buttonPressed==False:
        hand=hands[0]
        fingers=detector.fingersUp(hand)
        cx,cy = hand['center']
        lmList=hand['lmList']

        # Constrain values for easier drawing

        xVal=int(np.interp(lmList[8][0],[width//2,width],[0,width]))
        yVal=int(np.interp(lmList[8][1],[100,height-100],[0,height]))
        indexFinger = xVal,yVal

        if cy<=gestureThreshold:  # if hand is at the height of the face
            annotationStart = False
            # Gesture 1-left
            if fingers==[1,0,0,0,0]:
                annotationStart = False
                print('left')
                if imgNumber>0:
                    buttonPressed = True
                    annotations = [[]]
                    annotationNumber = 0
                    imgNumber-=1

            # Gesture 2-Right
            if fingers==[0,0,0,0,1]:
                annotationStart = False
                print('right')
                if imgNumber<len(pathImages)-1:
                    buttonPressed = True
                    annotations = [[]]
                    annotationNumber = 0
                    imgNumber+=1


     # Gesture 3-Show Pointer
        if fingers==[0,1,1,0,0]: # outside this loop as we dont wanted it to work only above green line instead we want it work everywhere
            cv2.circle(imgCurrent,indexFinger,5,(0,0,255),cv2.FILLED)
            annotationStart = False
    # Gesture 4-Draw Pointer
        if fingers == [0, 1, 0, 0,0]:  # outside this loop as we dont wanted it to work only above green line instead we want it work everywhere
            if  annotationStart is False:
                annotationStart = True
                annotationNumber +=1
                annotations.append([])
            cv2.circle(imgCurrent, indexFinger, 5, (0, 0, 255), cv2.FILLED)
            annotations[annotationNumber].append(indexFinger)
        else:
            annotationStart=False
 
    # Gesture 5-Erase
        if fingers== [0,1,1,1,0]:
           if annotations:
               if annotationNumber>=0:
                 annotations.pop(-1)
                 annotationNumber -=1
                 buttonPressed=True

    else:
        annotationStart = False
    # Buttion Pressed Itteration
    if buttonPressed:
        buttonCounter+=1
        if buttonCounter>buttonDelay:
            buttonCounter=0
            buttonPressed=False

    for i in range(len(annotations)):
        for j in range(len(annotations[i])):
            if j!=0:
               cv2.line(imgCurrent,annotations[i][j-1],annotations[i][j],(0,0,255),4)


    # Adding webcam image on the slides
    imgSmall=cv2.resize(imgFrame,(ws,hs)) # for web cam
    h,w,_=imgCurrent.shape   # for slides



    #for placing my video in the top right corner
    imgCurrent[0:hs,w-ws:w]=imgSmall

    cv2.imshow('frame',imgFrame)
    cv2.imshow('Slides',imgCurrent)


    key=cv2.waitKey(1)
    if key==ord('q'):
        break