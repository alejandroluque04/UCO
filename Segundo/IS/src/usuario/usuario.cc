#include "usuario.h"
#include "funciones.h"
#include <vector>
#include <fstream>      //para manejo de ficheros
#include <iostream>
#include <sstream>
#include <string>
#include <chrono>   //para pausa
#include <thread>   //para pausa


int Usuario::ip_=0;



std::string Usuario:: GetFecha(){
    std::string res = std::ctime(&fecha_entrada_);
    if(res[res.length()-1] == '\n'){res[res.length()-1] = '\0';}
    return res;
}



void Usuario::mostrarMenu(){
    std::cout<<"\n \033[1;34mMenu\033[0m\n";
    std::cout<<"1. Listar Actividades\n";

    //si el usuario esta registrado
    if(GetRol()==2 || GetRol()==3 || GetRol()==4){
        std::cout<<"2. Enviar Correo Electrónico\n";
        std::cout<<"3. Realizar Preinscripción\n";
        std::cout<<"4. Mis Actividades\n";

    //si el usuario es director academico o admin
    if(GetRol()==3 || GetRol()==4){
        std::cout<<"5. Gestionar Inscripciones\n";

        //si el usuario es admin
        if(GetRol()==4){
            std::cout<<"6. Administrar Actividades\n";
        }
    }
    }
    std::cout<<"0. Salir\n";
    std::cout<<"\n";
    std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo
    opcionMenu();
}


void Usuario::opcionMenu(){
    int i;
    std::cout<<"\n\033[1;34mSeleccione la opción que desee\033[0m\n";
    if(std::cin>>i){
    }
    else{
        std::cout<<"\033[1;31mERROR, entrada no válida\033[1;31m\n";
        exit(EXIT_FAILURE);
    }

    while(i<0 || i>6){
        std::cout<<"\nIntroduzca una opción válida\n";
        //repetir menu y opcion
        mostrarMenu();
    }
    switch (i){
        case 0:
            std::cout<<"\n";
            salirMenu();
        break;
        case 1:
            std::cout<<"\n";
            listarActividadesAvanzado();
            mostrarMenu();
            break;
        case 2:
            std::cout<<"\n";
            //si ul usuario no está registrado
            if((GetRol())==1){
                std::cout<<"Introduzca una opcion válida\n";
                //repetir menu y opcion
                mostrarMenu();
            }
            menuEnvioCorreo();
            std::cout<<"Opcion sin implementar\n";
            mostrarMenu();
            break;
        case 3:
            std::cout<<"\n";
            //si el usuario no está registrado
            if((GetRol())==1){
                std::cout<<"Introduzca una opcion válida\n";
                //repetir menu y opción
                mostrarMenu();
            }
            realizarPreinscripcion();
            mostrarMenu();
            break;
        case 4:
            std::cout<<"\n";
            //si el usuario no está registrado
            if((GetRol())==1){
                std::cout<<"Introduzca una opcion válida\n";
                //repetir menu y opcion
                mostrarMenu();
            }
            MisActividades();
            mostrarMenu();
            break;
        case 5:
            std::cout<<"\n";
            //si el usuario no es admin o director
            if((GetRol())==1 || GetRol()==2){
                std::cout<<"Introduzca una opción válida\n";
                //repetir menu y opcion
                mostrarMenu();
            }
            else{
                GestionarInscripciones();
                mostrarMenu();
            }
            break;
        case 6:
            std::cout<<"\n";
            //si el usuario no es admin
            if((GetRol())==1 || GetRol()==2 || GetRol()==3){
                std::cout<<"Introduzca una opcion válida\n";
                //repetir menu y opcion
                mostrarMenu();
            }
            else{
                AdministrarActividades();
                mostrarMenu();
            }
            break;
        default:
            std::cout<<"\nIntroduzca una opcion válida\n";
            //repetir menu y opcion
            mostrarMenu();
            break;
    }
}



