import sys

import pygame

def check_events(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right
                # ship.rect.centerx += 1
                ship.moving_right = True # setting flag moving_right as true when player press button

            elif event.key == pygame.K_LEFT:
                ship.moving_left = True # setting flag moving_left as true when player press button

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False # setting flag moving_right as false when player release button

            elif event.key == pygame.K_LEFT:
                ship.moving_left = False # setting flag moving_left as false when player release button

def update_screen(ai_settings, screen, ship):
    # Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()

