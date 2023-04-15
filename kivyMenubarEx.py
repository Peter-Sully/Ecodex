from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivy.core.window import Window
  
# builder method
helper="""
Screen:

    name:'Main screen'
    BoxLayout:
        orientation:'vertical'
        MDTopAppBar:
            title:'EcoDex'
            left_action_items:[['menu',lambda x: app.navigation_draw()]]
            right_action_items:[['cog-box',lambda x: app.navigation_draw()]]
            elevation:2
            md_bg_color: 0,100/255, 0,1
    MDFloatingActionButton:
        icon: "camera"
        pos_hint: {"center_x": .8, "center_y": .1}
        md_bg_color: 0,100/255,0,1
"""
class Demo(MDApp):
  
    def build(self):
  
        screen=Builder.load_string(helper)
        return screen
      
    # lambda Function
    def navigation_draw(self):
        print("NavBar")
  
if __name__ == "__main__":
    Window.size = (450, 820)
    Demo().run()