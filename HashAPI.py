import pefile
import os
import sys
from hash import hash1, hash2
# def hash1(inp):
	# s = inp.lower()
	# res = 0
	# for i in range(0, len(s)):
		# p1 = (res << 6) & 0xffffffff
		# p2 = (res << 16) & 0xffffffff
		# res = (p1 + p2 - res + ord(s[i])) & 0xffffffff
	# return res ^ 0x3682A23E

# def hash2(s):
	# res = 0x2326
	# for i in range(0, len(s)):
		# tmp = (res * 65600 - res + ord(s[i])) & 0xffffffff
		# res = tmp
		# tmp = (ord(s[i]) + ((res >> 1) | (res << 7))) & 0xffffffff
		# res += tmp
			
	# return res

dllArray = ["advapi32.dll", "gdi32.dll", "iphlpapi.dll", "kernel32.dll", "nspr4.dll", "ntdll.dll", 
	"ole32.dll", "oleaut32.dll", "shell32.dll", "shlwapi.dll", "urlmon.dll", "user32.dll", "wininet.dll",
	"ws2_32.dll", "bcrypt.dll", "Kernelbase.dll"]

# dllNameHash = []
# apiNameHahs = []	
Uniq = []	

print("enum hashAPI {")
for name in dllArray:
	path = "C:\\Windows\\System32\\" + name
	if not os.path.exists(path): 
		print (path + ' not exist', file=sys.stderr)
		continue
	dll = pefile.PE("C:\\Windows\\System32\\" + name)
	dll.parse_data_directories()
	print ("\t" + name.replace('.', '_').upper() + "_LIBHASH =", hash1(name), ",")
	for entry in dll.DIRECTORY_ENTRY_EXPORT.symbols:
		if entry.name == None: continue
		strName = entry.name.decode("UTF-8")
		# print (strName, file=sys.stderr)
		if strName.lower() in Uniq: continue
		else:
			Uniq.append(strName.lower())
			print ("\t" + strName.upper() + "_HASH =", hash2(strName), ",")
print ("};")			