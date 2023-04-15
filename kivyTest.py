from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Ellipse, Color

class DrawingCanvas(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            # Draw a rectangle
            Color(1, 0, 0)  # Set color to red
            Rectangle(pos=(touch.x, touch.y), size=(100, 50))  # Set rectangle position and size

    def on_touch_up(self, touch):
        with self.canvas:
            # Draw a circle
            Color(0, 1, 0)  # Set color to green
            Ellipse(pos=(touch.x, touch.y), size=(50, 50))  # Set circle position and size

class DrawingApp(App):
    def build(self):
        return DrawingCanvas()

if __name__ == '__main__':
    DrawingApp().run()
