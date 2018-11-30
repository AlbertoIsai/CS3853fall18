#!/usr/bin/python
from datetime import datetime
import sys
import operator
NUMBER_OF_WAYS = 16

class Cache(object):

	def __init__(self, hex_str):
		self.address = int(hex_str, 16)
		tsm = datetime.now()
		self.ts = tsm.second *1000 + tsm.microsecond
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
hit = 0.00
miss = 0.00
total = 0.00
missRate = 0.00
set0 = []
set1 = []
set0Full = False
set1Full = False
fh = open(sys.argv[1], "r")
for line in fh:
	fields = line.strip().split()
	c = Cache(fields[2])

	tagMatch = False
	tagIndex = 0


	if c.get_set() == 0:
		if not set0:
			set0.insert(0, c)
			miss += 1
		else:
			for x in range(0, len(set0)):
				current_tag = set0[int(x)].get_tag()
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
			elif not set0Full:
				set0.sort(key=operator.attrgetter('ts'))
				set0.insert(0, c)
				miss += 1
			else:
				set0.sort(key=operator.attrgetter('ts'))
				set0.pop(0)
				set0.append(c)
				miss += 1

			if len(set0) == NUMBER_OF_WAYS:
				set0Full = True
	else: #set = 1
		if not set1:
			set1.insert(0, c)
			miss += 1
		else:
			for x in range(0, len(set1)):
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
			elif not set1Full:
				set1.sort(key=operator.attrgetter('ts'))
				set1.insert(0, c)
				miss += 1
			else :
				set1.sort(key=operator.attrgetter('ts'))
				set1.pop(0)
				set1.append(c)
				miss += 1

			if len(set1) == NUMBER_OF_WAYS:
				set1Full = True
total = hit + miss

missRate = (miss / total) * 1.0

print("Cache miss rate: %.2f%%" % float(missRate*100.0))
