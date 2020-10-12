import pygame
import sys
import math
from game import Game
from game import GameWonException, GameDrawException

class GUI:
    def __init__(self, game):
        self._game = game

    def _readPLayerMove(self):
        cmd = input("Give column:")
        return int(cmd)

    def drawBoard(self, board, SQUARESIZE, RADIUS, screen):
        BLUE = (0,0,255)
        BLACK = (0,0,0)
        RED = (255,0,0)
        YELLOW = (255, 255, 0)
        for r in range(6):
            for c in range(7):
                pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
                if board.get(r,c) == 0:
                    pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
                elif board.get(r,c) == 1:
                    pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
                elif board.get(r,c) == -1:
                    pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
        pygame.display.update()

    def drawMotion(self, SQUARESIZE, RADIUS, screen, width, posx):
        BLACK = (0,0,0)
        YELLOW = (255, 255, 0)
        pygame.draw.rect(screen, BLACK, (0,0,width, SQUARESIZE))
        pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()

    def message(self, msg, screen):
        msg_font = pygame.font.SysFont("Copperplate Gothic Bold", 75)
        BLUE = (0,0,255)
        BLACK = (0,0,0)
        RED = (255,0,0)
        YELLOW = (255, 255, 0)
        SQUARESIZE = 90
        width = 7 * SQUARESIZE
        if msg == "player win":
            pygame.draw.rect(screen, BLACK, (0,0,width, SQUARESIZE))
            label = msg_font.render("Congrats! Player won.", 1, YELLOW)
            screen.blit(label, (40, 10))
            pygame.display.update()

        elif msg == "computer win":
            pygame.draw.rect(screen, BLACK, (0,0,width, SQUARESIZE))
            label = msg_font.render("You were defeated.", 1, RED)
            screen.blit(label, (40, 10))
            pygame.display.update()
        else:
            pygame.draw.rect(screen, BLACK, (0,0,width, SQUARESIZE))
            label = msg_font.render("The game is tie.", 1, BLUE)
            screen.blit(label, (40, 10))
            pygame.display.update()


    def start(self):
        board = self._game.getBoard()
        pygame.init()
        SQUARESIZE = 90
        RADIUS = int(SQUARESIZE/2 - 5)
        width = 7 * SQUARESIZE
        height = 8 * SQUARESIZE

        size = (width, height)
        screen = pygame.display.set_mode(size)
        
        self.drawBoard(board, SQUARESIZE, RADIUS, screen)
        pygame.display.update()

        playerMove = True
        game_over = False

        while not game_over:
            try:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEMOTION:
                        posx = event.pos[0]
                        self.drawMotion(SQUARESIZE, RADIUS, screen, width, posx)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print(board)
                        
                        posx = event.pos[0]
                        column = int(math.floor(posx/SQUARESIZE))
                        playerMove = True
                        self._game.playerMove(column)
                        self._game.check()
                        print(board)

                        playerMove = not playerMove
                        self._game.computerMove()
                        self._game.check()
                        print(board)
                        self.drawBoard(board, SQUARESIZE, RADIUS, screen)

            except GameWonException:
                game_over = True
                print(board)
                self.drawBoard(board, SQUARESIZE, RADIUS, screen)
                pygame.display.update()
                if playerMove == True:
                    self.message("player win", screen)
                    print("Congrats!")
                else:
                    self.message("computer win", screen)
                pygame.time.wait(3000)
                
            except GameDrawException:
                game_over = True
                print(board)
                self.drawBoard(board, SQUARESIZE, RADIUS, screen)
                self.message("draw", screen)
                pygame.time.wait(3000)
            except ValueError:
                continue