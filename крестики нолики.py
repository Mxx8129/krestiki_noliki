import time

import pygame
import random

DISPLAY_WIDTH = 300
DISPLAY_HEIGHT = 300

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
FPS = 30
clock = pygame.time.Clock()
pygame.init()

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Крестики нолики")

field = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
]


def draw_grid():
    pygame.draw.line(screen, BLACK, (100, 0), (100, 300), 3)
    pygame.draw.line(screen, BLACK, (200, 0), (200, 300), 3)
    pygame.draw.line(screen, BLACK, (0, 100), (300, 100), 3)
    pygame.draw.line(screen, BLACK, (0, 200), (300, 200), 3)


def create_message(msg, color, x, y, font_name, size):
    style = pygame.font.SysFont(font_name, size)
    message = style.render(msg, True, color)
    screen.blit(message, (x, y))


def draw_tic_tac_toe():
    for i in range(3):
        for j in range(3):
            if field[i][j] == "x":
                pygame.draw.line(screen, BLACK, (j * 100 + 5, i * 100 + 5), (j * 100 + 95, i * 100 + 95), 3)
                pygame.draw.line(screen, BLACK, (j * 100 + 95, i * 100 + 5), (j * 100 + 5, i * 100 + 95), 3)
            elif field[i][j] == "0":
                pygame.draw.circle(screen, BLACK, (j * 100 + 50, i * 100 + 50), 45, 3)


# noinspection PyGlobalUndefined
def prowerka(symbol):
    flag_win = False
    global win
    for line in field:
        if line.count(symbol) == 3:
            flag_win = True
            win = [[0, field.index(line)], [1, field.index(line)], [2, field.index(line)]]
            print(win)
    for column in range(3):
        if field[0][column] == field[1][column] == field[2][column] == symbol:
            flag_win = True
            win = [[column, 0], [column, 1], [column, 2]]
            print(win)
    if field[0][0] == field[1][1] == field[2][2] == symbol:
        flag_win = True
        win = [[0, 0], [1, 1], [2, 2]]
        print(win)
    if field[0][2] == field[1][1] == field[2][0] == symbol:
        flag_win = True
        win = [[0, 2], [1, 1], [2, 0]]
        print(win)
    return flag_win


game_over = False
run_game = True
while run_game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            draw_tic_tac_toe()
            mous_pos = pygame.mouse.get_pos()
            if field[mous_pos[1] // 100][mous_pos[0] // 100] == '':
                field[mous_pos[1] // 100][mous_pos[0] // 100] = 'x'
                x = random.randint(0, 2)
                y = random.randint(0, 2)
                while field[x][y] != '':
                    x = random.randint(0, 2)
                    y = random.randint(0, 2)
                field[x][y] = '0'
        player_win = prowerka("x")
        bot_win = prowerka("0")
        result = field[0].count("x") + field[0].count("0") + field[1].count("x") + field[1].count("0") + field[2].count(
            "x") + field[2].count("0")
        if player_win or bot_win:
            game_over = True
            if player_win:
                pygame.display.set_caption("Вы победили!")
            elif bot_win:
                pygame.display.set_caption("Компьютер победил!")
            else:
                pygame.display.set_caption("Ошибка")
        elif result == 8:
            pygame.display.set_caption("Ничья")
            time.sleep(3)
            run_game = False
    screen.fill(WHITE)
    if game_over:
        pygame.draw.rect(screen, GREEN, (win[0][0] * 100, win[0][1] * 100, 100, 100))
        pygame.draw.rect(screen, GREEN, (win[1][0] * 100, win[1][1] * 100, 100, 100))
        pygame.draw.rect(screen, GREEN, (win[2][0] * 100, win[2][1] * 100, 100, 100))



    draw_grid()
    draw_tic_tac_toe()
    pygame.display.flip()
pygame.quit()
