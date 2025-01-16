from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from PIL import Image as PILImage
import os


IMAGE_FOLDER = "C:\\Users\\Westnet\\Desktop\\imagenes elementos"

class MainApp(App):
    def build(self):
        self.title = "Kivy Mobile App"

        # Layout principal
        root = BoxLayout(orientation="vertical")

        # Barra de tareas
        top_bar = BoxLayout(size_hint_y=0.1, padding=10, spacing=10, background_color=[0.9, 0.3, 0.5, 1])
        