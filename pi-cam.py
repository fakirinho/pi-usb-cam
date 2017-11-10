from camera_controller import CameraController
import ftplib
import datetime
import time
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("device", help="name of device used for taking photos, defaults to '/dev/video0'")
parser.add_argument("width", metavar="int", type=int, help="width of the image in pixels, defaults to 640")
parser.add_argument("height", metavar="int", type=int, help="width of the image in pixels, defaults to 480")
parser.add_argument("hostname", help="FTP hostname")
parser.add_argument("username", help="username")
parser.add_argument("password", help="password")
args = parser.parse_args()


cam_controller = CameraController(args.device, args.width, args.height)
cam_controller.capture_image("image.jpg")

session = ftplib.FTP(args.hostname, args.username, args.password)
image_to_be_uploaded = open("image.jpg", 'r')
timestamp = time.time()
filename = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d_%H:%M:%S') + '.jpg'
session.storbinary('STOR ' + filename, image_to_be_uploaded)

image_to_be_uploaded.close()
os.remove("image.jpg")
session.close()

cam_controller.cleanup()
