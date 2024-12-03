cmake_minimum_required(VERSION 3.10)
project(aplicacion)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)
enable_testing()

add_subdirectory(usuario)
add_subdirectory(funciones)
add_subdirectory(programa-main)
