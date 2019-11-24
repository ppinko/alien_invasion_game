import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize pygame, settings and screen object
    pygame.init() # initilizing background setting
    ai_settings = Settings() # derive settings from settings.py
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height)) # initializing screen size
    pygame.display.set_caption("Alien Invasion") # set name of the game at the top of the screen

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store games statistics
    stats = GameStats(ai_settings)

    # Make a ship
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets in
    bullets = Group() # this class behaves like a list for games with extra functionality

    # Make a group to store aliens in
    aliens = Group()
    
    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, 
                play_button)
        
run_game()
