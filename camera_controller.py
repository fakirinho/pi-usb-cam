from pygame import camera, image, init as pygame_init, quit as pygame_quit

class CameraController:
    def __init__(self, device_name='/dev/video0', width=640, height=480):
        pygame_init()
        camera.init()

        self.device = camera.Camera(device_name, (width, height))
        self.device.start()

    def capture_image(self, filename):
        captured_image = self.device.get_image()
        image.save(captured_image, filename)

    def cleanup(self):
        camera.quit()
        pygame_quit()
