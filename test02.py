import sys
from iotbx import mtz
from cctbx.array_family import flex
import iotbx

#Read the 1st mtz file
mtz1 = mtz.object(sys.argv[1])

#Read the 2nd mtz file
mtz2 = mtz.object(sys.argv[2])

#Extract miller arrays by using cctbx
refl1_ = mtz1.as_miller_arrays()
refl2_ = mtz2.as_miller_arrays()


ref1 = [x for x in refl1_ if x.is_xray_amplitude_array()][0]
ref2 = [x for x in refl2_ if x.is_xray_amplitude_array()][0]

print(ref1.info())
print(ref2.info())

# Common reflections
com1,com2 = ref1.common_sets(ref2)

# Binner
binner = com1.setup_binner(n_bins=10)

for i_bin in binner.range_used():
    sel1 = com1.select(binner.bin_indices()==i_bin)
    sel2 = com2.select(binner.bin_indices()==i_bin)
    assert len(sel1.data())==len(sel2.data())

    # The lowest & highest resolution limit of this bin.
    low = binner.bin_d_range(i_bin)[0]
    high = binner.bin_d_range(i_bin)[1]

    # mean value of the amplitude difference the designated shell
    difff = flex.mean(sel1.data()-sel2.data()) / sel1.size()
    print("%8.2f - %8.2f %12.5e" % (low, high, difff))
