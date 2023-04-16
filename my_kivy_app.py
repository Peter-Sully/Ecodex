from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp

layout = GridLayout(cols=3, spacing=90, size_hint_y=None)
# Make sure the height is such that there is something to scroll.
layout.bind(minimum_height=layout.setter("height"))
for i in range(100):
    btn = Button(text=str(i), size_hint_y=None, height=300)
    layout.add_widget(btn)
root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))

root.add_widget(layout)


# define screen
class CameraClick(Screen):
    def capture(self):
        camera = self.ids["camera"]
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("./data/temp.png".format(timestr))
        print("Captured")
        with open("./data/temp.png", "rb") as image_data:
            theData = ifi.sciNameFromImage(image_data)
        print(theData)


class PhotoScreen(Screen):
    layout = GridLayout(cols=3, spacing=90, size_hint_y=None)
    # Make sure the height is such that there is something to scroll.
    layout.bind(minimum_height=layout.setter("height"))
    for i in range(100):
        btn = Button(text=str(i), size_hint_y=None, height=300)
        layout.add_widget(btn)
    rt = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
    root.clear_widgets()
    root.add_widget()


class WindowManager(ScreenManager):
    pass


kv2 = Builder.load_file("swap.kv")
sm = ScreenManager()
sm.add_widget(CameraClick(name="camera"))
sm.add_widget(PhotoScreen(name="photos"))


class MyKivyApp(MDApp):
    # kv = Builder.load_file("sd.kv")
    data = {
        "Python": ["language-php", "on_press", lambda x: print("pressed PHP")],
        "language-cpp": "C++",
        "language-java": "Java",
    }

    def callback(self, instance):
        print("hai")
        # root.ids.my_label.text = "ding!"
        self.root.add_widget()
        print(self.root.ids.text)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        Window.title = "My Kivy App"
        return kv2


if __name__ == "__main__":
    MyKivyApp().run()
