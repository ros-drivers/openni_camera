^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package openni_launch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.11.0 (2018-01-13)
-------------------

1.10.0 (2018-01-06)
-------------------
* [maintenance] Repository moved to https://github.com/ros-drivers/openni_camera
* Contributors: Isaac I.Y. Saito

1.9.8 (2016-05-07)
------------------
* [feat] adding depth_registered_filtered injection `#26 <https://github.com/ros-drivers/openni_launch/issues/26>`_
* [sys][Travis CI] Update config to using industrial_ci with Prerelease Test. `#28 <https://github.com/ros-drivers/openni_launch/issues/28>`_
* Contributors: Jonathan Bohren, Isaac I.Y. Saito

1.9.7 (2015-11-15)
------------------
* 1st ROS Jade release
* [sys] Add a simple travis config
* Contributors: Isaac I.Y. Saito

1.9.6 (2015-10-27)
------------------
* [feat] adjust frame ids to TF2
* [fix] Removes the leading '/' from the TF frames in case tf_prefix is empty, which fixes this error:
  [ WARN] [1432284298.914340788]: TF2 exception:
  Invalid argument "/camera_rgb_optical_frame" passed to lookupTransform argument target_frame in tf2 frame_ids cannot start with a '/' like:  (/camera/camera_nodelet_manager)
  Actually, tf_prefix is now ignored altogether.
* Contributors: Jack O'Quin, Jonathan Binney, Martin Günther

1.9.5 (2014-04-18)
------------------
* Test the ROS launch files, fix some errors (`#10
  <https://github.com/ros-drivers/openni_launch/issues/10>`_).
* Fix errors found by roslaunch unit test (`#10
  <https://github.com/ros-drivers/openni_launch/issues/10>`_).
* Add unit tests for launch file dependencies.
* Contributors: Jack O'Quin, jonbinney

1.9.4 (2013-08-25 18:04)
------------------------
* Fix missing run_depend.
* Contributors: Marcus Liebhardt, jonbinney

1.9.3 (2013-08-25 17:49)
------------------------
* Switch to rgbd_launch.
* Added sw_registration and hw_registration flags.
* Modified the top level file to use internal file names.
* device.launch is now internal.
* Added deprecation notice about rgb.launch.
* Deprecation notices about the move of common launch files to rgbd_launch.
* Added tf prefix resolution.
* Contributors: Piyush Khandelwal, jonbinney

1.9.2 (2013-08-01)
------------------
* Fix device registered point cloud generation.
* Disabled unregistered depth and disparity processing when
  depth_registration is set to true.
* Fixing xyzrgb pointcloud generation when device registration is
  enabled.
* Contributors: Piyush Khandelwal, jonbinney

1.9.1 (2013-07-29)
------------------
* Allow proper usage of namespaces for openni's nodes and nodelets.
* Add arguments for switching on/off each processing module.
* Removes (assumed) duplicated depth nodelets include thereby removing
  service registration error.
* Add topic remappings to sort the versious nodelets i/o (i.e. depth, rgb etc.).
* Add option of utilising the worker threads parameter for the nodelet manager.
* Moves nodelet_manager into camera namespace.
* Contributors: Marcus Liebhardt, jonbinney

1.9.0 (2013-06-27)
------------------

1.8.3 (2013-01-03)
------------------
* Catkinizing openni_launch.
* Moved manager setup to manager.launch. Added options load_driver and
  publish_tf for suppressing the driver and/or default tf tree, to
  better support bag file playback and calibration.
* Moved launching of all processing nodelets from device.launch to new
  processing.launch for better reusability, for example bag file
  playback.
* Use 'respawn' arg instead of 'bond' (deprecated). Conforms to
  image_proc and stereo_image_proc launch files, and now attempts to
  respawn loaders when bonds are enabled. Removed rgb.launch, using
  image_proc.launch instead.
* Initial commit of openni_launch as unary stack.
* Contributors: Jonathan Binney, Julius Kammerl, Michael Ferguson, Patrick Mihelich, jbinney
