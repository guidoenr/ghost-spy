import abc
import pyautogui
import cv2
import platform
import socket
import json

from captures import cpath


class Module(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def run(self, save_path_name):
        pass


class Screenshot(Module):

    def run(self, save_path_name):
        screenshot = pyautogui.screenshot()
        screenshot.save(cpath.generate_day_folder() + '/screenshot-' + save_path_name + '.jpg')


class WebcamSnap(Module):

    def run(self, save_path_name):
        cam_id = self.search_camera_id()
        if cam_id == -1:
            pass
        else:
            webcam = cv2.VideoCapture(cam_id)
            check, frame = webcam.read()
            cv2.imwrite(cpath.generate_day_folder() + '/webcam_snap-' + save_path_name + '.jpg', img=frame)
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

class SystemInfo(Module):

    def run(self, save_path_name):
        uname = platform.uname()
        hostname = socket.gethostname()

        data = {
            'System': uname.system,
            'Node name': uname.node,
            'Version': uname.version,
            'Machine': uname.machine,
            'Hostname': hostname,
            'Ip Address': socket.gethostbyname(hostname)
        }
        path = cpath.generate_day_folder() + '/system_info-' + save_path_name + '.json'
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)


if __name__ == '__main__':
    screenshot = Screenshot()
    systeminfo = SystemInfo()

    screenshot.run('sc')
    systeminfo.run('sy')

