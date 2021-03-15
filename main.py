import common.get_data as gd
import os
import pyautogui, datetime, os, cv2

def take_screenshot(savepath):
    screenshot = pyautogui.screenshot()
    screenshot.save(savepath + str(datetime.datetime.now()) + '.jpg')

def get_current_path():
    return os.getcwd()

def get_log_path():
    return get_current_path() + '/log/'

if __name__ == '__main__':
    take_screenshot(get_log_path())
    webcam = cv2.VideoCapture(1)
    check, frame = webcam.read()
    cv2.imwrite(filename=get_log_path() + 'asd.jpg',img=frame)
    webcam.release()