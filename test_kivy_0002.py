from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


### clase que contiene todos tus elementos

class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid,self).__init__(**kwargs)
        self.cols = 4
        self.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline =False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Last Name: "))
        self.lastName = TextInput(multiline =False)
        self.add_widget(self.lastName)

        self.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline =False)
        self.add_widget(self.email)





class MyApp(App):

    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()