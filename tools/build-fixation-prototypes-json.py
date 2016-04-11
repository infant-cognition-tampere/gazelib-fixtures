# -*- coding: utf-8 -*-
'''
In this file we pick:
- a fixation without blinks (rows 600-1600)
- a fixation with three blinks (rows 1600-2600)

'''

import os
import gazelib
from lib import *

this_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(this_dir)
source_dir = os.path.join(root_dir, 'original-recordings')
target_dir = os.path.join(root_dir, 'prototypes')

infilename = 'recording-001-fixation.gazedata'
infilepath = os.path.join(source_dir, infilename)

g0 = gazelib.load_csv_as_dictlist(infilepath, delimit='\t')
xs, ys, vals = gazelib.combine_coordinates(g0, ['0', '1'],
       'XGazePosRightEye', 'YGazePosRightEye', 'ValidityRightEye',
       'XGazePosLeftEye', 'YGazePosLeftEye', 'ValidityLeftEye')
g1 = gazelib.add_key(g0, 'comb_x',   list(xs))
g2 = gazelib.add_key(g1, 'comb_y',   list(ys))
g3 = gazelib.add_key(g2, 'comb_val', list(vals))

wout_blinks = g3[600:1600]
with_blinks = g3[1600:2600]

pointlists = [0,0]
pointlists[0] = trial_to_icl_pointlist_v1(wout_blinks)
pointlists[1] = trial_to_icl_pointlist_v1(with_blinks)

standards = [0,0]
standards[0] = trial_to_icl_standard_v1(wout_blinks)
standards[1] = trial_to_icl_standard_v1(with_blinks)

outfilepath = os.path.join(target_dir, 'fixation-gazepoints.pointlist.json')
gazelib.write_fancy_json(outfilepath, pointlists)
outfilepath = os.path.join(target_dir, 'fixation-gazepoints.standard.json')
gazelib.write_fancy_json(outfilepath, standards)
