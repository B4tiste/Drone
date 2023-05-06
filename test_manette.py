import pygame
import sys

# Initialisez pygame et la manette
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Créez une fenêtre pygame
screen = pygame.display.set_mode((640, 480))

# Boucle principale
running = True
while running:
    screen.fill((255, 255, 255))
    
    # Traitez les événements de la manette
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Affichez les valeurs des axes
    for i in range(joystick.get_numaxes()):
        axis_value = joystick.get_axis(i)
        text = f"Axe {i}: {axis_value:.2f}"
        font = pygame.font.Font(None, 36)
        text_surface = font.render(text, True, (0, 0, 0))
        screen.blit(text_surface, (10, 30 * i))

    # Affichez les valeurs des boutons
    for i in range(joystick.get_numbuttons()):
        button_value = joystick.get_button(i)
        text = f"Bouton {i}: {'Enfoncé' if button_value else 'Relâché'}"
        font = pygame.font.Font(None, 36)
        text_surface = font.render(text, True, (0, 0, 0))
        screen.blit(text_surface, (320, 30 * i))

    # Affichez les valeurs des chapeaux (D-pad)
    for i in range(joystick.get_numhats()):
        hat_value = joystick.get_hat(i)
        text = f"Chapeau {i}: {hat_value}"
        font = pygame.font.Font(None, 36)
        text_surface = font.render(text, True, (0, 0, 0))
        screen.blit(text_surface, (10, 360 + 30 * i))
    
    pygame.display.flip()

# Quittez pygame
pygame.quit()
sys.exit()
