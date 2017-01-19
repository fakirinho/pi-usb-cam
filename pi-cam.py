import pygame.camera
import ftplib
import datetime
import time
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("hostname", help="FTP hostname")
parser.add_argument("username", help="username")
parser.add_argument("password", help="password")
args = parser.parse_args()

pygame.init()
pygame.camera.init()

cam = pygame.camera.Camera("/dev/video0", (640, 480))
cam.start()
cam.get_controls()
image = cam.get_image()
pygame.image.save(image, "image.jpg")

session = ftplib.FTP(args.hostname, args.username, args.password)
image_to_be_uploaded = open("image.jpg", 'r')
timestamp = time.time()
filename = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d_%H:%M:%S') + '.jpg'
session.storbinary('STOR ' + filename, image_to_be_uploaded)

image_to_be_uploaded.close()
os.remove("image.jpg")
session.close()
cam.stop()
pygame.quit()
