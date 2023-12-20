# game settings 
WIDTH = 1000
HEIGHT = 686
FPS = 30



# player settings
PLAYER_JUMP = 30
PLAYER_GRAV = 1.5
PLAYER_FRIC = 0.2

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (116, 102, 59)

GROUND =(0, HEIGHT - 40, WIDTH, 40, "normal")

# fixed bug that let the player fall through half the platform 
PLATFORM_LIST = [
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20,"normal"),
                 (125, HEIGHT - 350, 100, 20, "moving"),
                 (130, HEIGHT - 500, 100, 10, "moving"),
                 (222, 200, 100, 20, "normal"),
                 (175, 100, 100, 20, "normal")]