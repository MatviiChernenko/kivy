# напиши модуль для реалізації секундоміра
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import BooleanProperty

class Seconds(Label):
    done = BooleanProperty(False)
   
    def __init__(self, total, **kwargs):
        self.total = total
        self.current = 0
        self.done = False
        my_text = f"Минуло секунд:{self.current}"
        super().__init__(text = my_text)

    def restart(self, total, **kwargs):
        self.total = total
        self.current = 0
        self.done = False
        self.text = f"Минуло секунд:{self.current}"
        self.start()

    def start(self):
        Clock.schedule_interval(self.change,1)

    def change(self, dt):
        self.current += 1
        self.text = f"Минуло секунд:{self.current}"
        if self.current >= self.total:
            self.done = True
            return False