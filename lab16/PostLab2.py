from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

class TextInputApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.input_field = TextInput(hint_text="Type something here...", multiline=False, font_size=20)
        layout.add_widget(self.input_field)

        button = Button(text="Show Text", font_size=24)
        button.bind(on_press=self.show_text)
        layout.add_widget(button)

        self.label = Label(text="", font_size=24)
        layout.add_widget(self.label)

        return layout

    def show_text(self, instance):
        user_text = self.input_field.text
        self.label.text = f"You typed: {user_text}"

if __name__ == "__main__":
    TextInputApp().run()