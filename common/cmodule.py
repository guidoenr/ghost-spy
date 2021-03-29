import abc
import pyautogui
import cv2
import platform
import socket
import json
import geocoder
from geopy.geocoders import Nominatim
from captures import cpath


class Module(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def run(self, save_path_name):
        pass


class Screenshot(Module):

    def run(self, save_path_name):
        pass
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
        cam_id = 0
        webcam = cv2.VideoCapture(cam_id)
        for i in range(0, 10):
            if not webcam.isOpened():
                cam_id += 1
                webcam = cv2.VideoCapture(cam_id)
            else:
                return cam_id
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


class GeoLocator(Module):

    def run(self, save_path_name):
        ip = geocoder.ip('me')
        coordinates = ip.latlng
        locator = Nominatim(user_agent='geocoder')
        location = locator.reverse(coordinates)
        path = cpath.generate_day_folder() + '/geolocation-' + save_path_name + '.json'
        data = location.raw
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)


if __name__ == '__main__':
    g = GeoLocator()
    g.run('s')
