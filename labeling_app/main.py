from pathlib import Path

import tkinter as tk
from tkinter import filedialog

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image

from labeling_app.screen_names import ScreenNames


class AltViewButtons(BoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, orientation="vertical")
        self.default_color = (0.8, 0.8, 0.8, 1.0)
        self.active_color = (1.0, 0.0, 0.0, 1.0)

        lbl = Label(text="Select Leaf View")
        self.add_widget(lbl)

        self.dorsal_btn = Button(text="Dorsal", background_color=self.default_color)
        self.dorsal_btn.bind(on_release=lambda x: self.switch("dorsal"))
        self.ventral_btn = Button(text="Ventral", background_color=self.default_color)
        self.ventral_btn.bind(on_release=lambda x: self.switch("ventral"))

        self.selected_view = ""

        self.add_widget(self.dorsal_btn)
        self.add_widget(self.ventral_btn)

    def switch(self, view):
        if view not in ["dorsal", "ventral"]:
            print("Invalid option")
            return

        self.selected_view = view
        print(f"Current view now set to: {self.selected_view}")

        if self.selected_view == "dorsal":
            self.dorsal_btn.background_color = self.active_color
            self.ventral_btn.background_color = self.default_color
        elif self.selected_view == "ventral":
            self.ventral_btn.background_color = self.active_color
            self.dorsal_btn.background_color = self.default_color


class LabelingScreen(Screen):
    def __init__(
        self,
    ):
        super().__init__(name=ScreenNames.LABELING)

        self.img_idx = 0
        self.image_paths = []

        FONT_SIZE = 32
        page = BoxLayout(padding=10, orientation="vertical")

        # Select path button
        select_path_btn = Button(
            text="Select Image Folder",
            color="green",
            font_size=FONT_SIZE,
            size_hint=(1, 0.1),
        )
        select_path_btn.bind(on_press=self.get_image_directory)
        page.add_widget(select_path_btn)

        # Arrow Keys
        arrow_box = BoxLayout(
            padding=10,
            orientation="horizontal",
            size_hint=(1, 0.05),
        )

        # left
        left_btn = Button(text="<-", color="white", font_size=FONT_SIZE)
        left_btn.bind(on_press=self.goto_prev_image)
        arrow_box.add_widget(left_btn)

        # right
        right_btn = Button(text="->", color="white", font_size=FONT_SIZE)
        right_btn.bind(on_press=self.goto_next_image)
        arrow_box.add_widget(right_btn)

        page.add_widget(arrow_box)

        # Image
        self.image = Image(source=None, size_hint=(1, 0.7))
        page.add_widget(self.image)

        # View Buttons
        view_btns = AltViewButtons(size_hint=(1, 0.1))
        page.add_widget(view_btns)

        # Go to home page
        go_home_btn = Button(
            text="Home", color="blue", font_size=FONT_SIZE, size_hint=(1, 0.05)
        )
        go_home_btn.bind(on_press=self.goto_home_screen)
        page.add_widget(go_home_btn)

        self.add_widget(page)

    def goto_prev_image(self, instance):
        if not self.image_paths:
            return
        self.img_idx = (
            len(self.image_paths) - 1 if self.img_idx == 0 else self.img_idx - 1
        )
        self.update_image()

    def goto_next_image(self, instance):
        if not self.image_paths:
            return
        self.img_idx = (self.img_idx + 1) % len(self.image_paths)
        self.update_image()

    def update_image(self):
        if not self.image_paths:
            return
        self.image.source = str(self.image_paths[self.img_idx])

    def get_image_directory(self, instance):
        acceptable_image_extentions = [".png", ".jpg"]
        self.image_paths = []
        self.img_idx = 0

        image_dir = Path(filedialog.askdirectory())
        for root, dirs, files in image_dir.walk():
            for f in files:
                path = root / f
                if path.suffix.lower() in acceptable_image_extentions:
                    self.image_paths.append(path)

        self.update_image()

    def goto_home_screen(self, instance):
        self.manager.transition.direction = "right"
        self.manager.current = ScreenNames.HOME


class HomeScreen(Screen):
    def __init__(self):
        super().__init__(name=ScreenNames.HOME)
        FONT_SIZE = 32
        page = BoxLayout(padding=10, orientation="vertical")

        # Begin Trip
        goto_labeling_btn = Button(
            text="Start Labeling", color="green", font_size=FONT_SIZE
        )
        goto_labeling_btn.bind(on_press=self.goto_labeling_screen)
        page.add_widget(goto_labeling_btn)

        self.add_widget(page)

    def goto_labeling_screen(self, instance):
        self.manager.transition.direction = "left"
        self.manager.current = ScreenNames.LABELING


class LeafLabelingApp(App):
    def __init__(self):
        super().__init__()

    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen())
        sm.add_widget(LabelingScreen())
        return sm


if __name__ == "__main__":
    app = LeafLabelingApp()
    app.run()