void Usuario::realizarPreinscripcion(){
    int ret_insc, id;
    int nLinea=-10;
    if(listarActividadesBasico(1)){
        std::cout<<"No hay actividades para mostrar\n";
        mostrarMenu();
    }
    

    std::cout<<"\n\033[1;34mIntroduzca el identificador de la actividad a la que se quiere preinscribir\033[0m\n";
    if(std::cin>>id){
    }
    else{
        std::cout<<"\033[1;31mERROR, entrada no válida\033[1;31m\n";
        exit(EXIT_FAILURE);
    }

    bool encontrado;

    struct act_academica act;
    std::ifstream ListaActividades("ListaActividades.txt");

    fallo_fichero(ListaActividades);



    //mientras que no se alcance el final del fichero, se leen las actividades una a una
    while((leerStrAct(ListaActividades, act))==1){
        //la estructura de actividad tiene 11 campos, por lo que las lineas se leen de 11 en 11
        nLinea+=11;
        if(act.id==id){
            std::cout<<"\n\n\033[1;32mActividad encontrada\033[0m\n";
            std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo
            encontrado=true;
            if(act.estado!=1){
                std::cout<<"\033[1;31mERROR, no se puede hacer la inscripción\033[1;31m\n";
                ListaActividades.close();
                exit(EXIT_FAILURE);
            }
            if(act.plazas_disp>0){
                std::cout<<"\nHay plazas disponibles, realizando preinscripcion\n";
                std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo
                ret_insc=inscripcion(*this, act);
                if(ret_insc==1){
                    ListaActividades.close();
                    //el usuario esta preinscrito
                    if(sustituirStr("ListaActividades.txt", act, nLinea)){
                        std::cout<<"\n\033[1;32mSe han actualizado las plazas disponibles de la actividad\033[0m\n";
                        return;
                    }
                }
                else{
                    ListaActividades.close();
                    //el usuario no se ha preinscrito
                    if(ret_insc==0){
                        std::cout<<"\033[1;31mNo se ha realizado la preinscripción\033[1;31m\n";
                        exit(EXIT_FAILURE);
                    }
                }
            }
            
        }
        
    }

    ListaActividades.close();
    //no se ha encontrado la actividad
    if(!encontrado){
        std::cout<<"\n\033[1;31mNúmero de actividad no válido\033[0m\n\n";
        realizarPreinscripcion();
    }

}


//funcion para listar/enumerar las actividades
bool Usuario::listarActividadesBasico(int opcion){
    struct act_academica act;
    bool vacio=true;
    std::string cad;
    //abro el fichero en el que se encuentran listadas las actividades en modo lectura
    std::ifstream ListaActividades("ListaActividades.txt");

    fallo_fichero(ListaActividades);

    
    //mientras que no se alcance el final del fichero, se leen las actividades una a una
    while((leerStrAct(ListaActividades, act))==1){

        if(opcion==1){
            
            if(act.estado==1 || act.estado==3){
                vacio=false;
                std::cout<<act.id<<". "<<act.nombre<<std::endl;
            }
        }
        else{
            if(opcion==2){
                vacio=false;
                std::cout<<act.id<<". "<<act.nombre<<std::endl;
            }
        }
    }

    ListaActividades.close();
    return vacio;
}


