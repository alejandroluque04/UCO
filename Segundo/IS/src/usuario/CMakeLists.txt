# CMakeLists.txt en la carpeta src/usuario

# Agregar la biblioteca de usuario
add_library(usuario usuario.cc usuario.h)

# Enlazar la biblioteca de usuario con la biblioteca de funciones
target_link_libraries(usuario PUBLIC funciones)


target_include_directories(usuario PUBLIC ${CMAKE_CURRENT_LIST_DIR})


