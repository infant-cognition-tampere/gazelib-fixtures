# -*- coding: utf-8 -*-
import gazelib

gp = gazelib.load_json('fixtures/fixation-gazepoints.pointlist.json')

# Select fixation #1
fixation = gp[1]

# Select invalid
is_invalid = lambda x: (x[0] == None or x[1] == None)
invs = filter(is_invalid, fixation)

# Number of invalids
print(len(invs))
