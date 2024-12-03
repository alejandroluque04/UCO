#include <lib.h>
#include "gtest/gtest.h"

// Pruebas para la clase Usuario
TEST(UsuarioTest, SetIpTest) {
    Usuario usuario;
    std::string ip = usuario.GetIP();
    EXPECT_FALSE(ip.empty());  // Asegurarse de que la IP no esté vacía
}

TEST(UsuarioTest, GetNombreTest) {
    Usuario usuario("Usuario_de_prueba");
    EXPECT_EQ(usuario.GetNombre(), "Usuario_de_prueba");
}

TEST(UsuarioTest, SetNombreTest) {
    Usuario usuario;
    usuario.SetNombre("NuevoNombre");
    EXPECT_EQ(usuario.GetNombre(), "NuevoNombre");
}

// Otras pruebas pueden ser agregadas para las clases y funciones restantes
// Asegúrate de cubrir todas las funciones y casos posibles

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
