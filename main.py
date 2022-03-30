import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from minimax.algorithm import minimax
from checkers.board import Board
from minimax.algorithm import get_all_moves

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        if game.turn == WHITE:
            moves = get_all_moves(game.get_board(),WHITE, game)
            print(moves)
            if not moves:
                print("RED WON")
                run = False
            moves = get_all_moves(game.get_board(), RED, game)
            print(moves)
            if not moves:
                print("WHITE WON")
                run = False
            value, new_board = minimax(game.get_board(), 4, WHITE, game)
            game.ai_move(new_board)
        
        if game.winner() != None:
            if game.winner() == WHITE:
                print('WHITE WON')
            else:
                print("RED WON")
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    
    pygame.quit()

main()
