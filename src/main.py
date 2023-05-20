import pygame
import button
import chessMain

pygame.init()

# create game window
SCREEN_WIDTH = 901
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chess")
logo = pygame.image.load('../assets/images/chess _logo.png')
pygame.display.set_icon(logo)
background = pygame.image.load('../assets/images/background.jpg')


# define fonts
font = pygame.font.SysFont("arialblack", 40)

# define colours
TEXT_COL = (0, 0, 0)

# load button images
playwithcomputer_img = pygame.image.load('../assets/images/button_play-with-computer.png').convert_alpha()
playwithfriend_img = pygame.image.load('../assets/images/button_play-with-friend.png').convert_alpha()

# create button instances
playwithcomputer_button = button.Button(270, 365, playwithcomputer_img, 1)
playwithfriend_button = button.Button(270, 455, playwithfriend_img, 1)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def main():
    # game variables
    game_paused = True
    menu_state = "main"
    # game loop
    run = True
    while run:
        # screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))
        # check if game is paused
        if game_paused == True:
            # check menu state
            draw_text('CHOOSE OPTION', font, TEXT_COL, 265, 70)
            if menu_state == "main":
                if playwithcomputer_button.draw(screen):
                    menu_state = "play with computer"
                if playwithfriend_button.draw(screen):
                    menu_state = "play with friend"

            if menu_state == "play with computer":
                if __name__ == '__main__':
                    chessMain.playwithcomputer = True
                    chessMain.main()
                menu_state = "main"

            if menu_state == "play with friend":
                if __name__ == '__main__':
                    chessMain.playwithcomputer = False
                    chessMain.main()
                menu_state = "main"
        else:
            pass

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
