import PySimpleGUI as sg
import cv2

layout=[
    [sg. Image(key = '-IMAGE')],
    [sg. Text ('People in picture:0', key = '-TEXT', expand_x =True, justification='c')]
]