from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp


class MyKivyApp(MDApp):
    data = {
        "Python": ["language-php", "on_press", lambda x: print("pressed PHP")],
        "language-cpp": "C++",
        "language-java": "Java",
    }

    def callback(self, instance):
        print("hai")
        self.root.ids.my_label.text = "ding!"

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        # # Set the window size
        # Window.size = (800, 600)
        # Set the window title
        Window.title = "My Kivy App"

        # Load the KV file
        return Builder.load_file("sd.kv")


if __name__ == "__main__":
    MyKivyApp().run()
