from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
import re

Window.size = (500, 700)

Builder.load_file('kalk.kv')


class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'

    def button_press(self, button):
        prior = self.ids.calc_input.text
        if "Error" in prior:
            prior = '0'
        if prior == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}{sign}'

    def dot(self):
        prior = self.ids.calc_input.text
        flag = True
        for i in prior[::-1]:
            if i == '.':
                flag = False
            if i in "+-/*":
                break
        if flag:
            self.ids.calc_input.text = f'{prior}.'

    def remove(self):
        prior = self.ids.calc_input.text
        if len(prior) != 1:
            prior = prior[:-1]
            self.ids.calc_input.text = prior
        else:
            self.ids.calc_input.text = "0"

    def pos_neg(self):
        prior = self.ids.calc_input.text
        if '-' in prior:
            self.ids.calc_input.text = f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{prior}'

    def equals(self):
        prior = self.ids.calc_input.text
        try:
            answer = eval(prior)
            self.ids.calc_input.text = str(answer)[:10]
        except:
            self.ids.calc_input.text = 'Error'


class CalculatorApp(App):
    def build(self):
        Window.clearcolor = (0.3, 0.3, 0.3, 1)
        return MyLayout()


if __name__ == '__main__':
    CalculatorApp().run()
