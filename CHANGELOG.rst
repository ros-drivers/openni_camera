^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package openni_camera
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.9.1 (2014-01-17)
------------------
* add explicit dependency on log4cxx (`#21 <https://github.com/ros-drivers/openni_camera/issues/21>`_)
* Contributors: Jack O'Quin

1.9.0 (2013-06-27 13:39)
------------------------

1.8.9 (2013-06-27 15:14)
------------------------
* Merge pull request `#16 <https://github.com/ros-drivers/openni_camera/issues/16>`_ from forouher/asus-serial
  ASUS xtion: use serial number
* Merge pull request `#17 <https://github.com/ros-drivers/openni_camera/issues/17>`_ from jkammerl/flicker-patch
  another attempt to fix depth image flickering
* access image data via WritableData()
* deep&safe copy of image,ir,depth images
* adding libusb to library target
* workaround: remove some calls that segfault later
  unless this patch is applied, the driver will segfault later
  when querying the prime sense serial id.
  the fact that this patch is necessary is somewhat fishy and
  an indication that the other patches are probably not quite
  correct.
* openni_driver: return prime sense serial id
* Merge pull request `#14 <https://github.com/ros-drivers/openni_camera/issues/14>`_ from stwirth/z_scaling
  Depth scaling parameter
* added depth scaling parameter
* Merge pull request `#12 <https://github.com/ros-drivers/openni_camera/issues/12>`_ from dgossow/groovy-devel
  [bugfix] add exception handling
* fixed typo
* added exception handling for fill*Image
* Merge pull request `#10 <https://github.com/ros-drivers/openni_camera/issues/10>`_ from dgossow/groovy-devel
  [bugfix] Publish reasonable camera info when changing depth resolution.
* Merge pull request `#9 <https://github.com/ros-drivers/openni_camera/issues/9>`_ from jkammerl/groovy-devel
  adding check to make sure dynamic reconfigure has been called before mes...
* [bugfix] Publish reasonable camera info when changing depth resolution.
* adding check to make sure dynamic reconfigure has been called before message generation
* Merge pull request `#8 <https://github.com/ros-drivers/openni_camera/issues/8>`_ from jkammerl/groovy-devel
  fixing late dynamic_reconfigure initialization
* fixing late dynamic_reconfigure initialization
* Contributors: Dariush Forouher, David Gossow, Julius Kammerl, Stephan Wirth, jonbinney

1.8.8 (2013-01-08)
------------------
* switching to 1.8.8
* Contributors: Julius Kammerl

1.8.7 (2013-01-04)
------------------
* fix the export
* Contributors: Vincent Rabaud

1.8.6 (2013-01-03)
------------------
* catkin fixes
* removing stack.xml from groovy-branch
* catkinizing openni_camera
* removing .hgtags
* fixing variable evaluation
* patching cmake to use pkg-config
* new rosdeps

1.8.5
-----
* ignore failure to find image source when using asus pro
* checking error code after enumerating usb devices

1.8.4
-----
* applied stephane's patch for xtion subsampling bug

1.8.3
-----
* applied stephane magnenat's patch to fix subsampling
* claiming ownership
* Export OpenNI include flags for people using the OpenNI wrapper lib.
* Copied over test scripts
* Initial commit of openni_camera as unary stack. Contains the OpenNI wrapper library and new nodelet, but not the deprecated nodelet.
* Contributors: Jonathan Binney, Julius Kammerl, Michael Ferguson, Patrick Mihelich, Tully Foote, jbinney
