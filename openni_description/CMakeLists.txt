cmake_minimum_required(VERSION 2.8.3)
project(openni_description)

find_package(catkin REQUIRED)

catkin_package()

install(DIRECTORY model
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/
)
