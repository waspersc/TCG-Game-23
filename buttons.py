import pygame as pg#imports the pg module which allows pg to operate
import random #imports a random number generator if needed during the pg
import os #imports and operating system module so python can interact with the computer such as file searching
import sprites #imports the sprites module where all the games sprites are held and listed

WIDTH = 1920 #the width of the window stored in a variable
HEIGHT = 1080 #the height of the window stored in a variable
FPS = 60 #the frame count limit for the window so it loops 60 times per second
score = 0

#colours
#this is so i can easily call on colour value which are stored in variables
RED = (255,0,0) #the rgb value for red
GREEN = (0,255,0) #the rgb value for blue
BLUE = (0,0,255) #the rgb value for green
WHITE = (255,255,255) #the rgb value for white
BLACK = (0,0,0) #the rgb value for black
pg.init()


def menuPlayButton(self):
    menuFont = pg.font.SysFont('Corbel',35, bold = True, italic = False)
    font = menuFont.render('Play', True, WHITE)
    fontRect = font.get_rect()
    fontRect.center = (WIDTH/2, HEIGHT/2)   
    pg.draw.rect(self.screen, WHITE, [(876.2), (485), 165, 110])
    pg.draw.rect(self.screen, BLACK, [(885), (490), 150, 100])
    self.screen.blit(font, fontRect)

def finalScoreMenuButton(self):
    menuFont = pg.font.SysFont('Corbel',35, bold = True, italic = False)
    font = menuFont.render('Menu', True, WHITE)
    fontRect = font.get_rect()
    fontRect.center = (WIDTH/2, HEIGHT/2)   
    pg.draw.rect(self.screen, WHITE, [(876.2), (485), 165, 110])
    pg.draw.rect(self.screen, BLACK, [(885), (490), 150, 100])
    self.screen.blit(font, fontRect)

def menuButton(self):
    menuFont = pg.font.SysFont('Corbel',35, bold = True, italic = False)
    font = menuFont.render('Menu', True, WHITE)
    fontRect = font.get_rect()
    fontRect.center = (WIDTH/2, 741)
    pg.draw.rect(self.screen, WHITE, [(877.5), (683), 165, 110])
    pg.draw.rect(self.screen, BLACK, [(885), (688), 150, 100])
    self.screen.blit(font, fontRect) 

def highScoreBoardButton(self):
    highScoreBoardFont = pg.font.SysFont('Corbel', 32, bold = True, italic = False)
    font = highScoreBoardFont.render('High Score', True, WHITE)
    fontRect = font.get_rect()
    fontRect.center = (WIDTH/2, 775)
    pg.draw.rect(self.screen, WHITE, [(877.5), (719), 165, 110])
    pg.draw.rect(self.screen, BLACK, [(885), (724), 150, 100])
    self.screen.blit(font, fontRect)


def drawScore(self):
    scoreFont = pg.font.SysFont('Corbel',50, bold = True, italic = False)
    font = scoreFont.render("Score:", True, RED)
    fontRect = font.get_rect()
    fontRect.center = (1700, 50)
    self.screen.blit(font, fontRect)
    scoreString = scoreFont.render(str(self.score), True, RED)
    scoreStringRect = scoreString.get_rect()
    scoreStringRect.center = (1800, 50)
    self.screen.blit(scoreString ,scoreStringRect)

def drawTimer(self):
    timerFont = pg.font.SysFont('Corbel', 50, bold = True, italic = False)
    font = timerFont.render("Time:", True, RED)
    fontRect = font.get_rect()
    fontRect.center = (1700, 1030)
    self.screen.blit(font, fontRect)
    timerString = timerFont.render(str(self.humanTimer), True, RED)
    timerStringRect = timerString.get_rect()
    timerStringRect.center = (1825, 1030)
    self.screen.blit(timerString, timerStringRect)

def drawFinalScoreScreen(self):
    scoreFont = pg.font.SysFont('Corbel',70, bold = True, italic = False)
    font = scoreFont.render("YOUR FINAL SCORE:", True, RED)
    fontRect = font.get_rect()
    fontRect.center = (WIDTH/2, 200)
    self.screen.blit(font, fontRect)
    scoreString = scoreFont.render(str(self.score), True, RED)
    scoreStringRect = scoreString.get_rect()
    scoreStringRect.center = (1350, 200)
    self.screen.blit(scoreString ,scoreStringRect)

def drawMenuTitleScreen(self):
    scoreFont = pg.font.SysFont('Corbel',70, bold = True, italic = False)
    font = scoreFont.render("Main Menu", True, WHITE)
    fontRect = font.get_rect()
    fontRect.center = (WIDTH/2, 200)
    self.screen.blit(font, fontRect)

def drawPauseTitleScreen(self):
    scoreFont = pg.font.SysFont('Corbel',70, bold = True, italic = False)
    font = scoreFont.render("Paused", True, BLACK)
    fontRect = font.get_rect()
    fontRect.center = (WIDTH/2, 200)
    self.screen.blit(font, fontRect)

def drawHighScoreBoardTitle(self):
    scoreFont = pg.font.SysFont('Corbel',70, bold = True, italic = False)
    font = scoreFont.render("Leaderboards", True, WHITE)
    fontRect = font.get_rect()
    fontRect.center = (WIDTH/2, 200)
    self.screen.blit(font, fontRect)

def drawHighScoreValue(self):
    if os.path.exists('high_score.txt'):
        with open('high_score.txt', 'r') as file:
            high_scoreUnsorted = file.readlines()
            high_score = sorted(high_scoreUnsorted, reverse = True)
    scoreFont = pg.font.SysFont('Corbel', 70, bold = True, italic = True)
    font = scoreFont.render(str(high_score), True, WHITE)
    fontRect = font.get_rect()
    fontRect.center = (WIDTH/2, 400)
    self.screen.blit(font, fontRect)    
            