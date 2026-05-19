import pygame
import sys
import settings
from snake import Snake
from food import Food

pygame.init()

screen= pygame.display.set_mode((settings.WIDTH,settings.HEIGHT))
pygame.display.set_caption("Snake Game")

clock= pygame.time.Clock()

snake= Snake()
food=Food()
game_over=False
score=0
font=pygame.font.SysFont(None,35)
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_r:
                snake.reset()
                food.respawn()
                score=0
                game_over=False
                snake.direction=[0,0]
            if not game_over:
                if event.key == pygame.K_LEFT:
                    snake.change_direction(-settings.SPEED,0)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(settings.SPEED,0)
                elif event.key == pygame.K_UP:
                    snake.change_direction(0,-settings.SPEED)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(0,settings.SPEED)
    if not game_over:
        snake.move()
        head=snake.get_head()

        if head[0] <0 or head[0]>= settings.WIDTH or head[1]<0 or head[1]>= settings.HEIGHT:
            game_over = True
        if snake.check_self_collision():
            game_over=True
        if (head[0] < food.position[0] + settings.BLOCK_SIZE and head[0] + settings.BLOCK_SIZE > food.position[0] and head[1] < food.position[1] + settings.BLOCK_SIZE and head[1] + settings.BLOCK_SIZE > food.position[1]):
            food.respawn()
            snake.length +=1
            score+=1

    screen.fill(settings.BLACK)

    pygame.draw.rect(
        screen,
        settings.RED,
        (food.position[0],food.position[1],settings.BLOCK_SIZE,settings.BLOCK_SIZE)
    )
    for part in snake.body:
        pygame.draw.rect(
            screen,
            settings.GREEN,
            (part[0],part[1], settings.BLOCK_SIZE, settings.BLOCK_SIZE)
        )
    
    
    score_text= font.render(
        f"Score: {score}",
        True,
        settings.WHITE
    )
    screen.blit(score_text, (10, 10))
    if game_over:
        text=font.render("GAME OVER - Press R",True,settings.WHITE)
        screen.blit(text, (80,settings.HEIGHT//2))
    pygame.display.update()
    clock.tick(settings.SPEED)
pygame.quit()
sys.exit()