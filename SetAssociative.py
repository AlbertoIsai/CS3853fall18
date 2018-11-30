#!/usr/bin/python
from datetime import datetime
import sys
import operator
NUMBER_OF_WAYS = 16

class Cache(object):

	def __init__(self, hex_str):
		self.address = int(hex_str, 16)
		tsm = datetime.now()
		self.ts = tsm.microsecond
		self.tag = (self.address & 0xF80)/0b10000000

	def get_offset(self):
		offset = self.address & 0x3F
		return offset

	def get_set(self):
		set = (self.address & 0x40)/0b1000000
		return set

	def get_tag(self):
		return self.tag

	def get_time(self):
		return self.ts

fh = open(sys.argv[1], "r")
for line in fh:
	fields = line.strip().split()
	c = Cache(fields[2])
	set0 = []
	set1 = []
	tagMatch = False
	tagIndex = 0
	hit = 0.00
	miss = 0.00
	total = 0.00
	missRate = 0.00
	y = 0
	z = 0
	if c.get_set() == 0:
		if not set0:
			set0.insert(0, c)
			miss += 1
			y += 1
		for x in range(y):
			current_tag = set0[x].get_tag()
			if c.get_tag() == current_tag:
				tagMatch = True
				tagIndex = x
				break
			else:
				tagMatch = False

		if tagMatch == True:
			set0.insert(tagIndex, c)
			set0.sort(key=operator.attrgetter('ts'))
			hit += 1
		else:
			set0.sort(key=operator.attrgetter('ts'))
			set0.insert(0, c)
			miss += 1
		if y < NUMBER_OF_WAYS:
			y += 1
	else: #set = 1
		if not set1:
			set1.insert(0, c)
			miss += 1
			z += 1
		for x in range(z):
			current_tag = set1[x].get_tag()
			if c.get_tag() == current_tag:
				tagMatch = True
				tagIndex = x
				break
			else:
				tagMatch = False

		if tagMatch == True:
			set1.insert(tagIndex, c)
			set1.sort(key=operator.attrgetter('ts'))
			hit += 1
		else:
			set1.sort(key=operator.attrgetter('ts'))
			set1.insert(0, c)
			miss += 1
		if z < NUMBER_OF_WAYS:
			z += 1
total = hit + miss

missRate = (miss / total) * 1.0

print float(missRate)
