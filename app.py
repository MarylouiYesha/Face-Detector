import PySimpleGUI as sg
import cv2

layout=[
    [sg. Image(key = '-IMAGE')],
    [sg. Text ('People in picture:0', key = '-TEXT', expand_x =True, justification='c')]
]

window = sg.Window('Face Detector', layout)

video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    _, frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
    gray,
        scaleFactor = 1.3,
        minNeighbors = 7,
        minSize =(30,30))
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    imgbytes = cv2.imencode('.png', frame) [1].tobytes()
    window['-IMAGE'].update(data=imgbytes)
    
    window ['-TEXT-'].update(f'People in picture: {len(faces)}')

window.closet()