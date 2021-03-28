import pygame
from graph import Node

pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("first game")
x = 450
y= 450
h = 50
w = 50
vel = 5
run = True
while run:
	pygame.time.delay(100)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run  = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] :
		if x <0 :
			x = 0
		else:
			x -= vel
	if keys[pygame.K_RIGHT] :
		if x > 450 :
			x = 450
		else:
			x += vel
	if keys[pygame.K_UP] :
		if y <0 :
			y = 0
		else:
			y -= vel
	if keys[pygame.K_DOWN] :
		if y >500 :
			y = 500
		else:
			y += vel

	win.fill((0,0,0))
	pygame.draw.rect( win, (255,0,0), (x,y,h,w) )	
	pygame.display.update()	
pygame.quit()



