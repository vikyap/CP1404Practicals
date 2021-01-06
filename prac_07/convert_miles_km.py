from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty


class ConvertMilesKm(App):
    message = StringProperty()

    def build(self):
        self.title = "Convert miles to km"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_convert(self):
        result = self.handle_invalid_inputs() * 1.609344
        self.message = str(result)

    def handle_increment(self, change):
        self.root.ids.input_number = self.handle_invalid_inputs() + change

    def handle_invalid_inputs(self):
        try:
            miles = float(input(self.root.ids.input_number.text))
            return miles
        except ValueError:
            return 0


ConvertMilesKm().run()
