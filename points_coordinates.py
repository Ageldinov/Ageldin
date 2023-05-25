# import the required library
import PySimpleGUI as sg
import cv2
import numpy as np

# define a function to display the coordinates of
def coordinates(values, window, picture):
    StartY = values['-Y START IN-']
    EndY = values['-Y END IN-']
    StartX = values['-X START IN-']
    EndX = values['-X END IN-']
    points = []

    # of the points clicked on the image
    def click_event(event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            a = (float(EndX)-float(StartX))*(x/width)
            b = (float(EndY)-float(StartY)-(float(EndY)-float(StartY))*(y/height))
            points.append(f'({round(a, 2)},{round(b, 2)})')
            
            # put coordinates as text on the image
            cv2.putText(img, f'({round(a, 1)},{round(b, 1)})',(x,y),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
      
            # draw point on the image
            cv2.circle(img, (x,y), 3, (0,255,255), -1)
 
    # read the input image
    img = cv2.imread(str(picture))
    height, width = img.shape[:2]
    print (height, width)

    # create a window
    cv2.namedWindow('Point Coordinates')

    # bind the callback function to window
    cv2.setMouseCallback('Point Coordinates', click_event)

    # display the image
    while True:
        cv2.imshow('Point Coordinates',img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    # Находим текст вывода и выводим в него все данные и результат
    #text_elem = window['-RESULT 3-']
    sg.popup_ok('Вы выбрали:', *points, title='')

    cv2.destroyAllWindows()

