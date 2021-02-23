from picamera import PiCamera
from time import sleep
from datetime import datetime
from gpiozero import Button

button = Button(25)
camera = PiCamera()

camera.start_preview()
imageId = 1
while True:
    try:
        button.wait_for_press()
        sleep(2);
        camera.annotate_text_size = 50
        camera.annotate_text = datetime.now().strftime('%A %d %b %Y %H:%M:%S')
        camera.capture('/home/pi/Desktop/image%03d.jpg' % imageId)
        imageId += 1
    except KeyboardInterrupt:
        camera.stop_preview()
        break