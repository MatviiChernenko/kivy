from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(TestScreen(name="test"))
        sm.add_widget(TestScreen2(name="test2"))
        sm.add_widget(TestScreen3(name="test3"))
        sm.add_widget(TestScreen4(name="test4"))
        sm.add_widget(TestScreen5(name="test5"))        
        return sm

class TestScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        button = Button(text = "Нажмеш лох")
        button1 = Button(text = "Hello world!")
        button2 = Button(text = "Лохотрон!!!")
        button3 = Button(text = "Халява")
        button1.on_press = self.any_window
        button2.on_press = self.any_window1
        button3.on_press = self.any_window2
        self.count = ""
        button.on_press = self.test
        self.label1 = Label(text = "")
        layot = BoxLayout(orientation = "vertical", padding = 10, spacing=20)
        layot.add_widget(button)
        layot.add_widget(button1)
        layot.add_widget(button2)
        layot.add_widget(button3)
        layot.add_widget(self.label1)

        self.add_widget(layot)
    def test (self):
        self.count = "лох"
        self.label1.text = str(self.count)
        self.manager.current = "test3"
    def any_window(self):
        self.manager.current = "test2"
    def any_window1(self):
        self.manager.current = "test4"
    def any_window2(self):
        self.manager.current = "test5"

class TestScreen2(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        label = Label(text = "Big")
        button = Button( text = "back")
        layout = BoxLayout()
        button.on_press = self.back
        layout.add_widget(label)
        layout.add_widget(button)

        self.add_widget(layout)
    def back(self):
        self.manager.current = "test"

class TestScreen3(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        label = Label(text = "Лох")
        button = Button( text = "back")
        layout = BoxLayout()
        button.on_press = self.back
        layout.add_widget(label)
        layout.add_widget(button)

        self.add_widget(layout)
    def back(self):
        self.manager.current = "test"

class TestScreen4(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        label = Label(text = "-1000000 грн")
        button = Button( text = "back")
        layout = BoxLayout()
        button.on_press = self.back
        layout.add_widget(label)
        layout.add_widget(button)

        self.add_widget(layout)
    def back(self):
        self.manager.current = "test"

class TestScreen5(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        label = Label(text = "Халяви не буде")
        button = Button( text = "back")
        layout = BoxLayout()
        button.on_press = self.back
        layout.add_widget(label)
        layout.add_widget(button)

        self.add_widget(layout)
    def back(self):
        self.manager.current = "test"




app = MyApp()
app.run()