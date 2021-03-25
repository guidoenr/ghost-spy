import abc
import pyautogui
import cv2
import datetime
from captures import cpath


class Module(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def run(self, save_path_name):
        pass


class Screenshot(Module):

    def run(self, save_path_name):
        screenshot = pyautogui.screenshot()
        screenshot.save(cpath.route + 'screenshot-' + save_path_name + '.jpg')


class WebcamSnap(Module):

    def run(self, save_path_name):
        id = self.search_camera_id()
        if id == -1:
            pass
        else:
            webcam = cv2.VideoCapture(id)
            check, frame = webcam.read()
            cv2.imwrite(cpath.route + 'webcam_snap-' + save_path_name + '.jpg', img=frame)
            webcam.release()

    def search_camera_id(self):
        id = 0
        webcam = cv2.VideoCapture(id)
        for i in range(0, 10):
            if not webcam.isOpened():
                id +=1
                webcam = cv2.VideoCapture(id)
            else:
                return id
        return -1


if __name__ == '__main__':
    screenShot = Screenshot()
    screenShot.run('xdxd')
