================
gazelib-fixtures
================

This package contains 14 human gaze recordings to be used for unit testing and algorithm design.

Abbreviations:

- SRT = Saccadic Reaction Time
- SD = Saccade Duration
- C = Center of the screen
- UR = Upper Right corner
- LR = Lower Right corner
- UL = Upper Left corner
- LL = Lower Left corner

Two (2) fixations
=================
We asked the participant to stare at C, recorded the gaze position on screen with an eye tracker, and then selected two representative sets of 1000 sample points.

Samples in fixtures/fixation-gazepoints.\*.json:

-  [0]: fixation of 3.3 sec without blinks

   - 1000 sample points
   - 300 Hz sampling rate
   - 0 invalid sample points

-  [1]: fixation of 3.3 sec with 3 blinks

   - 1000 sample points
   - 300 Hz sampling rate
   - 102 invalid sample points

Twelve (12) saccades
====================
Each saccade sample contains 300 sample points recorded at 300 Hz. At the first sample point a stimulus image was revealed at one of the four corners. After SRT sample points the gaze starts to move and the movement lasts for SD sample points.

Samples in fixtures/trials-gazepoints.\*.json:

- [0]: direct saccade from C to UR
- [1]: direct saccade from C to LR
- [2]: direct saccade from C to LL
- [3]: direct saccade from C to UL
- [4]: multipart saccade from C to UR
- [5]: multipart saccade from C to LR
- [6]: multipart saccade from C to LL
- [7]: multipart saccade from C to UL
- [8]: curved multipart saccade from C to UR
- [9]: curved multipart saccade from C to LR
- [10]: curved multipart saccade from C to LL
- [11]: curved multipart saccade from C to UL

We extracted SRT and SD from a video recording (120 Hz) for each trial. They are available in ``fixtures/trials-features.json``.

File formats
============

The samples come in two formats: pointlist and standard.

\*.pointlist.json
-----------------

A pointlist file is a list of samples. Each sample is a list of points. Each point is a list [x, y]. The x and y are combined average coordinates of both eyes.

Invalid points equal to ``[null, null]``.


\*.standard.json
----------------

A standard file is a list of samples. Each sample is a list of points. Each point is a dictionary with the following keys:

- left_pupil_diam: The diameter of left pupil. Value can be null. Example value: 3.190
- left_x: The horizontal gaze position of the left eye. Relative to screen size. Value can be null. Example value: 0.507
- left_y: The vertical gaze position of the left eye. Relative to screen size. Value can be null. Example value: 0.541
- right_pupil_diam: The diameter of right pupil. Value can be null. Example value: 3.190
- right_x: The horizontal gaze position of the right eye. Relative to screen size. Value can be null. Example value: 0.515
- right_y: Vertical gaze position of the right eye. Value can be null. Example value: 0.549
- time: Sample capture time in microseconds since UNIX epoch. Value cannot be null. Example value: 1448373364122185



Data collection method
======================

The data has been collected through the following experiment. The participant is asked to follow a white square on a screen. For the first 10 seconds, the square stays still at the center of the screen. The participant stares at the square and blinks his eyes a few times. After the 10 seconds, 12 attention shifting trials were played. With each trial, the square first appears at the middle, and after two seconds, moves to a corner. For the first 4 trials, the participant was asked to follow the square as quickly as possible. For the next 4 trials, the participant was asked to pause the saccade between the center and the corner and then continue to the corner. For the last 4 trials, the participant was asked to do arc-like saccades.

Tobii TX300 eye tracker was used to capture the data.

**Detailed description** of the used collection methods can be found at ``docs/method-description.pdf``.


Original recordings
===================

The original recordings are contained in four files:

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



Developer notes
===============

The video files are large. GitHub supports large files if Git Large File Storage is used. Therefore, before ``$ git push``, install Git Large File Storage (git-lfs).


License
=======

MIT
