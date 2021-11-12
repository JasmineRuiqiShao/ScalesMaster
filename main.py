# This app decides the type of scale the musician is going to practise
import random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image

key_signatures = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'Ab', 'Eb', 'Bb', 'F']
timbre = ['Staccato', 'Legato']
tonality = ['Major','Minor','Chromatic', 'Blues']
dynamics = ['Forte', 'Piano', 'Crescendo', 'Decrescendo']


class PracticeMachine(GridLayout):
    def __init__(self, **kwargs):
        super(PracticeMachine, self).__init__(**kwargs)

        # Set columns
        self.cols = 1
        self.top_grid = GridLayout()
        self.top_grid.cols = 3

        # Add Instrument input box
        self.top_grid.add_widget(Label(text="Instrument:", font_size=80))
        self.instrument = TextInput(multiline=False, font_size=80)
        self.top_grid.add_widget(self.instrument)

        self.add_widget(self.top_grid)

        # Create a Submit Button
        self.submit = Button(text="Let's Practise!", font_size=80)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        instrument = self.instrument.text
        key = random.choice(key_signatures)
        tone = random.choice(tonality)
        loudness = random.choice(dynamics)
        phrasing = random.choice(timbre)
        notes = random.randint(1, 8)
        self.add_widget(Image(source='Bach.jpeg'))
        self.add_widget(Label(
            text=f'You are going to practise: {instrument} '
                 f'\n key: {key} '
                 f'\n tonality: {tone}'
                 f'\n with {notes} notes {phrasing} '
                 f'\n dynamics: {loudness}.'))
        self.instrument.text = ""


class ScalesMaster(App):
    def build(self):
        return PracticeMachine()


if __name__ == '__main__':
    ScalesMaster().run()
