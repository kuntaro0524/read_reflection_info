import sys
from iotbx import mtz
from iotbx.reflection_file_reader import any_reflection_file


#hkl_in = any_reflection_file(file_name="test.mtz")
#miller_arrays = hkl_in.as_miller_arrays()



mtzobj = mtz.object(sys.argv[1])
mtzobj.show_summary()
#hkl = mtzobj.extract_miller_indices()
#mil = mtzobj.as_miller_arrays()

#i_obs = miller_arrays[0]
mtzobj.amplitude()
#print(i_obs.show_summary())

