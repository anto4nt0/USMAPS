import pygame
from pygame.locals import *
import obd
pygame.init()
#connection = obd.OBD()
connect = obd.Async(fast=False)
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
screen_w = screen.get_width()
screen_h = screen.get_height()
circle_y = screen_h/2
circle1_x = screen_w * .25
circle2_x = screen_w * .5
circle3_x = screen_w * .75
circle_rad = (circle2_x - circle1_x)/2
speed_text_x = screen_w * .25
speed_text_y = screen_h * .25
rpm_text_x = screen_w * .5
rpm_text_y = screen_h * .25
load_text_x = screen_w * .75
load_text_y = screen_h * .25
headerFont = pygame.font.SysFont("Arial", 50)
digitFont = pygame.font.SysFont("Arial", 50)
white = (255,255,255)
black = (0,0,0)
grey = (112, 128, 144)
speed = 0
rpm = 0
load = 0
def draw_hud():
	screen.fill(grey)
	pygame.draw.circle(screen, black, (int(circle1_x), int(circle_y)), int(circle_rad), 5)
	pygame.draw.circle(screen, black, (int(circle2_x), int(circle_y)), int(circle_rad), 5)
	pygame.draw.circle(screen, black, (int(circle3_x), int(circle_y)), int(circle_rad), 5)
	speed_text = headerFont.render("SPEED", True, black)
	rpm_text = headerFont.render("RPM", True, black)
	load_text = headerFont.render("LOAD", True, black)
	speed_text_loc = speed_text.get_rect(center=(speed_text_x, speed_text_y))
	rpm_text_loc = rpm_text.get_rect(center=(rpm_text_x, rpm_text_y))
	load_text_loc = load_text.get_rect(center=(load_text_x, load_text_y))
	screen.blit(speed_text, speed_text_loc)
	screen.blit(rpm_text, rpm_text_loc)
	screen.blit(load_text, load_text_loc)
def get_speed(s):
	global speed
	if not s.is_null():
		#speed = int(s.value.magnitude) #for kph
		speed = int(s.value.magnitude * .060934) #for mph
def get_rpm(r):
	global rpm
	if not r.is_null():
		rpm = int(r.value.mangitude)
def get_load(l):
	global load
	if not l.is_null():
		load = int(l.value.mangitude)
connection.watch(obd.commands.SPEED, callback=get_speed)
connection.watch(obd.commands.RPM, callback=get_rpm)
connection.watch(obd.commands.ENGINE_LOAD, callback=get_load)
connection.start()
running = True
while running:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				connection.stop()
				connection.close()
				running = False
			elif event.type == QUIT:
				connection.stop()
				connection.close()
				running = False
	draw_hud()
	speedDisplay = digitFont.render(str(speed), 3, white)
	rpmDisplay = digitFont.render(str(rpm), 3, white)
	loadDisplay = digitFont.render(" " + str(load) + " %", 3, white)
	screen.blit(loadDisplay, (circle3_x-(circle3_x/8), circle_y-45))
	screen.blit(rpmDisplay, (circle2_x-(circle2_x/8), circle_y-45))
	screen.blit(speedDisplay,(circle1_x-(circle1_x/8), circle_y-45))
	pygame.display.update()
	pygame.display.flip()