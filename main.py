import constant as cp
import pygame
from pygame.locals import *
from pygame.math import Vector2
from pygame import mixer
import time
import random
import math

game_state = 0
number_of_people = 0
amount_of_food = 0
clean_water_percentage = 0
strength = 0
amount_of_rocks = 0
amount_of_metal = 0 
class Player():
    pass

class HUD():
    pass

class CITY():
    pass

class Main():
    def handle_inputs(self,keys,event):
        if event.type == pygame.KEYDOWN:
            if event.key == K_a:
                keys[0] = True
            if event.key == K_d:
                keys[1] = True
            if event.key == K_w:
                keys[2] = True
            if event.key == K_s:
                keys[3] = True
            if event.key == K_1:
                keys[4] = True
            if event.key == K_2:
                keys[5] = True
            if event.key == K_3:
                keys[6] = True

        if event.type == pygame.KEYUP:
            if event.key == K_a:
                keys[0] = False
            if event.key == K_d:
                keys[1] = False
            if event.key == K_w:
                keys[2] = False
            if event.key == K_s:
                keys[3] = False
            if event.key == K_1:
                keys[4] = False
            if event.key == K_2:
                keys[5] = False
            if event.key == K_3:
                keys[6] = False
            

    def setup_pygame(self):
        screen = pygame.display.set_mode((cp.width , cp.height))
        pygame.display.set_caption(cp.title)
        pygame.init()
        return screen
    
    def menu(self,screen,font):
        global game_state
        play_text = font.render("Play", True, cp.White)
        play_text_y_offset = 0

        score_text = font.render("Press any key to contune:", True, cp.White)
        while game_state == 0:
            screen.fill(cp.Blue)
            screen.blit(play_text,(cp.width/2 - play_text.get_width() / 2 , cp.height / 2 - play_text.get_height() / 2 + play_text_y_offset))
            screen.blit(score_text, (cp.width / 2 - score_text.get_width() , cp.height /2 - score_text.get_height() / 2 + 150))
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    game_state = 2
                if event.type == pygame.KEYDOWN:
                    game_state = 1
                if pygame.mouse.get_pos()[0] < cp.width/2 + play_text.get_width() / 2 and pygame.mouse.get_pos()[0] > cp.width/2 - play_text.get_width() / 2:
                    if pygame.mouse.get_pos()[1] < cp.height/2 + play_text.get_height() / 2 + play_text_y_offset and pygame.mouse.get_pos()[1] > cp.height/2 - play_text.get_height() / 2 + play_text_y_offset:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            game_state = 1
            pygame.display.update()

    def HUD(self,screen,font):
        global game_state
        self.previous_frame_time = time.time()
        while game_state > 2:
            pygame.display.update()
        pass
    
    def Roma(self,screen,font):
        global game_state
        self.previous_frame_time = time.time()
        while game_state == 3:
            screen.fill(cp.Purple)
            pygame.display.update()

    def Eygpt(self,screen,font):
        global game_state
        self.previous_frame_time = time.time()
        while game_state == 4:
            pygame.display.update()
    
    def China(self,screen,font):
        global game_state
        self.previous_frame_time = time.time()
        while game_state == 5:
            pygame.display.update()
    

    def game(self, screen, font, keys):
        global game_state
        Roma_text = font.render("Roma",True,cp.Purple)
        Roma_Number_text = font.render("1",True,cp.Purple)
        # Cairo will often be refird to as Eygpt
        Eygpt_text = font.render("Cairo",True,cp.Yellow)
        Eygpt_number_text = font.render("2",True,cp.Yellow)
        # Shanghai will often be refird to as China
        China_text = font.render("Shanghai",True,cp.Red)
        China_number_number = font.render("3",True,cp.Red)


        Button_test = font.render("Press the number below the city you want to play as ",True,cp.White)
        self.previous_frame_time = time.time()
        
        while game_state == 1: 
            # Write screen full of of the information needed
            screen.fill(cp.Black)
            # This is the City Text
            screen.blit(Roma_text,(cp.width * .10,cp.height/3))
            screen.blit(Eygpt_text,(cp.width *.45, cp.height/3))
            screen.blit(China_text,(cp.width * .75, cp.height/3))
            # Instruciton text
            screen.blit(Button_test,(cp.width * .10, 100))
            # The numbers under the city
            screen.blit(Roma_Number_text,(cp.width * .14 , cp.height *.40))
            screen.blit(Eygpt_number_text,(cp.width * .48, cp.height * .40))
            screen.blit(China_number_number,(cp.width * .80, cp.height * .40))
            
            
            for event in pygame.event.get():
                self.handle_inputs(keys,event)
                if event.type == pygame.QUIT:
                    game_state = 2
                #if event.type == pygame.KEYDOWN:
                    #if event.type == K_1:
                       # keys
                       # game_state = 3
                    #if event.type == K_2:
                        #game_state = 4
                    #if event.type == K_3:
                       # game_state = 5
                #if mouse_x > (cp.width *.17) - (Roma_text.get_width() * .5) and mouse_x < (cp.width * .17) + (Roma_text.get_width() * .5):
                    #if mouse_y > (cp.height * .33) - (Roma_text.get_height() *.5 ) and mouse_y < (cp.height * .33) + (Roma_text.get_heigth()*.5):
                       # if event.type == pygame.MOUSEBUTTONDOWN:
                            #screen.fill(cp.Purple)
                            #game_state = 3
            
                            #print("works")
            if keys[4] == True:
                game_state = 3
            if keys[5] == True:
                game_state = 4
            if keys[6] == True:
                game_state = 5
                
            pygame.display.update()

    def __init__(self) -> None:
        while game_state != 2:
            screen = self.setup_pygame()
            font = pygame.font.Font("Inter.ttf",32)
             #        A      D      W      S      1     2      3
            keys = [False, False, False, False, False, False, False]
            
            if game_state == 0:
                self.menu(screen, font)
            elif game_state == 1 :
                self.previous_frame_time = time.time()
                self.game(screen, font, keys)
            elif game_state == 3 :
                self.Roma(screen,font)
            elif game_state == 4:
                self.Eygpt(screen,font)
            elif game_state == 5:
                self.China(screen,font)

game = Main()