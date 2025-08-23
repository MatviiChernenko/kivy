# напиши модуль для роботи з анімацією
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.properties import NumericProperty,BooleanProperty

class Runner(BoxLayout):
    value = NumericProperty(0)
    finished = BooleanProperty(False)

    def __init__(self,total,**kwargs):
        super().__init__(**kwargs)
        self.total = total
        self.animation = (Animation(pos_hint={"top":0.1},duration=0.75)+
                          Animation(pos_hint={"top":1},duration=0.75))
        self.animation.repeat = True
        self.animation.on_progress = self.next
        self.button = Button(size_hint= (1,0.1),pos_hint={"top":1},background_color=(255/255,45/255,166/255,1))
        self.add_widget(self.button)
    def start(self):
        self.value = 0
        self.finished = False
        self.animation.repeat = True
        self.animation.start(self.button)

    def next(self, widget, step):
        if step == 1:
            self.value += 1
            if self.value >= self.total:
                self.animation.repeat = False
                self.finished = True