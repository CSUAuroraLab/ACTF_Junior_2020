cmake_minimum_required(VERSION 3.10)
project(SoulLike)
#pythonuse里的脚本用于生成中间的一段代码。
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_BUILD_TYPE "release")
set(CMAKE_CXX_FLAGS_RELEASE "$ENV{CXXFLAGS} -o1 -fvisibility=hidden -s -Wall")
add_executable(SoulLike main.cpp)