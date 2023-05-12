import pygame
import os

from button import Button
from src.shapes import Rectangle, Circle
from src import *

pygame.init()
pygame.font.init()

#Colors
from src.COLORS import BLUE, BROWN, BLACK


disp = pygame.display.Info()
SIZE = (disp.current_w, disp.current_h)
SIZE = (500, 400)
print(SIZE)
CENT_X = SIZE[0] // 2
CENT_Y = SIZE[1] // 2

def LList_vis(surface, font):
    last_add_time = pygame.time.get_ticks()
    # Create a LList object
    linked_list = LList(surface, font)

    run = True

    # Main loop
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Check if the user clicked the left mouse button
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                # Check if the user clicked on a node
                linked_list.remove(pos)

                # Check if the user clicked on the "Add Node" button
                if 10 <= pos[0] <= 120 and 10 <= pos[1] <= 50:
                    linked_list.add(linked_list.node_count + 1)

                # Check if the user clicked on the "Insert Node" button
                elif 125 <= pos[0] <= 255 and 10 <= pos[1] <= 50:
                    pos = input("Enter the position to insert: ")
                    linked_list.insert_node(linked_list.node_count + 1, int(pos))

                # Check if the user clicked on the "Exit" button
                elif 260 <= pos[0] <= 330 and 10 <= pos[1] <= 50:
                    run = False

        # Clear the surface
        surface.fill(BLUE)

        # Display the linked list
        linked_list.display()

        # Draw the "Add Node" button
        button_rect = pygame.Rect(10, 10, 110, 40)
        pygame.draw.rect(surface, BLACK, button_rect, 2)
        text = font.render("Add Node", True, BLACK)
        text_rect = text.get_rect(center=button_rect.center)
        surface.blit(text, text_rect)

        # Draw the "Insert Node" button
        button_rect = pygame.Rect(125, 10, 130, 40)
        pygame.draw.rect(surface, BLACK, button_rect, 2)
        text = font.render("Insert Node", True, BLACK)
        text_rect = text.get_rect(center=button_rect.center)
        surface.blit(text, text_rect)

        # Draw the "Exit" button
        button_rect = pygame.Rect(260, 10, 70, 40)
        pygame.draw.rect(surface, BLACK, button_rect, 2)
        text = font.render("Exit", True, BLACK)
        text_rect = text.get_rect(center=button_rect.center)
        surface.blit(text, text_rect)

        # Update the surface
        pygame.display.flip()

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
                # call to visaulization
                vis_font = pygame.font.SysFont("Calibri", 25, True, False)
                match ds:
                    case "linked-list":
                        LList_vis(win, vis_font)
                    
                
                print(ds)

        pygame.display.update()


if __name__ == "__main__":
    main()
    pygame.quit()
