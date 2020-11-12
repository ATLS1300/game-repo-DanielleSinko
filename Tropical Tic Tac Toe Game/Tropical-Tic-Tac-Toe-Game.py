#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:46:15 2020

@author: DanielleSinko ApoorvaKanekal CarolineSmolky
This game is a tic tac toe game. Once the player presses a square on the board there will be a swtich between a watermelon image and a pineapple image with every other click on the squares.
Text will appear in the command line to demonstrate whos turn it is, as well as who won!
Extra Credit- ''' She liked how the images looked with the light blue color of the background. She though that it had a fun aspect to it. 
She said it would have been nice to have a 'the end or winner' pop up at the end of the game on the screen. Overall she was impressed.''' 
Instructions: press the green arrow to run the code, the board will appear and click the space bar, press any square box to start, play with a friend or as both the watermelon and pineapple  
"""

import turtle, random
import checkWin

turtle.colormode(255) #this was orignally a panel
turtle.tracer(0)
numside = 3 # number of spaces per side of the board
empty = [] 
boardList= []    
      
# List of turtles
turtList = []
for i in range(9):
  turtList.append(turtle.Turtle())
  turtList[i].hideturtle()

switch= False

# class for Game Manager
class GameManager:
    def __init__(self):        
        # =========DEFINE GLOBAL VARIABLES BELOW=========
        self.w=600
        self.h=600
        turtle.setup(self.w,self.h) # start with calling setup to turn on listeners
        turtle.listen() # for keyboard listening
        self.panel=turtle.Screen()
        self.panel.tracer(0)
        
        
        self.running = True 
        
        # splash screen
        self.splash_IMG= "splash.gif"
        self.splashTurt = turtle.Turtle()
        self.panel.onkeypress(self.clearScreen,"space")
        self.drawSplash()
        
        
        
        #creates a colormode to add a light blue background 
        self.panel.bgcolor('light blue')
        
        # Add in images
        self.watermelon = 'watermelon.gif'
        self.pineapple = 'pineapple.gif'
        self.panel.addshape(self.watermelon)
        self.panel.addshape(self.pineapple)

    def clearScreen(self):
        # for onkeypress callback function
        self.splashTurt.clear()
                   
        
    def drawSplash(self):
        #set the turtle to be on the image
        self.panel.addshape(self.splash_IMG)
        self.splashTurt.shape(self.splash_IMG)
        
        #draw image in the center
        self.splashTurt.stamp()
        self.background= self.splashTurt.stamp()
        self.splashTurt.hideturtle()
        self.splashTurt.clearstamp(self.background)
        
            
     
    def main(self):
        #object instantiation       
        self.instance = Board()
        print("makeboard")
        self.instance.player.size
        self.instance.player.WIDTH  
        self.inst= players(self.watermelon, self.pineapple)
        self.players1= players(self.watermelon, self.pineapple, True)
        self.players2= players(self.watermelon, self.pineapple, False)
        
       
        # =========ANIMATIONS BELOW=========
        # code will execute in order within the loop
        while self.running:
            
            self.inst.square_positions() #calling method in while loop 
            self.panel.onclick(self.inst.switch_btwn_players)
            self.panel.update()
            self.panel.listen()
            self.panel.mainloop()
        
    
           
            
#class for BOARD
class Board:
    #initializing the function to create the attributes of the board
    def __init__(self):
        # self.board= self.makeBoardList
        self.player=turtle.Turtle()
        self.player.size=3
        self.player.WIDTH= 8
        self.player.LINE_COLOR= 'black'
        
        for i in range(2):
            self.player.penup()
            self.player.goto(-300,-100)
            self.player.pendown()
            self.player.forward(600)
            self.player.penup()
            self.player.goto(-300,100)
            self.player.pendown()
            self.player.forward(600)
        
        self.player.right(90)
        #draw both of the vertical lines
        for i in range(2):
            self.player.penup()
            self.player.goto(-100, 300)
            self.player.pendown()
            self.player.forward(600)
            self.player.penup()
            self.player.goto(100, 300)
            self.player.pendown()
            self.player.forward(600)

                                        
#class for players
class players(GameManager):
    #initializing function to create attribtues
    def __init__(self, watermelon, pineapple, switch= True):
        GameManager.__init__(self)
        self.players1= switch
        self.players2= switch
        self.watermelon= watermelon
        self.pineapple= pineapple
        self.turtList= []
        self.positions= []
        self.turtPos= []
        self.r =3
        self.c= 3
        self.square1= []
        self.square2= []
        self.square3= [] 
        self.square4= []
        self.square5= []
        self.square6= []
        self.square7= []
        self.square8= []
        self.square9= [] 
        self.board= self.makeBoardList()
        
    #locations of squares (boundaries) 
    def square_positions(self,r=3,c=3):
        global positions, square1, square2, square3, square4, square5, square6, square7, square8, square9
        for y in range(r): 
            for x in range(c):
                if x == 0 and y==0:
                    self.square1 = [((x * 200) - 200), ((y * 200) - 200)]
                elif x == 1 and y==0:
                    self.square2 = [((x * 200) - 200), ((y * 200) - 200)]
                elif x == 2 and y==0:
                    self.square3 = [((x * 200) - 200), ((y * 200) - 200)]
                # When Y = 1
                elif x == 0 and y==1:
                    self.square4= [((x * 200) - 200), ((y * 200) - 200)]
                elif x == 1 and y==1:
                    self.square5 = [((x * 200) - 200), ((y * 200) - 200)]
                elif x == 2 and y==1:
                    self.square6 = [((x * 200) - 200), ((y * 200) - 200)]
                # When Y = 2
                elif x == 0 and y==2:
                    self.square7 = [((x * 200) - 200), ((y * 200) - 200)]
                elif x == 1 and y==2:
                    self.square8 = [((x * 200) - 200), ((y * 200) - 200)]
                elif x == 2 and y==2:
                    self.square9 = [((x * 200) - 200), ((y * 200) - 200)]
                    
        
        
            self.positions = (self.square1, self.square2, self.square3, self.square4, self.square5, self.square6, self.square7, self.square8, self.square9)
            
    #defining method inside this class to switch between players       
    def switch_btwn_players(self,x,y):
        global switch 
        # breakpoint()
        switch = not switch 
        for c in range(9): 
            self.turtPos = self.positions[c] 
            self.turtX = self.turtPos[0]
            self.turtY = self.turtPos[1]
            if round(self.turtX)-100<=round(x)<=round(self.turtX)+100 and round(self.turtY)-100<=round(y)<=round(self.turtY)+100:
                turtList[c].penup()
                turtList[c].goto(self.turtPos)
                if switch == True:
                    turtList[c].shape(self.watermelon) 
                    self.board[int(c/3)][c%3]="watermelon"
                else:
                    turtList[c].shape(self.pineapple)
                    self.board[int(c/3)][c%3]="pineapple"
                turtList[c].showturtle()
                self.winner()
        self.panel.update()
        
    #defining the method inside the class to create the BOARD     
    def makeBoardList(self): 
        board= []
        for i in range(3):
            row= []
            for j in range(3):
                row.append("")
            board.append(row)
        return board    
   
    #defining the method inside the class to create the "winner" text in the command line based on player actions
    def winner(self):
        WINNER = checkWin.checkWin(self.board)
        empty= ""
        print(WINNER)     
        gameOver = False # some variable to tell if my game is over. 
        # USE THIS TO DRAW YOUR GAMEOVER SCREEN (if you're doing that)
        
        self.panel.update()
        
        if type(WINNER) == str and WINNER!="":
            print(WINNER + ' is the winner!')
            gameOver = True # we have a winner, so the game is done.
        
        else:
            for row in self.board:
                if empty in row:
                    # are there any values equal to our "empty space" value?? 
                    # if so, gameOver isn't happening!
                    gameOver = False
                    break
                else: 
                    gameOver = True
                    print("It's a draw! No winner! \n",
                           '\n',
                           "Play again?")   
        if gameOver:
            
            turtle.done()  
                             


                
# instantiate Game Manager Object   
#call Game Manager
call= GameManager()
call.main()

turtle.done()         
            
            
            
            
            
            



