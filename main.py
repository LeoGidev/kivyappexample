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
        search_input = TextInput(hint_text="Buscar...", size_hint_x=0.8)
        search_button = Button(text="Buscar", size_hint_x=0.2)
        top_bar.add_widget(search_input)
        top_bar.add_widget(search_button)

        # Contenedor de imágenes
        scroll_view = ScrollView(size_hint_y=0.9)
        image_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        image_layout.bind(minimum_height=image_layout.setter('height'))

        # Cargar imágenes y sus descripciones