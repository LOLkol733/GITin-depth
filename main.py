from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class MyCrid(App):

    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=5)
        self.lb = Label(text='None', font_size=50)
        btn1 = Button(text='list', font_size=50, size=(200, 100), size_hint=(None, None))
        btn2 = Button(text='dict', font_size=50, size_hint=(.5, 1))
        btn3 = Button(text='str', font_size=50)
        btn4 = Button(text='number', font_size=50, on_press=self.lable_batton)
        layout.add_widget(self.lb)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        return layout
        # background_color=[1, 0, 0, 1]) 1- red, 0-green, 0-blu, 1-прозрачность
        # return Button(text='Button', font_size=50, background_color=[0, 1, 0, 1], background_normal='',
        #               on_press=self.btn_pressGreen)

    # def btn_pressGreen(self, instanse):
    #     """функция для изменения цвета кнопки"""
    #     instanse.text = "Button press"
    def lable_batton(self, instanse):
        instanse.text = 'Cool'
        self.lb.text = 'You, very Cool!'




if __name__ == '__main__':
    MyCrid().run()
