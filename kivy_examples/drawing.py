import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line

class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:
            Color(0,0,1,1, mode='rgba')
            Line(points=(20, 30, 400, 500, 60, 500))
            Color(1, 0, 1, .75, mode='rgba')
            self.rect = Rectangle(pos=(0,0), size=(50, 50))

    def on_touch_down(self, touch):
        self.rect.pos = touch.pos
        print("Mouse down", touch)

    def on_touch_move(self, touch):
        self.rect.pos = touch.pos
        print("Mouse move", touch)



class MyApp(App):
    def build(self):
        return Touch()

if __name__ == "__main__":
    MyApp().run()