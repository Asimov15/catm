#!/usr/bin/python
# Polybius 20/11/2017
# cellular automata turing machine.

import sys
import math

class automata():
	def __init__(self, r, n1, n2):
		self.length     = 1024
		self.linea      = []
		self.lineb      = []
		self.rule       = r
		self.rule_truth = []
		self.num1       = n1
		self.num2       = n2
		self.stepnum    = 0
						
		# create array based on rule and reverse order Wolfram has defined his rules this way.	
		# ie format in big endian	
		for i in '{0:08b}'.format(self.rule)[::-1]: 
			if i == "0":
				self.rule_truth.append(0)
			else:
				self.rule_truth.append(1)
				
		for i in range(self.length):
			self.linea.append(0)
			self.lineb.append(0)
		
		# seed with the two numbers you wish to add
		j = 0
		for i in '{0:08b}'.format(n1): 			
			if i == "1":
				self.linea[self.length / 2 - 8 + j] = 1
			j += 1
		
		j = 0
		for i in '{0:08b}'.format(n2): 			
			if i == "1":
				self.linea[self.length / 2 + j] = 1		
			j += 1
	
	def output(self):		
		for x in self.linea:			
			if x == 1:
				sys.stdout.write(u'\u2588')
				sys.stdout.flush()
			else:
				sys.stdout.write(" ")
				sys.stdout.flush()
	
	def get_cell(self,i):
		
		#wrapper function for getting pixel to handle the boundary.		
		boundary_value = 0
		if i < 0 or i >= len(self.linea):
			return int(boundary_value)
		else:
			return int(self.linea[i])
	
	def get_input(self,i):
		
		# get the value of the the three pixels above this pixel		
		x = 0
		for j in range(-1,2):
			x = x + self.get_cell(i+j) * math.pow(2, 1-j)			
						
		return int(x)
			
	def step(self):
		
		# calculate next line
		for i in range(self.length):
			self.lineb[i] = self.rule_truth[self.get_input(i)]	
		
		for i in range(self.length):
			self.linea[i] = self.lineb[i]	
	
	def run(self,n):
		
		# perform the automata for n iterations
		self.output()
		print
		for i in range(int(n)):
			self.step()			
			self.find_sol()
			self.stepnum += 1
			if i % 100000 == 0:
				print i
			
	def find_sol(self):
		
		# search for the answer in output		
		for x in range(self.length - 8):
			answer = 0
			for y in range(8):
				 answer = answer + self.linea[x+y] * math.pow(2, 7-y)
			#if answer > 0:
			#	print answer
			#print answer 
			if answer == num1 + num2:
				print "found it!!!!"
				print self.stepnum, x

seed = []

num1 = 101
num2 = 109
	
a = automata(110, num1, num2)
print a.rule_truth

a.run( int(1e6) )
	

