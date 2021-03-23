import pyautogui, os, datetime, cv2

webcam_id = 0

def take_screenshot():
    screen = pyautogui.screenshot()
    screen.save(os.getcwd() + '/log/' + str(datetime.datetime.now()) + '.jpg')

