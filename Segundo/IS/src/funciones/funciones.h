#ifndef FUNCIONES_H
#define FUNCIONES_H

#include "usuario.h"
#include <iostream>
#include <stdio.h>
#include <chrono>
#include <ctime>
#include <string>
#include <fstream> //para manejo de ficheros  

//HAY QUE AÑADIR LAS FUNCIONES DE CLASE A SU CLASE

struct act_academica{
    int id;
    std::string nombre;
    std::string descripcion;
    int aforo;
    int plazas_disp;
    float precio;
    std::string fecha;
    std::string lugar;
    std::string director_academico;
    std::string ponente;
    int estado = 0;
};


struct usuario1{
    std::string correo;
    std::string password;
    int rol;
    std::string nombre_completo;
    std::string dni;
    Facultad facultad;
    Carrera carrera;
};



void menu_inicio_sesion(Usuario &user);
void opc_menu_inicio_sesion(Usuario &user);
void pedirCredenciales(Usuario &user);
void repetirEleccion(Usuario &user);
int menu_admin_act();
void crear_Actividad();
bool comprobar_director(struct act_academica actividad);
bool comprobar_correo(std::string correo);
int leerStrUser(std::ifstream &fichero, struct usuario1 &u1);
int leerStrAct(std::ifstream &ListaActividades, struct act_academica &act);
bool sustituirStr(std::string nombrearchivo, struct act_academica &actividad, int numeroLinea);
void editar_Actividad(Usuario &user);
int inscripcion(Usuario &user, struct act_academica &act);
bool sustituirStrInsc(Usuario &user, int numeroLinea, int opcion);
void verMisActividades(Usuario &user);
void eliminar_Actividad(Usuario &user);
bool borrar(int numeroLinea, std::string nombreArchivo, int borrarLineas);
void eliminarInscripcion(Usuario &user);
void fallo_fichero(std::ifstream &fichero);
void fallo_fichero(std::ofstream &fichero);
void enviarCorreo(Usuario &user);
void difusion(Usuario &user);
void difusion_facultad(Usuario &user);
void difusion_carrera(Usuario &user);



#endif