import sys
from iotbx import mtz
import iotbx

mtzobj = mtz.object(sys.argv[1])

ref_array = mtzobj.as_miller_arrays()

i_obs = [x for x in ref_array if x.is_xray_amplitude_array()][0]

print("#######################")
print(i_obs.info())
print("#######################")
refls=i_obs.data()

print(len(refls))

#for refl in refls:
    #print(refl)