//funcion para listar las actividades con posibilidad de ver los datos de las mismas
void Usuario::listarActividadesAvanzado(){
    int opcion;
    std::string cad;
    char copcion;
    bool encontrado;
    struct act_academica act;

    //llamo a listarActividadesBásico para que muestre el id y el nombre de las actividades
    if(listarActividadesBasico(1)){
        std::cout<<"No hay actividades para mostrar\n";
        return;
    }

    //abro el fichero en el que se encuentran listadas las actividades en modo lectura
    std::ifstream ListaActividades("ListaActividades.txt");

    fallo_fichero(ListaActividades);


    std::cout<<"\n\033[1;34mIndique el id de la actividad que desea ver\033[0m\n";
    if(std::cin>>opcion){
    }
    else{
        std::cout<<"\033[1;31mERROR, entrada no válida\033[1;31m\n";
        exit(EXIT_FAILURE);
    }

    //hay que buscar en ListaActividades la correspondencia con el
    //identificador introducido, y mostrar las caracteristicas de dicha actividad
    while((leerStrAct(ListaActividades, act))==1){

        //si el identificador leido es igual al buscado lee la actividad, y las actividades se encuentran en estado activo o pasadas
        if(opcion==act.id && (act.estado==1 || act.estado==3)){
            encontrado=true;
            std::cout<<"\n\n\033[1;32mSe ha encontrado la actividad\033[0m\n";
            std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo

            //se deben leer las lineas de caracteristicas de la actividad
            std::cout<<"Número de actividad: "<<act.id <<std::endl;
            std::cout<<"Nombre: "<<act.nombre <<std::endl;
            std::cout<<"Descripción: "<<act.descripcion <<std::endl;
            std::cout<<"Aforo: "<<act.aforo <<std::endl;
            std::cout<<"Plazas disponibles: "<<act.plazas_disp<<std::endl;
            std::cout<<"Precio: "<<act.precio <<std::endl;
            std::cout<<"Fecha: "<<act.fecha <<std::endl;
            std::cout<<"Lugar: "<<act.lugar <<std::endl;
            std::cout<<"Director Académico: "<<act.director_academico <<std::endl;
            std::cout<<"Ponente: "<<act.ponente <<std::endl;
            switch(act.estado){
                case 1:
                    std::cout<<"Estado: Activa"<<std::endl;
                break;
                case 2:
                    std::cout<<"Estado: No Activa"<<std::endl;
                break;
                case 3:
                    std::cout<<"Estado: Caducada"<<std::endl;
                break;
            }
        }
    }

    if(!encontrado){
        std::cout<<"\nNo se ha encontrado la actividad\n";
        ListaActividades.close();
        return;
    }

    std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo
    std::cout<<"\n\n¿Quiere ver otra actividad? (y/n)\n";
    //se duplica ya que lee una \n residual
    std::getline(std::cin, cad);
    std::getline(std::cin, cad);

    if(cad.length()==1){
        copcion=cad[0];
    }
    else{
        copcion='x';
    }
    if(cad==""){
        copcion='x';
    }

    //compruebo que se ha introducido en copcion uno de los carácteres correctos
    while(copcion!='Y' && copcion!= 'y' && copcion!= 'N' && copcion!='n'){
        std::cout<<"\nOpcion no válida\n";
        std::cout<<"\n¿Quiere ver otra actividad? (y/n)\n";
        std::getline(std::cin, cad);

        if(cad.length()==1){
            copcion=cad[0];
        }
        else{
            copcion='x';
        }
        if(cad==""){
            copcion='x';
        }
    }

    if(copcion=='y' || copcion== 'Y'){
        ListaActividades.close();
        listarActividadesAvanzado();
    }
    else{
        ListaActividades.close();
    }
}


//funcion que servirá para salir del programa. Pregunta al usuario si quiere salir antes de cerrar
void Usuario::salirMenu(){
    std::string cad;
    char opcion;
    std::cout<<"\n¿Está seguro de querer salir? (y/n)\n";
    //hay que duplicar el getline ya que lee un \n residual
    std::getline(std::cin,cad);
    std::getline(std::cin,cad);

    if(cad.length()==1){
        opcion=cad[0];
    }

    else{
        opcion='x';
    }
    if(cad==""){
        opcion='x';
    }

    while(opcion!='Y' && opcion!= 'y' && opcion!= 'N' && opcion!='n'){
        std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo
        std::cout<<"\n\033[1;31mOpcion no válida\033[0m\n";
        std::cout<<"\n¿Está seguro de querer salir? (y/n)\n";
        std::getline(std::cin, cad);

        if(cad.length()==1){
            opcion=cad[0];
        }
        else{
            opcion='x';
        }
        if(cad==""){
            opcion='x';
        }
    }

    if(opcion=='y' || opcion== 'Y'){
        exit(EXIT_SUCCESS);
    }

    if(opcion=='N' || opcion=='n'){
        mostrarMenu();
    }
}



