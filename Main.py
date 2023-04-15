from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.toolbar import MDToolbar
from kivy.uix.screenmanager import Screen, ScreenManager


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("bbar.kv")


class Demo(Screen):
    def callback1(self):
        print("Left Icon Pressed!")

    def callback2(self):
        print("Right Icon Pressed!")


if __name__ == "__main__":

    class Test(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "BlueGray"
            return Builder.load_file("bbar.kv")

    Test().run()
