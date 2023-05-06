import pygame
import sys
from djitellopy import Tello

# Initialiser pygame et le joystick
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Initialiser le drone Tello
tello = Tello()
tello.connect()

# Définir la vitesse de base et la zone morte
base_speed = 50
deadzone = 0.1

def apply_deadzone(value, deadzone):
    return value if abs(value) > deadzone else 0.0

# Boucle principale
running = True
while running:
    # Traiter les événements de la manette
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Lire l'état des boutons A et B
    button_a = joystick.get_button(0)
    button_b = joystick.get_button(1)
    shoulder_left = joystick.get_button(4)
    shoulder_right = joystick.get_button(5)

    # Gérer les actions de décollage et d'atterrissage
    if button_a:
        tello.takeoff()
        pygame.time.delay(500)  # Ajouter une temporisation pour éviter les détections multiples
    if button_b:
        tello.land()
        pygame.time.delay(500)  # Ajouter une temporisation pour éviter les détections multiples
    
    # Gérer les actions de controle de la vitesse
    if shoulder_left:
        base_speed = 25
    if shoulder_right:
        base_speed = 50

        
    # Lire les axes du joystick
    left_y_axis = -joystick.get_axis(1)
    left_x_axis = joystick.get_axis(0)
    right_x_axis = joystick.get_axis(2)

    # Les gâchettes gauche et droite (de -1 à 1, avec -1 l'état relâché et 1 l'état enfoncé)
    left_trigger = joystick.get_axis(4)
    right_trigger = joystick.get_axis(5)

    # Appliquer la zone morte et convertir en vitesses Tello
    forward_backward_speed = int(apply_deadzone(left_y_axis, deadzone) * base_speed)
    left_right_speed = int(apply_deadzone(left_x_axis, deadzone) * base_speed)
    up_down_speed = int((right_trigger - left_trigger) * base_speed)
    yaw_speed = int(apply_deadzone(right_x_axis, deadzone) * base_speed)

    # Envoyer les commandes de vitesse au drone
    tello.send_rc_control(left_right_speed, forward_backward_speed, up_down_speed, yaw_speed)

    pygame.time.wait(50)

# Arrêter le drone et quitter pygame
tello.send_rc_control(0, 0, 0, 0)
tello.land()
pygame.quit()
sys.exit()
