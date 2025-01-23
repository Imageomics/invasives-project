from kivy.uix.label import Label
from kivy.uix. textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class DateBox(BoxLayout):
    def __init__(self):
        super().__init__(orientation="vertical")
        
        date_box = BoxLayout(orientation="horizontal")
        date_lbl = Label(text="Date")
        self.date_input = TextInput()
        date_box.add_widget(date_lbl)
        date_box.add_widget(self.date_input)
        
        self.add_widget(date_box)
        
    def get_date(self):
        return self.date_input.text

class SiteIDBox(BoxLayout):
    def __init__(self):
        super().__init__(orientation="vertical")
        
        site_box = BoxLayout(orientation="horizontal")
        site_lbl = Label(text="Site ID")
        self.site_input = TextInput()
        site_box.add_widget(site_lbl)
        site_box.add_widget(self.site_input)
        
        self.add_widget(site_box)
        
    def get_site_id(self):
        return self.site_input.text

class ElevationBox(BoxLayout):
    def __init__(self):
        super().__init__(orientation="vertical")
        
        elevation_box = BoxLayout(orientation="horizontal")
        ele_lbl = Label(text="Elevation")
        self.ele_input = TextInput()
        elevation_box.add_widget(ele_lbl)
        elevation_box.add_widget(self.ele_input)
        
        self.add_widget(elevation_box)
        
    def get_elevation(self):
        return self.ele_input.text

class LatLongInputBox(BoxLayout):
    def __init__(self):
        super().__init__(orientation="vertical")
        
        lat_box = BoxLayout(orientation="horizontal")
        lat_lbl = Label(text="Latitude")
        self.lat_input = TextInput()
        lat_box.add_widget(lat_lbl)
        lat_box.add_widget(self.lat_input)
        
        long_box = BoxLayout(orientation="horizontal")
        long_lbl = Label(text="Longitude")
        self.long_input = TextInput()
        long_box.add_widget(long_lbl)
        long_box.add_widget(self.long_input)
        
        self.add_widget(lat_box)
        self.add_widget(long_box)
        
    def get_lat_long(self):
        return self.lat_input.text, self.long_input.text