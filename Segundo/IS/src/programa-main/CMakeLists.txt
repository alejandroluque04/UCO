# CMakeLists.txt en la carpeta src/programa-main

# Agregar ejecutable principal (si es necesario)
add_executable(programa-main programa-main.cc)

# Enlazar el ejecutable principal con las bibliotecas necesarias
target_link_libraries(programa-main PUBLIC usuario)
target_link_libraries(programa-main PUBLIC funciones)


