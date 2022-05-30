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
        global game_state, clean_water_percentage,number_of_people,strength,amount_of_food,amount_of_metal,amount_of_rocks
        clean_water = font.render(f"Water: {clean_water_percentage}",True,cp.Black)
        people = font.render(f"People: {number_of_people}", True, cp.Black)
        Strength = font.render(f"Strength: {strength}", True, cp.Black)
        food = font.render(f"Food: {amount_of_food}", True, cp.Black)
        metal = font.render(f"Metal:{amount_of_metal}",True,cp.Black)
        rocks = font.render(f"Rocks: {amount_of_metal}",True,cp.Black)
        self.previous_frame_time = time.time()
        while game_state > 2:
            screen.blit(clean_water,(cp.width * .17,cp.height * 0))
            screen.blit(people,(cp.width * 0,cp.height * 0))
            screen.blit(Strength,(cp.width * .34,cp.height * 0))
            screen.blit(food,(cp.width * .53,cp.height * 0))
            screen.blit(metal,(cp.width * .68,cp.height * 0))
            screen.blit(rocks,(cp.width * .85,cp.height * 0))
            pygame.display.update()
        
    
    def Roma(self,screen,font,keys):
        global game_state
        self.previous_frame_time = time.time()
        while game_state == 3:
            screen.fill(cp.Purple)
            self.HUD(screen,font)
            pygame.display.update()

    def Eygpt(self,screen,font,keys):
        global game_state
        self.previous_frame_time = time.time()
        while game_state == 4:
            screen.fill(cp.Yellow)
            self.HUD(screen,font)
            pygame.display.update()
    
    def China(self,screen,font,keys):
        global game_state
        self.previous_frame_time = time.time()
        while game_state == 5:
            screen.fill(cp.Red)
            self.HUD(screen,font)
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
            font_small = pygame.font.Font("Inter.ttf",20)
             #        A      D      W      S      1     2      3
            keys = [False, False, False, False, False, False, False]
            
            if game_state == 0:
                self.menu(screen, font)
            elif game_state == 1 :
                self.previous_frame_time = time.time()
                self.game(screen, font, keys)
            elif game_state == 3 :
                self.Roma(screen,font_small,keys)
            elif game_state == 4:
                self.Eygpt(screen,font_small,keys)
            elif game_state == 5:
                self.China(screen,font_small,keys)

game = Main()