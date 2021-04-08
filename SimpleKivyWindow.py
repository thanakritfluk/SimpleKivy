from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MyBoxLayout(BoxLayout):

    def calculate(self):
        input_weight = self.ids["weight_input"].text
        try:
            cup_per_day = float(input_weight)*0.033
            self.ids["result"].text = "You should drinking {:.3f} litres".format(cup_per_day)
        except ValueError:
            self.ids["result"].text = "Please input the number"


class SimpleKivyWindow(App):

    def build(self):
        return MyBoxLayout()


if __name__ == '__main__':
    SimpleKivyWindow().run()
