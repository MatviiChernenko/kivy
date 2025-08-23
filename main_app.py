# напиши тут свою програму
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
import instructions
from ruffier import txt_nodata
import seconds 
import sits
import runner
from ruffier import *
from kivy.core.window import Window
Window.clearcolor = (255/44,45/66,166/75,1)
WITH, HEIGHT = 1080 // 3.2,1920 // 3.2

def check_int(value):
    try:
        return int(value)
    except:
        return False

class MainWindow(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        text = Label(text=instructions.txt_instruction, text_size = (WITH,HEIGHT//1.8))

        name_label = Label(text="Введіть ім'я")
        age_label = Label(text="Введіть вік")
        self.name_user = TextInput(multiline =False )
        self.age = TextInput(multiline =False )
        self.button = Button(text="Продовжити",size_hint = (0.5,0.1),pos_hint={"center_x":0.5})
        self.button.on_press = self.next

        layout_name = BoxLayout(size_hint = (1,0.15))
        layout_age = BoxLayout(size_hint = (1,0.15))
        layout_name.add_widget(name_label)
        layout_name.add_widget(self.name_user)
        layout_age.add_widget(age_label)
        layout_age.add_widget(self.age)

        main_layout = BoxLayout(orientation = "vertical",spacing = 10, padding = 10)
        main_layout.add_widget(text)
        main_layout.add_widget(layout_name)
        main_layout.add_widget(layout_age)
        main_layout.add_widget(self.button)
        self.add_widget(main_layout)



    def next(self):
        age_result = self.age.text
        self.manager.current = "first_pulse"
        if age_result <= "6":
            self.manager.current = "else_result"


class InputPulseFirst(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        text = Label(text=instructions.txt_test1)
        self.timer = seconds.Seconds(5)
        self.timer.bind(done = self.sec_finish)
        self.next_screen = False

        result_label = Label(text="Введіть результат")
        self.first_result = TextInput(multiline =False )
        self.first_result.set_disabled(True)
        
        self.button = Button(text="Почати")
        self.button.on_press = self.next

        layout_result = BoxLayout()
        layout_result.add_widget(result_label)
        layout_result.add_widget(self.first_result)


        main_layout = BoxLayout(orientation = "vertical")
        main_layout.add_widget(text)
        main_layout.add_widget(self.timer)
        main_layout.add_widget(layout_result)
        main_layout.add_widget(self.button)
        self.add_widget(main_layout)


    def next(self):
        if self.next_screen == False:
            self.button.set_disabled(True)
            self.timer.start()
        else:
            global first_result
            first_result = check_int(self.first_result.text)
            if first_result == False or first_result < 0:
                self.first_result.text = "0"
            else:
                self.manager.current = "sits"


    def sec_finish(self,*arg):
        self.next_screen = True
        self.first_result.set_disabled(False)
        self.button.set_disabled(False)
        self.button.text = "Продовжити"

class SitsWindow(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        text = Label(text=instructions.txt_sits,text_size = (WITH,HEIGHT//1.8))
        self.runner = runner.Runner(5)
        self.runner.bind(finished= self.run_finished)
        self.sits = sits.Sits(5)
        self.next_screen = False


        self.button = Button(text="Почати")
        self.button.on_press = self.next

        f_v_layout = BoxLayout(orientation = "vertical")
        f_v_layout.add_widget(text)

        h_layout = BoxLayout()
        h_layout.add_widget(f_v_layout)
        h_layout.add_widget(self.runner)

        main_layout = BoxLayout(orientation = "vertical")
        main_layout.add_widget(h_layout)
        main_layout.add_widget(self.sits)
        #main_layout.add_widget(self.button1)
        main_layout.add_widget(self.button)
        self.add_widget(main_layout)

    def run_finished(self,*args):
        self.button.set_disabled(False)
        self.next_screen = True

    def next(self):
        if self.next_screen == False:
            self.button.set_disabled(True)
            self.runner.start()
            self.runner.bind(value= self.sits.next)
        else:
            self.manager.current = "second_pulse"

    def sec_finish(self,*arg):
        self.next_screen = True
        self.button.set_disabled(False)
        self.button.text = "Продовжити"

class InputPulseSecond(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        self.check_timer = 0

        text = Label(text=instructions.txt_test3,text_size = (WITH,HEIGHT//1.8))
        self.timer = seconds.Seconds(3)
        self.timer.bind(done=self.sec_finish)
        self.instruction = Label(text = "")

        second_result_label = Label(text="Результат:")
        third_result_label = Label(text="Результат після відпочинку:")
        self.second_result = TextInput(multiline =False )
        self.second_result.set_disabled(True)
        self.third_result = TextInput(multiline =False )
        self.third_result.set_disabled(True)
        self.button = Button(text="Почати")
        self.button.on_press = self.next

        layout_first_result = BoxLayout()
        layout_second_result = BoxLayout()
        layout_first_result.add_widget(second_result_label)
        layout_first_result.add_widget(self.second_result)
        layout_second_result.add_widget(third_result_label)
        layout_second_result.add_widget(self.third_result)

        main_layout = BoxLayout(orientation = "vertical",spacing=10)
        main_layout.add_widget(text)
        main_layout.add_widget(self.instruction)
        main_layout.add_widget(self.timer)
        main_layout.add_widget(layout_first_result)
        main_layout.add_widget(layout_second_result)
        main_layout.add_widget(self.button)

        self.add_widget(main_layout)

    def sec_finish(self,*arg):
        if self.timer.done ==True:
            if self.check_timer == 0:
                #self.next_screen = True
                self.second_result.set_disabled(False)
                self.check_timer = 1 
                self.instruction.text = "Відпочивайте!"
                self.timer.restart(5)
            elif self.check_timer == 1:
                self.check_timer = 2
                self.instruction.text = "Міряйте пульс!"
                self.timer.restart(3)
            elif self.check_timer == 2:
                self.third_result.set_disabled(False)
                self.button.set_disabled(False)
                self.instruction.text = "Випишіть результати пульсу!"
                self.button.text = "закінчити"
                self.next_screen = True


    def next(self):
        if self.next_screen == False:
            self.timer.start()
            self.instruction.text = "Міряйте пульс!"
            self.button.set_disabled(True)
        else:
            global second_result,third_result
            second_result = check_int(self.second_result.text)
            third_result = check_int(self.third_result.text)
            if second_result == False or second_result < 0:
                self.second_result.text = "0"
            elif third_result == False or third_result < 0:
                self.third_result.text = "0"
            else:
                self.manager.current = "result"

class Result(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.result = Label()
        self.on_enter = self.before
        self.add_widget(self.result)

    def before(self):
        self.result.text = f"{first_result} {second_result} {third_result}"

class Else_Result(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.result = Label()
        self.on_enter = self.before
        self.add_widget(self.result)

    def before(self):
        self.result.text = f"{txt_nodata}"



class Ruffier(App):
    def build (self):
        Window.size = (WITH,HEIGHT)
        sm = ScreenManager()
        sm.add_widget(MainWindow(name = "main"))
        sm.add_widget(InputPulseFirst(name = "first_pulse"))
        sm.add_widget(SitsWindow(name = "sits"))
        sm.add_widget(InputPulseSecond(name = "second_pulse"))
        sm.add_widget(Result(name = "result"))
        sm.add_widget(Else_Result(name = "else_result"))
        return sm
    
ruffier = Ruffier()
ruffier.run()