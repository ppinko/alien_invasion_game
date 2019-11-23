import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize pygame, settings and screen object
    pygame.init() # initilizing background setting
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets in
    bullets = Group() # this class behaves like a list for games with extra functionality

    # Start the main loop for the game
    while True:

        # Watch for keyboard and mouse events
        # event is an action that user perform 
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update() # call bullet.update() for each bullet in the group bullets
        gf.update_screen(ai_settings, screen, ship, bullets)
        
run_game()
