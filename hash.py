import struct



def hash1(inp):
	# s = inp.lower()
	# res = 0
	# for i in range(0, len(s)):
		# p1 = (res << 6) & 0xffffffff
		# p2 = (res << 16) & 0xffffffff
		# res = (p1 + p2 - res + ord(s[i])) & 0xffffffff
	return hash2(inp)

def hash2(s):
	unicodeString = s.encode('utf-16')
	res = 0xffffffff
	for i in range(0, len(unicodeString)):
		res ^= unicodeString[i]
		for j in range(0,8):
			if (res & 1) != 0:
				res ^= 0x4358ad64
			res >>= 1
		
	return res