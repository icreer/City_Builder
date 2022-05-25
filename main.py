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

        if event.type == pygame.KEYUP:
            if event.key == K_a:
                keys[0] = False
            if event.key == K_d:
                keys[1] = False
            if event.key == K_w:
                keys[2] = False
            if event.key == K_s:
                keys[3] = False

    def setup_pygame(self):
        screen = pygame.display.set_mode((cp.width , cp.height))
        pygame.display.set_caption(cp.title)
        pygame.init()
        return screen
    
    def menu(self,screen,font):
        global game_state
        play_text = font.render("Play", True, cp.White)
        play_text_y_offset = 0

        score_text = font.render("HIGH SCORE: 0", True, cp.White)
        while game_state == 0:
            screen.fill(cp.Blue)
            screen.blit(play_text,(cp.width/2 - play_text.get_width() / 2 , cp.height / 2 - play_text.get_height() / 2 + play_text_y_offset))
            screen.blit(score_text, (cp.width / 2 - score_text.get_width() , cp.height /2 - score_text.get_height() / 2 + 150))
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    game_state = 2
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
    

    def game(self, screen, font):
        global game_state
        Roma_text = font.render("Roma",True,cp.Purple)
        Eygpt_text = font.render("Eygpt",True,cp.Yellow)
        China_text = font.render("China",True,cp.Red)
        self.previous_frame_time = time.time()
        
        #        A      D      W      S
        keys = [False, False, False, False]
        while game_state == 1: 
           
            screen.fill(cp.Black)
            screen.blit(Roma_text,(cp.width * .17,cp.height/3))
            screen.blit(Eygpt_text,(cp.width *.45, cp.height/3))
            screen.blit(China_text,(cp.width * .75, cp.height/3))
            for event in pygame.event.get():
                
                mouse_x = pygame.mouse.get_pos()[0]
                mouse_y = pygame.mouse.get_pos()[1]
                if event.type == pygame.QUIT:
                    game_state = 2
                if mouse_x > (cp.width *.17) - (Roma_text.get_width() * .5) and mouse_x < (cp.width * .17) + (Roma_text.get_width() * .5):
                    if mouse_y > (cp.height * .33) - (Roma_text.get_height() *.5 ) and mouse_y < (cp.height * .33) + (Roma_text.get_heigth()*.5):
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            #screen.fill(cp.Purple)
                            game_state = 3
                            print("works")
                
            pygame.display.update()

    def __init__(self) -> None:
        while game_state != 2:
            screen = self.setup_pygame()
            font = pygame.font.Font("Inter.ttf",32)

            if game_state == 0:
                self.menu(screen, font)
            elif game_state == 1 :
                self.previous_frame_time = time.time()
                self.game(screen, font)
            elif game_state == 3 :
                self.Roma(screen,font)

game = Main()