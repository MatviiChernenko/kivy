# напиши модуль для підрахунку кількості присідань
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import BooleanProperty

class Sits(Label):
    done = BooleanProperty(False)

    def __init__(self, total, **kwargs):
        self.total = total
        self.current = 0
        self.done = False
        my_text = f"залишилось присідань{self.total} "
        super().__init__(text=my_text,**kwargs)

    def restart(self, total, **kwargs):
        self.total = total
        self.current = 0
        self.done = False
        self.text = f"залишилось присідань{self.total} "
        self.start()


    def start(self):
        Clock.schedule_interval(self.next,1)

    def next(self, *args):
        self.current += 1
        tmp = self.total - self.current
        self.text = f"залишилось присідань{tmp}"
        #self.text = my_text
        if tmp <= 0:
            self.done = True
            return False