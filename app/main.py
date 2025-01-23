from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.camera import Camera
from kivy.uix.label import Label
from kivy.uix. textinput import TextInput
from kivy.lang import Builder

from app.screen_names import ScreenNames
from app.tools import get_gps_location
from app.elements.simple_inputs import LatLongInputBox, ElevationBox, SiteIDBox, DateBox

class TestCameraScreen(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        page = BoxLayout(padding=0, orientation="vertical")
        
        self.camera = Camera(play=True, size_hint=(1, 1), allow_stretch=True, keep_ratio=True)
        page.add_widget(self.camera)
        
        capture_btn = Button(text="Capture", height='48dp', size_hint_y=None)
        capture_btn.bind(on_press=self.capture_image)
        page.add_widget(capture_btn)
        
        self.add_widget(page)
        
    def capture_image(self, instance):
        #timestr = time.strftime("%Y%m%d_%H%M%S")
        #camera.export_to_png("IMG_{}.png".format(timestr))
        self.camera.export_to_png("IMG_test.png")
        print("Captured")

class BeginTripScreen(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        FONT_SIZE = 32
        page = BoxLayout(padding=10, orientation="vertical")

        # LatLong Input
        latlong_box = LatLongInputBox()
        page.add_widget(latlong_box)
        
        # Elevation Input
        elevation_box = ElevationBox()
        page.add_widget(elevation_box)
        
        # Site ID Input
        site_id_box = SiteIDBox()
        page.add_widget(site_id_box)
        
        # Date Input
        date_box = DateBox()
        page.add_widget(date_box)
        
        def test_print(instance):
            print(latlong_box.get_lat_long())
            print(elevation_box.get_elevation())
        
        # Test btn
        text_btn = Button(text="Print Data")
        text_btn.bind(on_press=test_print)
        page.add_widget(text_btn)

        # Go to home page
        begin_trip_btn = Button(text='Home', color="green", font_size=FONT_SIZE)
        begin_trip_btn.bind(on_press=self.goto_home_screen)
        page.add_widget(begin_trip_btn)
        
        self.add_widget(page)
        
    def goto_home_screen(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = ScreenNames.HOME

class HomeScreen(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        FONT_SIZE = 32
        page = BoxLayout(padding=10, orientation="vertical")

        # Begin Trip
        begin_trip_btn = Button(text='Start Trip', color="green", font_size=FONT_SIZE)
        begin_trip_btn.bind(on_press=self.goto_begin_trip_screen)
        page.add_widget(begin_trip_btn)
        
        # View Trips
        view_trips_btn = Button(text="View Trips", color="blue", font_size=FONT_SIZE)
        view_trips_btn.bind(on_press=self.goto_view_trips_screen)
        page.add_widget(view_trips_btn)
        
        self.add_widget(page)
    
    def goto_begin_trip_screen(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = ScreenNames.BEGIN_TRIP
    
    def goto_view_trips_screen(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = "test_camera_screen"

class LeafDataCollectionApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name=ScreenNames.HOME))
        sm.add_widget(BeginTripScreen(name=ScreenNames.BEGIN_TRIP))
        sm.add_widget(TestCameraScreen(name="test_camera_screen"))
        return sm


if __name__ == '__main__':
    app = LeafDataCollectionApp()
    app.run()

""" import kivy
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]

class HBoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(padding=10, orientation="vertical")
        colors = [red, green, blue, purple]

        for i in range(5):
            btn = Button(text="Button #%s" % (i+1),
                         background_color=random.choice(colors)
                         )

            layout.add_widget(btn)
        return layout

if __name__ == "__main__":
    app = HBoxLayoutExample()
    app.run() """

""" 
    from kivy.app import App
    from kivy.uix.image import Image
    
    class MainApp(App):
    def build(self):
        img = Image(source='assets/leaf.jpg',
                    size_hint=(1, .5),
                    pos_hint={'center_x':.5, 'center_y':.5})

        return img """