import pygame as pg
from source.main import main

import pygame
import os

os.environ["SDL_VIDEODRIVER"] = "dummy"  # Set virtual display driver
pygame.init()

if __name__=='__main__':
    main()
    pg.quit()
