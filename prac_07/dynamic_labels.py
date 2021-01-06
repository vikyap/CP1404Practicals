from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabels(App):
    message = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.namelist = ["Apple", "Orange", "Watermelon", "Pear"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        return self.root

    def create_labels(self):
        for name in self.namelist:
            temp_label = Label(text=name, id=name)
            self.root.ids.main_box.add_widget(temp_label)
            self.message = name


