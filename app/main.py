from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.camera import Camera
from kivy.uix.label import Label
from kivy.uix. textinput import TextInput
from kivy.lang import Builder

from app.screen_names import ScreenNames
from app.tools import get_gps_location, load_data_store, get_running_app, transition_screen
from app.elements.simple_inputs import ImageHolder, LatLongInputBox, ElevationBox, SiteIDBox, DateBox, PlantNumberBox, ImageBox

class CameraScreen(Screen):
    def __init__(self):
        super().__init__(name=ScreenNames.CAMERA_SCREEN)
        
        page = BoxLayout(padding=0, orientation="vertical")
        
        page.add_widget(get_running_app().get_camera())
        
        capture_btn = Button(text="Capture", height='48dp', size_hint_y=None)
        capture_btn.bind(on_press=self.capture_image)
        page.add_widget(capture_btn)
        
        self.add_widget(page)
        
    def capture_image(self, instance):
        #timestr = time.strftime("%Y%m%d_%H%M%S")
        #camera.export_to_png("IMG_{}.png".format(timestr))
        app = get_running_app()
        image = app.get_camera().export_as_image()
        app.get_current_image_holder().set_image(image)
        
        transition_screen(self, app.get_camera_exit_screen())
        
class AddLeavesScreen(Screen):
    def __init__(self):
        super().__init__(name=ScreenNames.ADD_LEAVES)
        
        page = BoxLayout(padding=10, orientation="vertical")
        
        # TODO add plant number here
        
class AddPlantScreen(Screen):
    def __init__(self):
        super().__init__(name=ScreenNames.ADD_PLANT)
        
        page = BoxLayout(padding=10, orientation="vertical")
        
        # LatLong Input
        self.latlong_box = LatLongInputBox()
        page.add_widget(self.latlong_box)
        
        # Elevation Input
        self.elevation_box = ElevationBox()
        page.add_widget(self.elevation_box)
        
        # Plant Number
        self.plant_box = PlantNumberBox()
        page.add_widget(self.plant_box)
        
        # Full Image box
        self.full_img_box = ImageBox(parent_screen=self, camera_screen_name=ScreenNames.CAMERA_SCREEN)
        page.add_widget(self.full_img_box)
        
        # Low Image box
        self.low_img_box = ImageBox(parent_screen=self, camera_screen_name=ScreenNames.CAMERA_SCREEN)
        page.add_widget(self.low_img_box)
        
        # Mid Image box
        self.mid_img_box = ImageBox(parent_screen=self, camera_screen_name=ScreenNames.CAMERA_SCREEN)
        page.add_widget(self.mid_img_box)
        
        # High Image box
        self.high_img_box = ImageBox(parent_screen=self, camera_screen_name=ScreenNames.CAMERA_SCREEN)
        page.add_widget(self.high_img_box)
        
        # Add Leaves button
        add_leaves_button = Button(text="Add Leaves")
        add_leaves_button.bind(on_press=self.goto_add_leaves_screen)
        page.add_widget(add_leaves_button)
        
        self.add_widget(page)
        
    def goto_add_leaves_screen(self, instance):
        # Save information here
        transition_screen(self, ScreenNames.ADD_LEAVES)
        

class PlantListScreen(Screen):
    def __init__(self):
        super().__init__(name=ScreenNames.PLANT_LIST)
        FONT_SIZE = 32
        page = BoxLayout(padding=10, orientation="vertical")
        
        #TODO: Add list of buttons with plant # in them
        
        # Add Plant Button
        add_plant_button = Button(text="Add Plant")
        add_plant_button.bind(on_press=self.goto_add_plant_screen)
        page.add_widget(add_plant_button)
        
        self.add_widget(page)
        
    def goto_add_plant_screen(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = ScreenNames.ADD_PLANT

class BeginTripScreen(Screen):
    def __init__(self,):
        super().__init__(name=ScreenNames.BEGIN_TRIP)
        FONT_SIZE = 32
        page = BoxLayout(padding=10, orientation="vertical")

        # LatLong Input
        self.latlong_box = LatLongInputBox()
        page.add_widget(self.latlong_box)
        
        # Elevation Input
        self.elevation_box = ElevationBox()
        page.add_widget(self.elevation_box)
        
        # Site ID Input
        self.site_id_box = SiteIDBox()
        page.add_widget(self.site_id_box)
        
        # Date Input
        self.date_box = DateBox()
        page.add_widget(self.date_box)
        
        # Create Trip Btn
        begin_trip_btn = Button(text='Create Trip', color="green", font_size=FONT_SIZE)
        begin_trip_btn.bind(on_press=self.create_trip)
        page.add_widget(begin_trip_btn)

        # Go to home page
        go_home_btn = Button(text='Home', color="blue", font_size=FONT_SIZE)
        go_home_btn.bind(on_press=self.goto_home_screen)
        page.add_widget(go_home_btn)
        
        self.add_widget(page)
        
    def goto_home_screen(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = ScreenNames.HOME
        
    def create_trip(self, instance):
        data_store = load_data_store()
        date = self.date_box.get_date()
        gps = self.latlong_box.get_lat_long()
        elevation = self.elevation_box.get_elevation()
        site_id = self.site_id_box.get_site_id()
        data_key = f"S{site_id}_{date.replace("/", "_")}"
        
        # TODO Check if exists, may need to be careful with overriding
        
        app = get_running_app()
        app.set_current_data_key(data_key)
        data_key = app.get_current_data_key()
        
        data_store.put(
            data_key,
            gps = gps,
            elevation = elevation,
            date = date,
            site_id = site_id,
        )
        self.manager.transition.direction = 'left'
        self.manager.current = ScreenNames.PLANT_LIST
        

class HomeScreen(Screen):
    def __init__(self):
        super().__init__(name=ScreenNames.HOME)
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
        pass
        #self.manager.transition.direction = 'left'
        #self.manager.current = ScreenNames.TEST_CAMERA_SCREEN

class LeafDataCollectionApp(App):
    def __init__(self):
        super().__init__()
        self.data_key = None
        self.camera_exit_screen_name = ScreenNames.HOME
        self.current_image_holder: ImageHolder = None
        self.camera = Camera(play=True, size_hint=(1, 1), allow_stretch=True, keep_ratio=True)
        
    def set_current_data_key(self, data_key: str):
        self.data_key = data_key
        
    def get_current_data_key(self):
        return self.data_key
    
    def set_camera_exit_screen(self, screen_name):
        self.camera_exit_screen_name = screen_name
        
    def get_camera_exit_screen(self):
        return self.camera_exit_screen_name
    
    def set_current_image_holder(self, image_holder: ImageHolder):
        self.current_image_holder = image_holder
        
    def get_current_image_holder(self):
        return self.current_image_holder
    
    def get_camera(self):
        return self.camera
        
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen())
        sm.add_widget(BeginTripScreen())
        sm.add_widget(PlantListScreen())
        sm.add_widget(AddPlantScreen())
        sm.add_widget(CameraScreen())
        return sm


if __name__ == '__main__':
    app = LeafDataCollectionApp()
    app.run()
