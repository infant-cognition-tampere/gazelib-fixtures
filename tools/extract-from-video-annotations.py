import json
import os
import gazelib

this_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(this_dir)
source_dir = os.path.join(root_dir, 'original-recordings')
source_path = os.path.join(source_dir, 'recording-001-video-annotations.json')
target_dir = os.path.join(root_dir, 'prototypes')
target_path = os.path.join(target_dir, 'trials-features.json')

r = None
with open(source_path, 'r') as jsonfile:
    r = json.load(jsonfile)

def filter_for_srt_and_sd(ev):
    if ev['type'] in ['stimulus-move', 'gaze-saccade-start', 'gaze-saccade-end']:
        if ev['location'] != 'unknown':
            return True
    return False

def get_average_frame(ev):
    return (ev['frame_id_min'] + ev['frame_id_max']) / 2.0

def frame2time(frame):
    return frame * 1000.0 / 120.0

features = []

prev_stimulus_move_min = 0
prev_stimulus_move_max = 0
prev_saccade_start_min = 0
prev_saccade_start_max = 0
for ev in filter(filter_for_srt_and_sd, r['events']):
    if ev['type'] == 'stimulus-move':
        if ev['location'] != 'mid':
            prev_stimulus_move_min = frame2time(ev['frame_id_min'])
            prev_stimulus_move_max = frame2time(ev['frame_id_max'])
    if ev['type'] == 'gaze-saccade-start':
        prev_saccade_start_min = frame2time(ev['frame_id_min'])
        prev_saccade_start_max = frame2time(ev['frame_id_max'])
    if ev['type'] == 'gaze-saccade-end':
        end_min = frame2time(ev['frame_id_min'])
        end_max = frame2time(ev['frame_id_max'])
        features.append({
            'saccadic_reaction_time_ms_min': prev_saccade_start_min - prev_stimulus_move_max,
            'saccadic_reaction_time_ms_max': prev_saccade_start_max - prev_stimulus_move_min,
            'saccade_duration_ms_min': end_min - prev_saccade_start_max,
            'saccade_duration_ms_max': end_max - prev_saccade_start_min
        })

# Add trial ID's
for i, trial in enumerate(features):
    trial['trial_id'] = i

# Write to file
gazelib.write_fancy_json(target_path, features)
