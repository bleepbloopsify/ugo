from idautils import *
from idc import *
from idaapi import *

print "Hello World!"

ea = BeginEA()

for funcea in Functions(SegStart(ea), SegEnd(ea)):
    print(GetFunctionName(funcea))