void Usuario::AdministrarActividades(){
    int opcion=menu_admin_act();
    switch(opcion){
        case 1:
            crear_Actividad();
            break;
        case 2:
            editar_Actividad(*this);
            break;
        case 3:
            eliminar_Actividad(*this);
        break;
    }

}



void Usuario::GestionarInscripciones(){
    int opcion, alumno, accion, nLinea=1, linea_act, linea_al, numeroLinea=-10, cont=0;
    std::vector <int> ocupados;
    std::string cad, cad2, dni, estado;
    bool encontrado=false, hayEspacio=false;
    if(listarActividadesBasico(1)){
        std::cout<<"No hay actividades\n";
        mostrarMenu();
    }
    std::cout<<"\n\033[1;34mIntroduzca la actividad para ver los inscritos\033[0m\n";
    
    if(std::cin>>opcion){
    }
    else{
        std::cout<<"\033[1;31mERROR, entrada no válida\033[1;31m\n";
        exit(EXIT_FAILURE);
    }

    std::ifstream ListaInscripciones("Inscripciones.txt");

    fallo_fichero(ListaInscripciones);



    std::ifstream ListaActividades("ListaActividades.txt");
    struct act_academica act;

    fallo_fichero(ListaActividades);

    //para saber en que linea empieza la actividad
    while((leerStrAct(ListaActividades, act))==1){
        numeroLinea+=11;
        if(act.id==opcion){
            break;
        }
    }
    ListaActividades.close();




    //hay que recorrer el fichero hasta encontrar la actividad
    while(std::getline(ListaInscripciones, cad)){
        hayEspacio = false;
        nLinea++;
        for (char c : cad) {
            if (std::isspace(c)) {
                hayEspacio = true;
                break;
            }
        }

        //comprobamos que en cad hay el id de una actividad, para hacer stoi, sino, falla
        if(!hayEspacio && cad!=""){
            //hemos leido la id de una actividad, comprobamos si es la que estamos buscando
            if(opcion==std::stoi(cad)){
                //almaceno el numero de linea del id de la actividad
                linea_act=nLinea-1;
                encontrado=true;
                std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo
                std::cout<<"\n\033[1;32mSe ha encontrado la actividad\033[0m\n";

                for(int i=1; i<=act.aforo; i++){
                    nLinea++;
                    std::getline(ListaInscripciones, cad2);
                    hayEspacio=false;
                    
                    for (char c : cad2) {
                        if (std::isspace(c)) {
                            hayEspacio = true;
                            break;
                        }
                    }

                    if(hayEspacio){
                        //estamos  leyendo una linea donde hay alguien inscrito
                        cont++;
                        ocupados.push_back(nLinea-1);
                        // Usar std::istringstream para dividir la cadena
                        
                        std::istringstream stream(cad2);
    
                        stream >> dni;
                        stream >> estado;

                        //se leen el DNI y el tipo de inscripcion de cada inscripcion de la actividad
                        std::cout<<cont<<". DNI: "<<dni<<"\nEstado: ";
                        switch(std::stoi(estado)){
                            case 1:
                                std::cout<<"Preinscrito\n\n";
                                break;
                            case 2:
                                std::cout<<"Inscrito\n\n";
                                break;
                            default:
                                std::cout<<"Estado no válido\n\n";
                                break;
                        }
                    }
                }


                std::cout<<"\n\033[1;34mIntroduzca el nº de la persona sobre la que quiere actuar\033[0m\n";
                if(std::cin>>alumno){
                    if(alumno>0 && alumno<=cont){
                        std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo
                    }
                    else{
                        std::cout<<"\033[1;31mEl numero introducido no corresponde a ningun usuario inscrito\033[0m\n\n";
                        ListaInscripciones.close();
                        mostrarMenu();
                    }
                }
                else{
                    std::cout<<"\033[1;31mERROR, entrada no válida\033[1;31m\n";
                    ListaInscripciones.close();
                    exit(EXIT_FAILURE);
                }

                //almaceno la linea en la que esta la inscripcion que queremos modificar
                linea_al=ocupados[alumno-1];

                std::cout<<"\n\033[1;34mSi quiere eliminar la inscripcion de esta persona introduzca 1\n";
                std::cout<<"Si quiere pasar de preinscrito a inscrito a esta persona introduzca 2\033[0m\n";

                if(std::cin>>accion){
                }
                else{
                    std::cout<<"\033[1;31mERROR, entrada no válida\033[1;31m\n";
                    ListaInscripciones.close();
                    exit(EXIT_FAILURE);
                }
                
                switch(accion){
                    case 1:
                        //se va a borrar la inscripcion
                        if(sustituirStrInsc(*this, linea_al, 2)){
                            std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo
                            std::cout<<"\n\033[1;32mSe ha eliminado la preinscripcion correctamente\033[0m\n";
                            act.plazas_disp++;
                            //cerramos fichero
                            ListaInscripciones.close();
                            if(sustituirStr("ListaActividades.txt", act, numeroLinea)){  
                                std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo  
                                std::cout<<"\nSe ha sumado 1 a las plazas disponibles de la actividad\n";
                                return;
                            }
                            return;
                        }
                        break;
                    case 2:
                        if(estado=="1"){
                            //se va a pasar de preinscrito a inscrito
                            if(sustituirStrInsc(*this, linea_al, 3)){
                                std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo
                                std::cout<<"\n\033[1;32mSe ha pasado a inscrito correctamente\033[0m\n";
                                ListaInscripciones.close();
                                return;
                            }
                        }
                        else{
                            if(estado=="2"){
                                std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo
                                std::cout<<"\nYa esta inscrito\n";
                                ListaInscripciones.close();
                                return;    
                            }
                            std::cout<<"\033[1;31mOpcion no válida\033[0m\n";
                            ListaInscripciones.close();
                            return;
                        }
                        break;
                    default:
                        std::cout<<"\033[1;31mOpcion no válida\033[0m\n";
                        ListaInscripciones.close();
                        return;
                        break;
                }
                
                std::cout<<"No hay inscripciones en esta actividad\n";
                return;
            }
        }
    }
    std::cout<<"No se ha encontrado la actividad\n";
    ListaInscripciones.close();
}



