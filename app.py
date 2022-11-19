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

window.closet()