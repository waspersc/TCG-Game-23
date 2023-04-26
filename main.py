import pygame as pg#imports the pg module which allows pg to operate
import random #imports a random number generator if needed during the pg
import os #imports and operating system module so python can interact with the computer such as file searching
import sprites #imports the sprites module where all the games sprites are held and listed
import buttons

WIDTH = 1920 #the width of the window stored in a variable
HEIGHT = 1080 #the height of the window stored in a variable
FPS = 60 #the frame count limit for the window so it loops 60 times per second

#colours
#this is so i can easily call on colour value which are stored in variables
RED = (255,0,0) #the rgb value for red
GREEN = (0,255,0) #the rgb value for blue
BLUE = (0,0,255) #the rgb value for green
WHITE = (255,255,255) #the rgb value for white
BLACK = (0,0,0) #the rgb value for black

#images
background = pg.image.load("background.jpg")

#sprites
class Game:
    def __init__(self, score = 0, timer = 0, humanTimer = 0, name = ""):
        #creates window
        pg.init() #intialises the window    
        self.screen = pg.display.set_mode((WIDTH, HEIGHT)) #sets the dinwo size to the width and the height stored in the variable above
        pg.display.set_caption("My Game") #sets the name of window to "My Game"
        self.clock = pg.time.Clock() #sets the clock speed of the window in a varibale called clock
        #pg.mouse.set_visible(False)#removes the cursor on screen
        self.score = score
        self.timer = timer
        self.humanTimer = humanTimer
        self.name = name

    def new(self):
        self.all_sprites = pg.sprite.Group() #initialises sprite group
        self.all_sprites.add((target)) #adds target to sprite group
        self.all_sprites.add((player)) #adds the players cursor to the sprite group
        self.playing = "Menu" #sets the play state to menu

    def run(self):
        while self.playing == "Menu": #starts off at menu state
            self.menu() #menu function
            while self.playing == "High Score":
                self.highScoreBoard()
            while self.playing == "Play": #when the play state is set to "Play" start the main routine
                self.timer -= 1
                self.humanTimer = round((self.timer/60), 1)
                self.dt = self.clock.tick(FPS) #sets the clock speed
                self.keystate = pg.key.get_pressed() #initialises keystate for when it needs to be referred to
                self.events() #calls on event function
                self.update() #calls on update function
                self.draw() #calls on draw function
                if self.timer <= 0:
                    self.playing = "Final Score"
                while self.playing == "Pause": #when state is set to "Pause" initiate pause function
                    self.keystate = pg.key.get_pressed() #gets keystate to check when the user needs to unpause the game via "escape"
                    self.pause()
                while self.playing == "Final Score":
                    self.finalScoreScreen()
        print("program has fallen out of run loop") #if any loop hole exists it will print this message

    def pause(self):
        while self.playing == "Pause": #when pause function is active
            self.screen.fill(RED) #sets pause menu to green, will be changed at a later date
            buttons.menuPlayButton(self)
            buttons.menuButton(self)
            buttons.drawPauseTitleScreen(self)
            pg.display.flip() #draws the green screen
            mouse = pg.mouse.get_pos()
            for event in pg.event.get(): #when key "escape" is pressed this will set back to play state
                if event.type == pg.MOUSEBUTTONDOWN:
                    if (885 <= mouse[0] <= 1035) and (490 <= mouse[1] <= 590):
                        self.playing = "Play" #automatically starts playing after a set time
                    elif (885 <= mouse[0] <= 1035) and (682 <= mouse[1] <= 792):
                        self.playing = "Menu"
                if event.type == pg.KEYUP:
                    if event.key == pg.K_ESCAPE:
                        self.playing = "Play"
                if event.type == pg.QUIT: #allows the user to quit out if needed
                    pg.quit()
                    exit()

    def menu(self):
        while self.playing == "Menu":
            self.score = 0
            self.screen.blit(background, (0, 0)) #fills the screen with black is to be changed at a later date
            buttons.menuPlayButton(self)
            buttons.highScoreBoardButton(self)
            buttons.drawMenuTitleScreen(self)
            pg.display.flip()
            mouse = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    if (885 <= mouse[0] <= 1035) and (490 <= mouse[1] <= 590):
                        self.playing = "Play"
                        self.timer = 3600
                    if (885 <= mouse[0] <= 1035) and (718 <= mouse[1] <= 850):
                        self.playing = "High Score"

    def quit(self): #quit function
        pg.quit()

    def update(self): #updates the players cursor every clock tick to keep a track of the position
        player.update()
        

    def draw(self):
        self.screen.blit(background, (0, 0)) #draws the background image into the back
        self.all_sprites.draw(self.screen) #draws all sprites on the screen
        buttons.drawScore(self)
        buttons.drawTimer(self)
        pg.display.flip() #flips to the screen so the user can see

    def targetHit(self):
        self.score += 1
        target.update() #updates the targets position randomly

    def finalScoreScreen(self):
        self.name = str(input("what is your name?"))
        with open("high_score.txt", "w") as file:
            file.write(str(self.score)+" - "+self.name)
        while self.playing == "Final Score":
            self.screen.blit(background, (0, 0))
            buttons.drawFinalScoreScreen(self)
            buttons.finalScoreMenuButton(self)
            pg.display.flip()
            mouse = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    if (885 <= mouse[0] <= 1035) and (490 <= mouse[1] <= 590):
                        self.playing = "Menu"
    
    def highScoreBoard(self):
        while self.playing == "High Score":
            self.screen.blit(background, (0, 0))
            buttons.drawHighScoreValue(self)
            buttons.drawHighScoreBoardTitle(self)
            buttons.menuButton(self)
            pg.display.flip()
            mouse = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    if (885 <= mouse[0] <= 1035) and (682 <= mouse[1] <= 792):
                        self.playing = "Menu"



    def events(self): #checks for all events that take place
        for event in pg.event.get():
            if self.keystate[pg.K_ESCAPE]: #if escape key is pressed sets the play state to "pause"
                self.playing = "Pause"
            elif event.type == pg.MOUSEBUTTONDOWN:#detects when the user clicks a mouse button 
                if pg.sprite.collide_rect(player, target): #if the player and target sprite's position collide when the mouse button is clicked it runs the targetHit function
                    game.targetHit()
            if event.type == pg.QUIT: #quit function for middle of the game
                pg.event.clear()
                pg.quit()
                exit()

player = sprites.Player() #initialises player sprite
target = sprites.Target() #initialises target sprite
game = Game() #initialises game sprite
game.new() #starts game routine
game.run() #starts game loop

