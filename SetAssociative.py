#!/usr/bin/python
import time
import sys
NUMBER_OF_WAYS = 16

class Cache(object):

	def __init__(self, hex_str):
		self.address = int(hex_str, 16)
		self.ts = time.time()

	def get_offset(self):
		offset = hex(self.address & 0x3F)
		return offset

	def get_set(self):
		set = hex((self.address & 0x40)/0b1000000)
		return set

	def get_tag(self):
		tag = hex((self.address & 0xF80)/0b10000000)
		return tag

	def get_time(self):
		return self.ts

c = Cache("0x108")

print c.get_offset()
print c.get_set()
print c.get_tag()
print c.get_time()
c1 = Cache("0x109")
set0 = [0] * NUMBER_OF_WAYS
set1 = [0] * NUMBER_OF_WAYS

set0[1] = c
set0[2] = c1
print set0[1].get_time()
print set0[1].get_time()
