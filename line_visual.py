#!/usr/bin/env python3
import base_visual as bv
import pygame

pygame.font.init ()
font_obj = pygame.font.SysFont (None, 20)

class LineVisual (bv.BaseVisual):
	def __init__ (self, width, height):
		bv.BaseVisual.__init__ (self, width, height)
		
	def draw (self, screen, color, offset):
		x_range = 100
		y_range = 1
		
		dataset = list ( map(lambda x: [offset [0] + int((x[0] / float(x_range)) * (self._width - 50)), offset [1] + (self._height - int ( ( (x[1] + (y_range/2.0)) / y_range) * self._height))], self._dataset))
		#print (dataset)
		pygame.draw.rect (screen, color, (offset[0], offset[1], self._width, self._height), 1)
		pygame.draw.lines (screen, color, False, dataset, 1)
		textsurface = font_obj.render ('{per}%'.format(per = round(self._dataset[-1][1] * 100, 2)), True, color)
		screen.blit (textsurface, (self._width - 50, dataset[-1][1]))
		