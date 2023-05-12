import pygame
import os

from button import Button
from src.shapes import Rectangle, Circle
from src import *

pygame.init()
pygame.font.init()

#Colors
BROWN = (95, 99, 79)
BLUE = (155, 196, 203)

disp = pygame.display.Info()
SIZE = (disp.current_w, disp.current_h)
SIZE = (500, 400)
print(SIZE)
CENT_X = SIZE[0] // 2
CENT_Y = SIZE[1] // 2

def set_up(): 
    pygame.display.set_caption("Linked List Visualizer")
    
    font = pygame.font.SysFont("opensans", 100)
    text = font.render('Linked List Visualizer!', True, BROWN)
    textRect = text.get_rect()
    textRect.center = (CENT_X, 100)

    exit_img = pygame.image.load("button_exit.png").convert_alpha()
    exit_btn = Button(1, 1, exit_img, 2)
    exit_btn.set_center(CENT_X, 700)
    return (text, textRect, exit_btn)

def vis_BST():
    win = pygame.display.set_mode(SIZE)
    setup = set_up()
    run = True
    while run: 
        win.fill(BLUE)
        win.blit(setup[0], setup[1])
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if setup[2].draw(win):
            print("EXIT")
            pygame.quit()

    
    
def main():
    run = True
    win = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Data Structure Visualizer")

    font = pygame.font.SysFont("opensans", 100)
    text = font.render('Data Structure Visualizer!', True, BROWN)
    textRect = text.get_rect()
    textRect.center = (CENT_X, 100)

    ds_buttons = {}
    button_to_vis = {}
    MENU_OFFSET = 200

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
        i_button.set_center(x_coord, 200 + (100 * idx))
        ds_buttons[name] = i_button

        exit_img = pygame.image.load("button_exit.png").convert_alpha()
        exit_btn = Button(1, 1, exit_img, 3)
        exit_btn.set_center(CENT_X, 700)
        
    
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
                vis = None
                # match ds:
                #     case "linked-list":
                vis = LListVisualizer(SIZE[0], SIZE[1], win)
                        
                                    
                while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                return
                            vis.visualize(event)
                    


        pygame.display.update()


if __name__ == "__main__":
    main()
    pygame.quit()
