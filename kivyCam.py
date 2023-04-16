"""
Camera Example
==============

This example demonstrates a simple use of the camera. It shows a window with
a buttoned labelled 'play' to turn the camera on and off. Note that
not finding a camera, perhaps because gstreamer is not installed, will
throw an exception during the kv language processing.

"""
# Uncomment these lines to see all the messages
# from kivy.logger import Logger
# import logging
# Logger.setLevel(logging.TRACE)
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.core.image import Image as CoreImage
from kivy.uix.camera import Camera
import time
import io
import infoFromImage as ifi
import os


Builder.load_string(
    """
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (1280, 1280)
        play: False
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
    Button:
        text: 'swap'
        size_hint_y: None
        height: '48dp'
        on_press: root.swap()
"""
)


class CameraClick(BoxLayout):
    def capture(self):
        camera = self.ids["camera"]
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("./data/temp.png".format(timestr))
        print("Captured")
        with open("./data/temp.png", "rb") as image_data:
            theData = ifi.sciNameFromImage(image_data)
        if theData == "404":
            return
        os.rename("./data/temp.png", f"./data/{theData}.png")

    def swap(self):
        self.text = "hai"
        print("hai")


class TestCamera(App):
    def build(self):
        return CameraClick()


TestCamera().run()
