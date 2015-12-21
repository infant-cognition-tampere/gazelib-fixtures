import os
import gazelib

this_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(this_dir)
source_dir = os.path.join(root_dir, 'original-recordings')
target_dir = os.path.join(root_dir, 'prototypes')

infilename = 'recording-001-trials.gazedata'
infilepath = os.path.join(source_dir, infilename)

g0 = gazelib.load_csv_as_dictlist(infilepath, delimit='\t')
xs, ys, vals = gazelib.combine_coordinates(g0, ['0', '1'],
       'XGazePosRightEye', 'YGazePosRightEye', 'ValidityRightEye',
       'XGazePosLeftEye', 'YGazePosLeftEye', 'ValidityLeftEye')
g1 = gazelib.add_key(g0, 'comb_x',   list(xs))
g2 = gazelib.add_key(g1, 'comb_y',   list(ys))
g3 = gazelib.add_key(g2, 'comb_val', list(vals))

g4 = gazelib.gazepoints_containing_value(g3, 'tag', ['Target'])
g5 = gazelib.split_at_change_in_value(g4, 'trialnumber')
g6 = list(map(lambda trial: gazelib.first_gazepoints(trial, 300), g5))

def get_value_or_none(value):
    value = float(value)
    if value == -1.0:
        return None
    return value

def gazepoint_to_icl_pointlist_v1(gp):
    x = get_value_or_none(gp['comb_x'])
    y = get_value_or_none(gp['comb_y'])
    return [x, y]

def gazepoint_to_icl_cyclops_v1(gp):
    return {
        'x': get_value_or_none(gp['comb_x']),
        'y': get_value_or_none(gp['comb_y']),
        'time': int(gp['TETTime'])
    }

def gazepoint_to_icl_standard_v1(gp):
    return {
        'left_x': get_value_or_none(gp['XGazePosLeftEye']),
        'left_y': get_value_or_none(gp['YGazePosLeftEye']),
        'left_pupil_diam': get_value_or_none(gp['LeftEyePupilDiameter']),
        'right_x': get_value_or_none(gp['XGazePosRightEye']),
        'right_y': get_value_or_none(gp['YGazePosRightEye']),
        'right_pupil_diam': get_value_or_none(gp['LeftEyePupilDiameter']),
        'time': int(gp['TETTime'])
    }

def get_outfilepath(trial_index, fileformat):
    filename = ('trial-' + str(trial_index).zfill(3) + ''
               '.' + fileformat + '.json')
    return os.path.join(target_dir, filename)

def trial_to_icl_pointlist_v1(trial):
    return list(map(gazepoint_to_icl_pointlist_v1, trial))

def trial_to_icl_standard_v1(trial):
    return list(map(gazepoint_to_icl_standard_v1, trial))

pointlists = list(map(trial_to_icl_pointlist_v1, g6))
outfilepath = os.path.join(target_dir, 'trials-gazepoints.pointlist.json')
gazelib.write_fancy_json(outfilepath, pointlists)

standards = list(map(trial_to_icl_standard_v1, g6))
outfilepath = os.path.join(target_dir, 'trials-gazepoints.standard.json')
gazelib.write_fancy_json(outfilepath, standards)

#for i, trial in enumerate(g6):
#    pointlist_trial = list(map(gazepoint_to_icl_pointlist_v1, trial))
#    #cyclops_trial = list(map(gazepoint_to_icl_cyclops_v1, trial))
#    #standard_trial = list(map(gazepoint_to_icl_standard_v1, trial))

#    gazelib.write_fancy_json(get_outfilepath(i, 'pointlist'), pointlist_trial)
#    #gazelib.write_fancy_json(get_outfilepath(i, 'cyclops'), cyclops_trial)
#    gazelib.write_fancy_json(get_outfilepath(i, 'standard'), standard_trial)



# xs0 = gazelib.get_key(g10[0], 'comb_x')
# ys0 = gazelib.get_key(g10[0], 'comb_y')
# print(xs0)
# p = plotting.figure(title="Trial 0", x_axis_label='x', y_axis_label='y')
# p.line(xs0, ys0, line_width=2)
# plotting.output_file('index.html', 'Trial 0')
# plotting.save(p)
