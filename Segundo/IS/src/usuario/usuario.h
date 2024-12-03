#ifndef USUARIO_H
#define USUARIO_H

#include <iostream>
#include <stdio.h>
#include <chrono>
#include <ctime>



//para restringir lo que pueden ser facultades
enum class Facultad{
    Educacion,
    Derecho,
    Politecnica,
    Ciencias
};

//para restringir lo que pueden ser carreras
enum class Carrera{
    Ingenieria_Informatica,
    Ingenieria_Mecanica,
    Ingenieria_Electrica,
    Ingenieria_Electronica,
    Matematicas,
    ADE,
    Fisica,
    Quimica
};


/*Clase Usuario*/

class Usuario{

    private:

    static int ip_;
    std::time_t fecha_entrada_;

    std::string correo_;
    std::string password_;
    int rol_;           //1: visitante, 2: alumno, 3: director academico, 4: organizador
    std::string nombre_completo_;
    std::string dni_;
    Facultad facultad_;
    Carrera carrera_;
        

    public:

    Usuario(std::time_t fecha_entrada = std::chrono::system_clock::to_time_t(std::chrono::system_clock::now()))
        : fecha_entrada_(fecha_entrada) {ip_++;}

    ~Usuario(){ip_--;}


    /*Getters*/

    static int GetIp(){return ip_;};

    std::string GetCorreo(){return correo_;}
    int GetRol(){return rol_;}
    std::string GetNombreCompleto(){return nombre_completo_;}
    std::string GetDni(){return dni_;}
    Facultad GetFacultad(){return facultad_;}
    Carrera GetCarrera(){return carrera_;}

    std::string GetFecha();

    /*Setters*/
    void SetCorreo(std::string correo){correo_=correo;}
    void SetPassword(std::string password){password_=password;}
    void SetRol(int rol){rol_=rol;}
    void SetNombreCompleto(std::string nombrecompleto){nombre_completo_=nombrecompleto;}
    void SetDni(std::string dni){dni_=dni;}
    void SetFacultad(Facultad facultad){facultad_=facultad;}
    void SetCarrera(Carrera carrera){carrera_=carrera;}

    /*Otras funciones*/
    void mostrarMenu();
    void opcionMenu();
    void salirMenu();
    bool listarActividadesBasico(int opcion);
    void listarActividadesAvanzado();
    void realizarPreinscripcion();
    void MisActividades();
    void GestionarInscripciones();
    void AdministrarActividades();
    void menuEnvioCorreo();

};


#endif