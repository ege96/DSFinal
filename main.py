import pygame
import os

from button import Button
from src.shapes import Rectangle, Circle
from src import *

# Colors
from src.COLORS import BLUE, BROWN, BLACK

pygame.init()
pygame.font.init()

disp = pygame.display.Info()
SIZE = (disp.current_w, disp.current_h)
CENT_X = SIZE[0] // 2
CENT_Y = SIZE[1] // 2


def main():
    run = True
    win = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Data Structure Visualizer")

    font = pygame.font.SysFont("opensans", 210)
    text = font.render('Data Structure Visualizer!', True, BROWN)
    textRect = text.get_rect()
    textRect.center = (CENT_X, 150)

    ds_buttons = {}
    MENU_OFFSET = 400

    BUTTON_FILES = os.listdir("Images")

    for idx, file_name in enumerate(BUTTON_FILES):
        if idx > (len(BUTTON_FILES) - 1) // 2:
            x_coord = CENT_X - MENU_OFFSET
            idx -= len(BUTTON_FILES) // 2
        else:
            x_coord = CENT_X + MENU_OFFSET

        name = file_name.split("_")[-1].split(".")[0]

        i_img = pygame.image.load(os.path.join("Images",
                                               file_name)).convert_alpha()
        i_button = Button(350, 210, i_img, 1)
        i_button.set_center(x_coord, 375 + (250 * idx))
        ds_buttons[name] = i_button

        exit_img = pygame.image.load("button_exit.png").convert_alpha()
        exit_btn = Button(1, 1, exit_img, 1)
        exit_btn.set_center(CENT_X, 900)

    while run:
        win.fill(BLUE)
        win.blit(text, textRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if exit_btn.draw(win):
            print("EXIT")
            pygame.quit()

        for ds in ds_buttons:
            if ds_buttons[ds].draw(win):
                # call to visaulization
                vis_font = pygame.font.SysFont("Calibri", 25, True, False)
                print(ds)
                match ds:
                    case "linked-list":
                        vis = LList(win, vis_font)
                    case "graph":
                        vis = GraphTest(win, vis_font)
                    case "stack":
                        vis = Stack(win, vis_font)
                    case "queue":
                        vis = Queue(win, vis_font)

                vis.visualize()

        pygame.display.update()


if __name__ == "__main__":
    main()
    pygame.quit()
