import os

from src import *
# Colors
from src.COLORS import BLUE, BROWN
from src.button import Button


def main():
    # initialize pygame
    pygame.init()
    pygame.font.init()

    disp = pygame.display.Info()
    SIZE = (disp.current_w, disp.current_h)

    # center of screem
    CENT_X = SIZE[0] // 2
    CENT_Y = SIZE[1] // 2

    # set run flag and window size
    run = True
    win = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Data Structure Visualizer")

    # title
    font = pygame.font.SysFont("opensans", 150)
    text = font.render('Data Structure Visualizer!', True, BROWN)
    textRect = text.get_rect()
    textRect.center = (CENT_X, 150)

    ds_buttons = {}
    MENU_OFFSET = 400

    BUTTON_FILES = os.listdir("Images")

    # create buttons
    for idx, file_name in enumerate(BUTTON_FILES):
        if idx > (len(BUTTON_FILES) - 1) // 2:
            x_coord = CENT_X - MENU_OFFSET
            idx -= len(BUTTON_FILES) // 2
        else:
            x_coord = CENT_X + MENU_OFFSET

        name = file_name.split("_")[-1].split(".")[0]

        i_img = pygame.image.load(os.path.join("Images",
                                               file_name)).convert_alpha()
        i_button = Button(350, 210, i_img, 0.75)
        i_button.set_center(x_coord, 350 + (200 * idx))
        ds_buttons[name] = i_button

    exit_img = pygame.image.load("button_exit.png").convert_alpha()
    exit_btn = Button(1, 1, exit_img, 0.75)
    exit_btn.set_center(CENT_X, 750)

    while run:
        win.fill(BLUE)
        win.blit(text, textRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if exit_btn.draw(win):
            print("EXIT")
            return

        # font to use for visualization
        vis_font = pygame.font.SysFont("Calibri", 25, True, False)

        for ds in ds_buttons:
            # if button is clicked
            if ds_buttons[ds].draw(win):
                # call to visualization
                print(ds)
                match ds:
                    case "linked-list":
                        vis = LList(win, vis_font)
                    case "graph":
                        vis = Graph(win, vis_font)
                    case "stack":
                        vis = Stack(win, vis_font)
                    case "queue":
                        vis = Queue(win, vis_font)
                    case _:
                        raise RuntimeError("Invalid Data Structure Selected")

                vis.visualize()

        pygame.display.update()


if __name__ == "__main__":
    main()
    pygame.quit()
