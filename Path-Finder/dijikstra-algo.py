'''
1. Create a grid of 25X25 (or any size you fancy, preferably large) small boxes. 0,0 be top left and 25,25 be bottom right
2. Color the different boxes according to the function. Add a starting box with a specific color, the blockages with another and finally, the location in another color.

'''

#Dijikstra Shortest Path Finder Algorithm Visualization
from tkinter import messagebox, Tk
import pygame
import sys

Window_Width = 500
Window_Height = 500
Row = 25
Column = 25

Box_Width = Window_Width // Column
Box_Height = Window_Height // Row

Grid=[]

class Box:
    def __init__(self,i,j):
        self.x=i
        self.y=j
        #The three flags
        self.Start=False
        self.Wall=False
        self.Target=False
    
    def draw(self,win,color): #self, window of the boxes and its color argument
        pygame.draw.rect(win, color, (self.x*Box_Width,self.y*Box_Height,Box_Width-2,Box_Height-2)) #Subtracting from Box_Width and Box_Height for the grid lines thickness

#Create the grid
for i in range(Column):
    arr=[]
    for j in range(Row):
        arr.append(Box(i,j)) #Appending the values to the array
    Grid.append(arr) #Appending the grid-array to the Array

Start_Box = Grid[0][0]
Start_Box.Start = True

Window = pygame.display.set_mode((Window_Width,Window_Height))

def main():
    Begin_Search = False #Algorithm Triggering Variable
    Target_Box_Set = False
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #Mouse-Controls
            elif event.type == pygame.MOUSEMOTION:
                x=pygame.mouse.get_pos()[0]
                y=pygame.mouse.get_pos()[1]
                #Draw the Wall for the Obstruction:
                if event.buttons[0]:
                    i=x//Box_Width
                    j=y//Box_Height
                    Grid[i][j].Wall = True
                #Set Target
                if event.buttons[2] and not Target_Box_Set:
                    i=x//Box_Width
                    j=y//Box_Height
                    Target_Box = Grid[i][j]
                    Target_Box.Target = True
                    Target_Box_Set = True
            #Start Algorithm
            if event.type == pygame.KEYDOWN and Target_Box_Set:
                Begin_Search = True
            
        
        Window.fill((0,0,0))

        for i in range(Column):
            for j in range(Row):
                Box = Grid[i][j]
                Box.draw(Window,(50,50,50))
                if Box.Start:
                    Box.draw(Window,(0,200,200))
                if Box.Wall:
                    Box.draw(Window,(90,90,90))
                if Box.Target:
                    Box.draw(Window,(200,200,0))

        pygame.display.flip()

main()