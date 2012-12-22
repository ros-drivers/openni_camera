cmake_minimum_required(VERSION 2.4.6)
include($ENV{ROS_ROOT}/core/rosbuild/rosbuild.cmake)

set(ROS_BUILD_TYPE RelWithDebInfo)
rosbuild_init()
rosbuild_make_distribution(1.8.5)

include(FindPkgConfig)

pkg_check_modules(OPENNI libopenni)

#message("Hello world ${OPENNI_LIBRARIES} ${OPENNI_INCLUDEDIR}")

set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)

# Dynamic reconfigure
rosbuild_find_ros_package(dynamic_reconfigure)
include(${dynamic_reconfigure_PACKAGE_PATH}/cmake/cfgbuild.cmake)
gencfg()

rosbuild_add_boost_directories()
include_directories(OPENNI_INCLUDEDIR)

# OpenNI Driver standalone library
rosbuild_add_library(openni_driver src/openni_driver.cpp
                                   src/openni_device.cpp
                                   src/openni_exception.cpp
                                   src/openni_device_primesense.cpp
                                   src/openni_device_kinect.cpp
                                   src/openni_device_xtion.cpp
                                   src/openni_device_oni.cpp
                                   src/openni_image_yuv_422.cpp
                                   src/openni_image_bayer_grbg.cpp
                                   src/openni_image_rgb24.cpp
                                   src/openni_ir_image.cpp
                                   src/openni_depth_image.cpp
                     )
target_link_libraries(openni_driver OPENNI_LIBRARIES)

# ROS nodelets library
rosbuild_add_library(openni_nodelet src/nodelets/driver.cpp)
target_link_libraries(openni_nodelet openni_driver)

# Node version of ROS driver
rosbuild_add_executable(openni_node src/nodes/openni_node.cpp)
