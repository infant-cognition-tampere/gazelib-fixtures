'''
We use this file as an ad-hoc tool to visualize gazedata.

'''

import os
import gazelib
import bokeh.plotting as plotting


this_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(this_dir)
source_dir = os.path.join(root_dir, 'original-recordings')
filename = os.path.join(source_dir, 'recording-001-fixation.gazedata')

g0 = gazelib.load_csv_as_dictlist(filename, delimit='\t')
xs, ys, vals = gazelib.combine_coordinates(g0, ['0', '1'],
       'LeftEyePupilDiameter', 'YGazePosRightEye', 'ValidityRightEye',
       'RightEyePupilDiameter', 'YGazePosLeftEye', 'ValidityLeftEye')

#g1 = gazelib.add_key(g0, 'comb_x',   list(xs))
#g2 = gazelib.add_key(g1, 'comb_y',   list(ys))
#g3 = gazelib.add_key(g2, 'comb_val', list(vals))
#g4 = gazelib.interpolate_using_last_good_value(g3, 'comb_x', 'comb_val', ['0', '1'])
#g5 = gazelib.interpolate_using_last_good_value(g4, 'comb_y', 'comb_val', ['0', '1'])
#g6 = gazelib.median_filter_data(g5, 7, 'comb_x')
#g7 = gazelib.median_filter_data(g6, 7, 'comb_y')
#g8 = gazelib.gazepoints_containing_value(g3, 'tag', ['Target'])
#g9 = gazelib.split_at_change_in_value(g8, 'trialnumber')
#g10 = list(map(lambda trial: gazelib.first_gazepoints(trial, 1000), g9))
#g6 = g5[600:2500]
#print(len(g5))
x = list(map(float, xs))
xs0 = list(range(0, len(x)))  # gazelib.get_key(, 'comb_x')
ys0 = x  # gazelib.get_key(g1, 'comb_x')
print(len(xs0))
print(len(ys0))

title = 'Fixation'

p = plotting.figure(title=title, x_axis_label='sample #', y_axis_label='pupils\' diameter')
p.cross(xs0, ys0, size=10)
p.line(xs0, ys0, line_width=1)

plotting.output_file('index.html', title)
plotting.save(p)
