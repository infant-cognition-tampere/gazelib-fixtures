# -*- coding: utf-8 -*-
'''
Helper functions
'''

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

def trial_to_icl_pointlist_v1(trial):
    return list(map(gazepoint_to_icl_pointlist_v1, trial))

def trial_to_icl_standard_v1(trial):
    return list(map(gazepoint_to_icl_standard_v1, trial))
