cmake_minimum_required(VERSION 2.8)

add_executable(helloworld helloworld.cpp)

find_package(Threads)
add_executable(usespthread usespthread.cpp)
target_link_libraries(usespthread ${CMAKE_THREAD_LIBS_INIT})

ADD_LIBRARY(MyEngineStatic STATIC ./myengine/myengine.cpp)
ADD_LIBRARY(MyEngineDynamic SHARED ./myengine/myengine.cpp)

install(TARGETS MyEngineStatic
	ARCHIVE DESTINATION .
    LIBRARY DESTINATION ../new
    PUBLIC_HEADER DESTINATION ../header )