class Settings():
    """ A Class to store all Settings for Alien Invasion"""
    
    def __init__(self):
        """ Initialize game settings """
        # Screen Settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)
        
        # Ship Settings
        self.ship_speed_factor = 1.5

        # Bullet Settings
        # Create Dark gray bullets with width 3 pixels and height 15 pixels
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)    