==================
saccade-prototypes
==================

Provides a collection of human gaze recordings to be used for unit testing and algorithm design.


Dataset description
===================

The set contains 14

Original recording
------------------

The original recording contains four files:

- original-recordings/recording-001-fixation.gazedata
- original-recordings/recording-001-trials.gazedata
- original-recordings/recording-001-video-annotations.json
- original-recordings/recording-001-video-diff-enhanced.mp4

The gazedata files are tab-separated-values files with following columns:

- LeftEyePosition3dRelativeX
- LeftEyePosition3dRelativeY
- LeftEyePosition3dRelativeZ
- LeftEyePosition3dX
- LeftEyePosition3dY
- LeftEyePosition3dZ
- XGazePosLeftEye: Relative horizontal position on the screen
- YGazePosLeftEye: Relative vertical position on the screen
- LeftEyePupilDiameter
- ValidityLeftEye: Tobii validity for eye recognition, 0 = perfect, 1 = good
- RightEyePosition3dRelativeX
- RightEyePosition3dRelative
- RightEyePosition3dRelativeZ
- RightEyePosition3dX
- RightEyePosition3dY
- RightEyePosition3dZ
- XGazePosRightEye
- YGazePosRightEye
- RightEyePupilDiameter
- ValidityRightEye
- TETTime: UNIX timestamp in microseconds
- stim: ID of stimulus
- aoi: Location ID of stimulus
- tag: Phase of trial, Wait = image at center, Target = image at corner
- trialnumber: Sequence number of trial, starts from 0
- starttime: Phase start UNIX timestamp in microseconds
- aoi_coord: Relative coordinates of stimulus location
- endtime: Phase end UNIX timestamp in microseconds


The data has been collected through the following experiment. The participant is asked to follow a white square on a screen. For the first 10 seconds, the square stays still at the center of the screen. The participant stares at the square and blinks his eyes a few times. After the 10 seconds, 12 attention shifting trials were played. With each trial, the square first appears at the middle, and after two seconds, moves to a corner. For the first 4 trials, the participant was asked to follow the square as quickly as possible. For the next 4 trials, the participant was asked to pause the saccade between the center and the corner and then continue to the corner. For the last 4 trials, the participant was asked to do arc-like saccades.

The experiment was recorded with both camera (120 Hz) and eye tracker (300 Hz). The recordings are available under ``original-recording/``. The timing of the events, such as stimulus appearing times and saccade starting times, were extracted from the video manually, resulting the file ``original-recording/recording-001-video-annotations.json``.

More details on the experiment are available under ``docs/``.

Derived prototypes
------------------

13 prototype files were generated from the data:

-  1 fixation at the center without blinks.
-  1 fixation at the center with multiple blinks.
-  4 saccades from the center to a corner.
-  8 cases where the gaze stopped one or more times while moving from the center to a corner.

For each case, the following are provided: a) the tracked gaze points, b) video recording, and c) features extracted from video, such as saccadic reaction times or times of blinks.


Format
======



Developer notes
===============

Before ``$ git push``, install Git Large File Storage (git-lfs).


License
=======

MIT
