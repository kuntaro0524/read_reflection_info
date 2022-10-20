import sys
from iotbx import mtz

mtzobj = mtz.object(sys.argv[1])
mtzobj.show_summary()

hkl = mtzobj.extract_miller_indices()
print(len(hkl))

for i in range(0,len(hkl)):
    print(hkl[i])
