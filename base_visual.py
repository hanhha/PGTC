#!/usr/bin/env python3

import numpy as np

class BaseVisual ():
	def __init__ (self, width, height):
		self._width = width
		self._height = height
		self._wrange = None
		self._hrange = None
			
	def set_dataset (self, dataset):
		self._dataset = dataset
		self._npdataset = np.array(dataset)
		self._max = np.nanmax (self._npdataset, axis = 0)
		self._min = np.nanmin (self._npdataset, axis = 0)
		self._avg = np.nanmean (self._npdataset, axis = 0)
		
	@property
	def max (self):
		return self._max
		
	@property
	def min (self):
		return self._min
		
	@property
	def avg (self):
		return self._avg
		
	@property
	def dataset (self):
		return self._dataset
		
	@property
	def npdataset (self):
		return self._npdataset
		
	def draw (self, screen, color):
		assert 0, 'draw is not implemented'

		

	




