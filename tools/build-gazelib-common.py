'''
Convert original recordings to gazelib/common/v1
'''

import gazelib
from gazelib.conversion.icl.gazelibfixtures import common

trials = '../original-recordings/recording-001-trials.gazedata'
fixation = '../original-recordings/recording-001-fixation.gazedata'
config = '../original-recordings/recording-001-experiment-config.json'

c1 = common.convert(fixation, config, 'mid')
c2 = common.convert(trials, config, 'shift')
c1.save_as_json('../fixtures/fixation-gazepoints.common.json',
                human_readable=True)
c2.save_as_json('../fixtures/trials-gazepoints.common.json',
                human_readable=True)
