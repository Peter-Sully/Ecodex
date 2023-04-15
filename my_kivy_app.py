from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MyKivyApp(App):
    def build(self):
        # Set the window size
        Window.size = (800, 600)
        # Set the window title
        Window.title = "My Kivy App"

        # Load the KV file
        return Builder.load_file("my_kivy_app.kv")


if __name__ == "__main__":
    MyKivyApp().run()
