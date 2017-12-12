from idaapi import *
from idautils import *
from idc import *

from ugo.structs import add_struct, add_struct_member

# ADD PCLNENTRY STRUCT

class myplugin_t(idaapi.plugin_t):
    flags = idaapi.PLUGIN_UNL
    comment = "This is a comment"

    help = "This is help"
    wanted_name = "My Python plugin"
    wanted_hotkey = "Alt-F8"

    def init(self):
        idaapi.msg("init() called!\n")
        return idaapi.PLUGIN_OK

    def run(self, arg):
        idaapi.msg("run() called with %d!\n" % arg)

    def term(self):
        idaapi.msg("term() called!\n")

def PLUGIN_ENTRY():
    return myplugin_t()

def PLUGIN_ENTRY():

    runtime_pclntab = LocByName("runtime.pclntab")

    sid = add_struct("pclnentry")
    err = add_struct_member(sid, "function", flags=(FF_0OFF | FF_QWORD)) # this is how to do pointers
    err = add_struct_member(sid, "dataOff", flags=(FF_0OFF | FF_QWORD), metadata=runtime_pclntab)

    curr = beginning = runtime_pclntab + 0x20
    pclntab_size = Dword(runtime_pclntab + 0x8)
    print(pclntab_size)

    for i in range(pclntab_size):
        MakeStructEx(curr, -1, "pclnentry")
        curr += 0x10
"""
def MakeStructEx(ea, size, strname):
    \"""
    Convert the current item to a structure instance

    @param ea: linear address
    @param size: structure size in bytes. -1 means that the size
        will be calculated automatically
    @param strname: name of a structure type

    @return: 1-ok, 0-failure
    \"""
    strid = idaapi.get_struc_id(strname)

    if size == -1:
        size = idaapi.get_struc_size(strid)

    return idaapi.doStruct(ea, size, strid)
"""