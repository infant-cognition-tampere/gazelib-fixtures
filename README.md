==================
saccade-prototypes
==================

Provides a collection of human gaze recordings to be used for unit testing and algorithm design.


Dataset description
===================

Original recording
------------------

The data has been collected through the following experiment. The participant is asked to follow a white square on a screen. For the first 10 seconds, the square stays still at the center of the screen. The participant stares at the square and blinks his eyes a few times. After the 10 seconds, 12 attention shifting trials were played. With each trial, the square first appears at the middle, and after two seconds, moves to a corner. For the first 4 trials, the participant was asked to follow the square as quickly as possible. For the next 4 trials, the participant was asked to pause the saccade between the center and the corner and then continue to the corner. For the last 4 trials, the participant was asked to do arc-like saccades.

The experiment was recorded with both camera (120 Hz) and eye tracker (300 Hz). The recordings are available under ``original-recording/``. The timing of the events, such as stimulus appearing times and saccade starting times, were extracted from the video manually, resulting the file ``original-recording/recording-001-video-annotations.json``.

More details on the experiment are available under ``docs/``.

Derived prototypes
------------------

14 prototype files were generated from the data:

-  1 fixation at the center without blinks.
-  1 fixation at the center with multiple blinks.
-  4 saccades from the center to a corner.
-  8 cases where the gaze stopped one or more times while moving from the center to a corner.

For each case, the following are provided: a) the tracked gaze points, b) video recording, and c) features extracted from video, such as saccadic reaction times or times of blinks.


Format
======


License
=======

MIT
