import ida_hexrays
import idaapi
import idautils
import ida_name

GETPROCADDRESS = 0x1004102C

def rename(funcAddr):
	pseudoCode = str(ida_hexrays.decompile(funcAddr)).split('\n')
	if len([i for i in pseudoCode if 'strcpy' in i]) > 1: return
	newName = next(filter(lambda i: 'strcpy' in i, pseudoCode), None).split('\"')[1]
	ida_name.set_name(funcAddr, 'inv_' + newName)

def autoRename():
	xrefObj = idautils.XrefsTo(GETPROCADDRESS)
	for a in xrefObj:
		funcAddr = idaapi.get_func(a.frm).start_ea
		if funcAddr == None: continue
		rename(funcAddr)