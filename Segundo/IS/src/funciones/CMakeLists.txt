add_library(funciones funciones.cc funciones.h)
target_link_libraries(funciones PUBLIC usuario)
target_include_directories(funciones PUBLIC ${CMAKE_CURRENT_LIST_DIR})