void Usuario::MisActividades(){
    std::cout<<"1. Ver mis inscripciones\n";
    std::cout<<"2. Eliminar inscripcion\n";
    
    int opcion;
    std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo
    std::cout<<"Introduzca la opción que desee\n";
    if(std::cin>>opcion){
    }
    else{
        std::cout<<"\033[1;31mERROR, entrada no válida\033[1;31m\n";
        exit(EXIT_FAILURE);
    }

    switch(opcion){
        case 1:
            verMisActividades(*this);
            break;
        case 2:
            eliminarInscripcion(*this);
            break;
        default:
            std::cout<<"\033[1;31mOpcion no válida\033[0m\n";
            MisActividades();
    }

}


void Usuario::menuEnvioCorreo(){
    std::cout<<"\n \033[1;34mIntroduzca la opción que desee\033[0m\n";
    std::cout<<"1. Enviar correo\n";
    if(GetRol()==3 || GetRol()==4){
        std::cout<<"2. Hacer difusión\n";
    }
    int opcion;

    if(std::cin>>opcion){
    }
    else{
        std::cout<<"\033[1;31mERROR, entrada no válida\033[1;31m\n";
        exit(EXIT_FAILURE);
    }

    switch(opcion){
        case 1:
            enviarCorreo(*this);
            mostrarMenu();
            break;
        case 2:
            if(GetRol()==3 || GetRol()==4){
                difusion(*this);
                mostrarMenu();
            }
            else{
                std::cout<<"\033[1;31mOpción no válida\033[0m\n";
                mostrarMenu();
            }
            break;
        default:
            std::cout<<"\033[1;31mOpción no válida\033[0m\n";
            mostrarMenu();
            break;
    }
}