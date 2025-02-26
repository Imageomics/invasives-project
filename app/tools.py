import os
from kivy.app import App

from kivy.storage.jsonstore import JsonStore

def transition_screen(screen, dest_screen_name, transition_direction="left"):
    screen.manager.transition.direction = 'left'
    screen.manager.current = dest_screen_name

def get_running_app():
    app = App.get_running_app()
    return app

def get_image_save_dir():
    return os.path.join("app_data/images/")

def load_data_store():
    data_store = JsonStore("app_data/leaf_app_data.json")
    return data_store

def get_gps_location():
    """Return the GPS location of the device

    Returns:
        (float, float): tuple of GPS location in (Latitude, Longitude)
    """
    
    # TODO: implment with something
    
    return 12.5, 12.5