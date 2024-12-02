import pygame
import time
import random

pygame.init()

color_1 = (255,255,255) #white
color_2 = (255,255,102) #yellow
color_3 = (0,0,0) #black
color_4 = (213,200,80)
color_5 = (0,255,0) #green
color_6 = (255,0,0) #red


box_len = 900
box_height = 600

add_caption = pygame.display.set_mode((box_len,box_height))
pygame.display.set_caption("SNAKE GAME")


timer = pygame.time.Clock()

snake_block = 10
snake_speed = 15

display_style = pygame.font.SysFont("Calibri",30,"bold")
score_font = pygame.font.SysFont("Calibri",30,"bold")

def final_score(score):
    value = score_font.render("***Enjoy the Snake Game***   Your score = " + str(score),True,color_6)
    add_caption.blit(value, [0,0])

    

def make_snake(snake_block, list_snake):
    for x in list_snake:
        pygame.draw.rect(add_caption,color_3,[x[0], x[1], snake_block,snake_block])
        
        
def display_msg(msg,color):
    massege = display_style.render(msg, True, color)
    add_caption.blit(massege, [box_len/6 , box_height/3])
    
    
def game_start():
    game_over = False
    game_close = False
    
    value_x = box_len/2
    value_y = box_height/2
    
    new_x = 0
    new_y = 0
    
    list_snake = []
    snake_length = 1
    
    forx_pos = round(random.randrange(0, box_len-snake_block)/ 10.0) * 10.0
    fory_pos = round(random.randrange(0,box_height-snake_block)/ 10.0) * 10.0
    
    while not game_over:
        while game_close :
            add_caption.fill(color_3)
            display_msg("You lost! wanna play again press C else press Q", color_1)
            final_score(snake_length-1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                        
                    if event.key == pygame.K_c:
                        game_start()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_LEFT:
                    new_x = -snake_block
                    new_y = 0
                elif event.key == pygame.K_RIGHT:
                    new_x = snake_block
                    new_y = 0
                elif event.key == pygame.K_UP:
                    new_y = -snake_block
                    new_x = 0
                elif event.key == pygame.K_DOWN:
                    new_y = snake_block
                    new_x = 0
                    
        if value_x>=box_len or value_x<0 or value_y>=box_height or value_y<0:
            game_close=True
            
        value_x = value_x + new_x 
        value_y = value_y + new_y
        add_caption.fill(color_4)
        pygame.draw.rect(add_caption,color_5,[forx_pos,fory_pos,snake_block,snake_block])
        snake_head =[value_x,value_y]
        #snake_head.append(value_x)
        #snake_head.append(value_y)
        list_snake.append(snake_head)
        if len(list_snake) > snake_length:
            del list_snake[0]
        
        for x in list_snake[:-1]:
            if x == snake_head:
                game_close = True
        
        make_snake(snake_block, list_snake)
        final_score(snake_length-1)
        
        if value_x == forx_pos and value_y == fory_pos:
            forx_pos = round(random.randrange(0, box_len-snake_block)/ 10.0) * 10.0
            fory_pos = round(random.randrange(0, box_height-snake_block)/ 10.0) * 10.0
            snake_length = snake_length+1
            
        pygame.display.update()    
        timer.tick(snake_speed)
        
    pygame.quit()
    quit()
    
game_start()
            
            
            
    


