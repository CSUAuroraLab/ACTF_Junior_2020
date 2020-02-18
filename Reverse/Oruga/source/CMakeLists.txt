cmake_minimum_required(VERSION 3.10)
project(oruga)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_BUILD_TYPE "release")
set(CMAKE_CXX_FLAGS_RELEASE "$ENV{CXXFLAGS} -o3 -fvisibility=hidden -s -Wall")
add_executable(oruga main.cpp)