#include "funciones.h"
#include "usuario.h"
#include <vector>
#include <fstream>      //para manejo de ficheros
#include <iostream>
#include <sstream>
#include <string>
#include <chrono>       //para pausa
#include <thread>       //para pausa


//funcion para leer todos los campos de una actividad academica de su fichero correspondiente
int leerStrAct(std::ifstream &ListaActividades, struct act_academica &act){
    std::string cad;

    if (!std::getline(ListaActividades, cad)) {
        return 0; // No se pudo leer el identificador, se considera el final del archivo
    }

    //Se leen uno a uno todos los campos
    act.id=stoi(cad);
    
    std::getline(ListaActividades, act.nombre);

    std::getline(ListaActividades, act.descripcion);

    //se lee el aforo, se comprueba que no esté en blanco
    std::getline(ListaActividades, cad);

    if(cad!=""){
        act.aforo=std::stoi(cad);
    }
    else{
        act.aforo=0;
    }

    //se leen las plazas disponibles, se comprueba que no esté en blanco
    std::getline(ListaActividades, cad);
    if(cad!=""){
        act.plazas_disp=std::stoi(cad);
    }
    else{
        act.plazas_disp=0;
    }


    //se lee el precio, se comprueba que no esté en blanco
    std::getline(ListaActividades, cad);
    if(cad!=""){
        act.precio=std::stoi(cad);
    }
    else{
        act.precio=0;
    }

    std::getline(ListaActividades, act.fecha);
    std::getline(ListaActividades, act.lugar);
    std::getline(ListaActividades, act.director_academico);
    std::getline(ListaActividades, act.ponente);

    //se lee el estado, se comprueba que no esté en blanco
    std::getline(ListaActividades, cad);
    if(cad!=""){
        act.estado=std::stoi(cad);
    }
    else{
        act.estado=2;
    }

    return 1; // Lectura exitosa
}



//esta sera la primera funcion que ejecute el programa. Recibe Usuario user como parámetro, ya que lo primero que debe hacer el programa en el main() es crear
//un user con la ip y la fecha de entrada
void menu_inicio_sesion(Usuario &user){
    std::cout<<"\n\033[1;34mSeleccione como desea acceder al sistema\033[0m\n";
    std::cout<<"1. Acceso con credenciales\n";
    std::cout<<"2. Acceso como invitado\n";
    opc_menu_inicio_sesion(user);
}


//sirve para dar pie a iniciar sesion como usuario registrado o continuar como invitado
void opc_menu_inicio_sesion(Usuario &user){
    int opcion;
    if(std::cin>>opcion){
    }
    else{
        std::cout<<"\033[1;31mERROR, entrada no válida\033[1;31m\n";
        exit(EXIT_FAILURE);
    }
    
    switch(opcion){
        case 1:
            pedirCredenciales(user);
            break;
        case 2:
            user.SetRol(1);
            user.mostrarMenu();
            break;
        default:
            while(opcion!=1 || opcion!=2){
            std::cout<<"Escoja una opción válida\n";
            menu_inicio_sesion(user);
    }
    }
}



//funcion para leer todos los campos de un usuario de su fichero correspondiente
int leerStrUser(std::ifstream &fichero, struct usuario1 &u1){
    std::string cad;

    if (!std::getline(fichero, u1.correo)) {
        return 0; // No se pudo leer el identificador, se considera el final del archivo
    }

    std::getline(fichero, u1.password);

    //hay que convertir el rol de string a int
    std::getline(fichero, cad);
    u1.rol=std::stoi(cad);
    
    std::getline(fichero, u1.nombre_completo);
    std::getline(fichero, u1.dni);

    //hay que convertir la facultad de string a Facultad
    std::getline(fichero, cad);
    if(cad=="Educacion"){
        u1.facultad=Facultad::Educacion;
    }
    if(cad=="Politecnica"){
        u1.facultad=Facultad::Politecnica;
    }
    if(cad=="Ciencias"){
        u1.facultad=Facultad::Ciencias;
    }
    if(cad=="Derecho"){
        u1.facultad=Facultad::Derecho;
    }

    //hay que convertir la carrera de string a Carrera
    std::getline(fichero, cad);
    if(cad=="Ingenieria_Informatica"){
        u1.carrera=Carrera::Ingenieria_Informatica;
    }
    if(cad=="Ingenieria_Mecanica"){
        u1.carrera=Carrera::Ingenieria_Mecanica;
    }
    if(cad=="Ingenieria_Electronica"){
        u1.carrera=Carrera::Ingenieria_Electronica;
    }
    if(cad=="Ingenieria_Electrica"){
        u1.carrera=Carrera::Ingenieria_Electrica;
    }
    if(cad=="Matematicas"){
        u1.carrera=Carrera::Matematicas;
    }
    if(cad=="ADE"){
        u1.carrera=Carrera::ADE;
    }
    if(cad=="Fisica"){
        u1.carrera=Carrera::Fisica;
    }
    if(cad=="Quimica"){
        u1.carrera=Carrera::Quimica;
    }

    return 1;
}


//funcion que pide el correo del usuario, si se encuentra en la bbdd le pide la contraseña, y si esta se introduce correctamente 
//se establecen los valores a los atributos del usuario
void pedirCredenciales(Usuario &user){
    std::string correo, password;
    struct usuario1 u1;
    std::cout<<"\nIntroduzca el correo\n";
    //hay que duplicar el getline ya que lee un \n residual
    std::getline(std::cin, correo);
    std::getline(std::cin, correo);
    if(correo==""){
        std::cout<<"\033[1;31mNo has introducido ningun correo\033[1;31m\n";
        exit(EXIT_FAILURE);
    }
    //debemos asegurarnos de que el correo se lee correctamente
    if(correo[correo.length() -1 ] == '\n'){
        correo[correo.length() -1 ] = '\0';
    }

    std::ifstream usuarios("usuarios.txt");
    int intentos=3;

    fallo_fichero(usuarios);

    //leo uno a uno los usuarios hasta encontrar correspondencia en el correo
    while((leerStrUser(usuarios, u1))==1){
        
        if(correo==u1.correo){
            std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo
            std::cout<<"\n\033[1;32mUsuario encontrado. Introduzca la contraseña\033[0m\n";
            std::getline(std::cin, password);
            
            //mientras que queden intentos, se permite introducir la contraseña
            while(intentos>0){
                while(password==""){
                    std::cout<<"Introduzca la contraseña\n";
                    std::getline(std::cin, password);
                }
                //compruebo que la contraseña sea correcta
                if(password==u1.password){
                    std::cout<<"\n\033[1;32mCredenciales correctas. Iniciando sesión\033[0m\n";

                    //inicializo los valores del usuario a los valores de la bbdd
                    user.SetCorreo(correo);
                    user.SetPassword(password);
                    user.SetRol(u1.rol);
                    user.SetNombreCompleto(u1.nombre_completo);
                    user.SetDni(u1.dni);
                    user.SetCarrera(u1.carrera);
                    user.SetFacultad(u1.facultad);
                    usuarios.close();
                    user.mostrarMenu();
                    usuarios.close();
                    break;
                }
                else{
                    //se ha introducido una contraseña incorrecta
                    intentos--;
                    if(intentos!=0){
                        std::cout<<"\nContraseña incorrecta. Inténtelo de nuevo. Intentos restantes: "<<intentos<<std::endl;
                        std::getline(std::cin, password);

                    }
                    else{
                        std::cout<<"\n\033[1;31mContaseña incorrecta. Se han agotado los intentos. Póngase en contacto con el organizador del sistema\033[1;31m\n";
                        usuarios.close();
                        exit(EXIT_FAILURE);
                    }
                }
            }
            
              usuarios.close();
              break;
        }
    }
    usuarios.close();
    std::cout<<"\033[1;31mNo se ha encontrado el usuario\033[1;31m\n";
    exit(EXIT_FAILURE);
}



int menu_admin_act(){
    int opcion;
    std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo
    std::cout<<"\n\033[1;34mSeleccione una opción\033[0m\n";
    std::cout<<"1. Crear Actividad Académica\n";
    std::cout<<"2. Editar Actividad Académica\n";
    std::cout<<"3. Eliminar Actividad Académica\n";

    if(std::cin>>opcion){
    }
    else{
        std::cout<<"\033[1;31mERROR, entrada no válida\033[1;31m\n";
        exit(EXIT_FAILURE);
    }

    std::cout<<"\n";
    if(opcion<1 || opcion>3){
        std::cout<<"Escoja una opción válida\n";
        menu_admin_act();
        return -1;
    }
    else{
        return opcion;
    }
}



void crear_Actividad(){
    int intento=0, cont=0;
    struct act_academica actividad;

    std::ifstream nact("ListaActividades.txt");
    fallo_fichero(nact);

    //debemos saber cual es el id de la ultima actividad para continuar con el id siguiente
    while((leerStrAct(nact, actividad))==1){
        cont=actividad.id;
    }
    cont++;
    nact.close();

    //se obtienen y comprueban los datos necesarios de la actividad académica
    std::cout<<"\nId de la actividad: "<<actividad.id<<"\n";
    std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo
    std::cout<<"\nIntroduzca el nombre de la actividad\n";
    //duplicamos ya que la primera vez lee un \n residual
    std::getline(std::cin, actividad.nombre);  
    std::getline(std::cin, actividad.nombre);
    while(actividad.nombre==""){
        std::cout<<"\nNo puede dejar este campo vacío.\nIntroduzca el nombre de la actividad\n";
        std::getline(std::cin, actividad.nombre);
    }

    std::cout<<"\nIntroduzca una descripcion de la actividad\n";
    std::getline(std::cin, actividad.descripcion);

    std::cout<<"\nIntroduzca el aforo para la actividad\n";
    if(std::cin>>actividad.aforo){
    } 
    else{
        std::cout<<"\033[1;31mERROR, entrada no válida\033[1;31m\n";
        exit(EXIT_FAILURE);
    }
    if(actividad.aforo<0){
        std::cout<<"\033[1;31mERROR, el valor introducido no puede ser negativo\033[1;31m\n";
        exit(EXIT_FAILURE);
    }
    actividad.plazas_disp=actividad.aforo;

    std::cout<<"\nIntroduzca el precio de la actividad\n";
    
    if(std::cin>>actividad.precio){
    }
    else{
        std::cout<<"\033[1;31mERROR, entrada no válida\033[1;31m\n";
        exit(EXIT_FAILURE);
    }
    if(actividad.precio<0){
        std::cout<<"\033[1;31mERROR, el valor introducido no puede ser negativo\033[1;31m\n";
        exit(EXIT_FAILURE);
    }

    std::cout<<"\nIntroduzca la fecha de la actividad\n";
    //duplicamos ya que la primera vez lee un \n residual
    std::getline(std::cin, actividad.fecha);
    std::getline(std::cin, actividad.fecha);
    while(actividad.fecha==""){
        std::cout<<"\n\033[1;31mNo puede dejar este campo vacío.\nIntroduzca la fecha de la actividad\033[0m\n";
        std::getline(std::cin, actividad.fecha);
    }

    std::cout<<"\nIntroduzca la lugar para la actividad\n";
    std::getline(std::cin, actividad.lugar);
    while(actividad.lugar==""){
        std::cout<<"\n\033[1;31mNo puede dejar este campo vacío.\nIntroduzca el lugar de la actividad\033[0m\n";
        std::getline(std::cin, actividad.lugar);
    } 

    std::cout<<"\nIntroduzca el/los ponente/s de la actividad (en una sola linea)\n";
    std::getline(std::cin, actividad.ponente);

    
    std::cout<<"\nIntroduzca el correo del director académico de la actividad\n";
    std::getline(std::cin, actividad.director_academico);
    while(!comprobar_director(actividad)){
        std::cout<<"\n\033[1;31mCorreo no válido\033[1;31m\n";
        std::cout<<"\nIntroduzca el correo del director académico de la actividad\n";
        std::getline(std::cin, actividad.director_academico);
    }

    while(actividad.estado!=1 && actividad.estado!=2){
        if(intento!=0){
            std::cout<<"\n\033[1;31mEstado no válido\033[0m\n";
        }
        std::cout<<"\nIntroduzca el estado para la actividad\n";
        std::cout<<"1: Activa       2: Oculta\n";
        if(std::cin>>actividad.estado){
        }
        else{
            std::cout<<"\033[1;31mERROR, entrada no válida\033[1;31m\n";
            exit(EXIT_FAILURE);
        }
        intento++;
    }

    //hay que abrir el fichero de actividades academicas para añadir e introducir la actividad creada
    std::ofstream actividades("ListaActividades.txt", std::ios::app);

    fallo_fichero(actividades);

    actividades<<actividad.id<<"\n";
    actividades<<actividad.nombre<<"\n";
    actividades<<actividad.descripcion<<"\n";
    actividades<<actividad.aforo<<"\n";
    //inicialmente las plazas disponibles serán el aforo total
    actividades<<actividad.plazas_disp<<"\n";
    actividades<<actividad.precio<<"\n";
    actividades<<actividad.fecha<<"\n";
    actividades<<actividad.lugar<<"\n";
    actividades<<actividad.director_academico<<"\n";
    actividades<<actividad.ponente<<"\n";
    actividades<<actividad.estado<<"\n";
    
    actividades.close();

    //se han creado la actividad, hay que crearla tambien en el fichero de Inscripciones
    std::ofstream inscripciones("Inscripciones.txt", std::ios::app);
    fallo_fichero(inscripciones);

    inscripciones<<actividad.id<<"\n";
    for(int i=0; i<actividad.aforo; i++){
        inscripciones<<"\n";
    }
    inscripciones.close();

}



//funcion que comprueba que el correo introducido como director academico al crear una actividad es correcto
bool comprobar_director(struct act_academica actividad){
    struct usuario1 u1;
    std::ifstream usuarios("usuarios.txt");

    fallo_fichero(usuarios);

    while((leerStrUser(usuarios, u1))==1){

        if(u1.correo==actividad.director_academico){
            if(u1.rol==3 || u1.rol==4){
                std::cout<<"\n\033[1;32mSe ha comprobado correctamente el director académico\033[0m\n";
                usuarios.close();
                return true;
            }
            else{
                std::cout<<"\n\033[1;31mEl correo introducido no pertenece a un director académico\033[0m\n";
                usuarios.close();
                return false;
            }
        }
    }
    std::cout<<"\nNo se ha encontrado el correo\n";
    usuarios.close();
    return false;
}



//funcion que comprueba que el correo introducido como director academico al crear una actividad es correcto
bool comprobar_correo(std::string correo){
    struct usuario1 u1;
    std::ifstream usuarios("usuarios.txt");

    fallo_fichero(usuarios);

    while((leerStrUser(usuarios, u1))==1){

        if(u1.correo==correo){
            std::cout<<"\n\033[1;32mSe ha comprobado correctamente el correo\033[0m\n";
            usuarios.close();
            return true;
        }

    }
    std::cout<<"\n\033[1;31mNo se ha encontrado el correo\033[0m\n";
    usuarios.close();
    return false;
}




bool sustituirStr(std::string nombreArchivo, struct act_academica &actividad, int numeroLinea){
    // Abrir el archivo en modo lectura
    std::ifstream archivoEntrada(nombreArchivo);

    fallo_fichero(archivoEntrada);

    // Leer el contenido del archivo línea por línea
    std::vector<std::string> lineas;
    std::string lineaActual;
    while (getline(archivoEntrada, lineaActual)) {
        lineas.push_back(lineaActual);
    }


    // Verificar si el número de línea es válido
    if (numeroLinea > 0 && numeroLinea <= static_cast<int>(lineas.size())) {
        // Sustituir la línea especificada
        //no hacemos nada con numeroLinea-1 ya que el id no cambia
        lineas[numeroLinea] = actividad.nombre;
        lineas[numeroLinea + 1] = actividad.descripcion;
        lineas[numeroLinea + 2] = std::to_string(actividad.aforo);
        lineas[numeroLinea + 3] = std::to_string(actividad.plazas_disp);
        lineas[numeroLinea + 4] = std::to_string(actividad.precio);
        lineas[numeroLinea + 5] = actividad.fecha;
        lineas[numeroLinea + 6] = actividad.lugar;
        lineas[numeroLinea + 7] = actividad.director_academico;
        lineas[numeroLinea + 8] = actividad.ponente;
        lineas[numeroLinea + 9] = std::to_string(actividad.estado);

        // Cerrar el archivo de entrada
        archivoEntrada.close();

        // Abrir el archivo en modo escritura para sobrescribir el contenido
        std::ofstream archivoSalida(nombreArchivo);
        fallo_fichero(archivoSalida);

        // Escribir el nuevo contenido de vuelta al archivo
        for (const std::string& linea : lineas) {
            archivoSalida << linea<<"\n";
        }

        archivoSalida.close();
        std::cout << "\033[1;32mSe ha actualizado la actividad\033[0m\n";
        return true;
    }
    else {
        std::cout << "\033[1;31mNo se ha actualizado la actividad\033[0m\n";
        return false;
    }
}



void editar_Actividad(Usuario &user){
    //muestro las actividades para elegir la actividad a editar. Usamos nLinea para saber el nº de linea en el que empieza la estructura que editaremos
    //hay que inicializar el numero de línea a -10 ya que si no, se sobreescribe la actividad siguiente a la deseada
    //nL_insc será el numero de linea del fichero de inscripciones, para modificar el aforo
    //nL_id almacenara el n de lidea del id de la actividad que se quiere editar en el fichero Inscripciones
    int opcion, intento=0, nLinea=-10, nL_insc=0, nL_id;      
    bool encontrado, hayEspacio;
    if(user.listarActividadesBasico(2)){
        std::cout<<"No hay actividades\n";
        user.mostrarMenu();
    }

    //busco la actividad
    struct act_academica act_orig, act_new;
    act_new.id=act_orig.id;
    std::string new_aforo, new_plazas, new_precio, new_estado, cad;
    std::vector <int> blanco;

    //abro el fichero en el que se encuentran listadas las actividades en modo lectura
    std::ifstream ListaActividades("ListaActividades.txt");

    //si no se ha abierto el fichero, error
    fallo_fichero(ListaActividades);


    std::cout<<"\n\033[1;34mIndique el id de la actividad que desea editar\033[0m\n";
    if(std::cin>>opcion){
    }
    else{
        std::cout<<"\033[1;31mERROR, entrada no válida\033[1;31m\n";
        ListaActividades.close();
        exit(EXIT_FAILURE);
    }

    //leemos la actividad correspondiente
    while((leerStrAct(ListaActividades, act_orig))==1){
        nLinea+=11;

        //si el identificador leido es igual al buscado, estamos en la actividad que buscabamos
        if(opcion==act_orig.id){
            encontrado=true;
            std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo
            std::cout<<"\n\033[1;32mSe ha encontrado la actividad\033[0m\n";
            std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo

            std::cout<<"\nIntroduzca los nuevos valores de cada campo. Si no desea modificar dicho campo, pulse enter\n\n";
            std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo
            std::cout<<"\nIntroduzca el nombre de la actividad\n";
            //duplicamos ya que la primera vez lee un \n residual
            std::getline(std::cin, act_new.nombre);
            std::getline(std::cin, act_new.nombre);

            std::cout<<"\nIntroduzca una descripcion de la actividad\n";
            std::getline(std::cin, act_new.descripcion);

            std::cout<<"\nIntroduzca el aforo para la actividad\n";
            std::getline(std::cin, new_aforo);

            //modificar el aforo significa modificar las plazas disponibles, por lo que hay que comprobar que si se ha reducido el aforo,
            //las plazas disponibles no queden en negativo
            if(new_aforo!=""){
                act_new.aforo=std::stoi(new_aforo);
                if(act_new.aforo<0){
                    std::cout<<"\033[1;31mERROR, el valor introducido no puede ser negativo\033[1;31m\n";
                    ListaActividades.close();
                    exit(EXIT_FAILURE);
                }
                int dif_aforo=act_new.aforo - act_orig.aforo;


                std::ifstream inscripciones("Inscripciones.txt");
                fallo_fichero(inscripciones);

                while(std::getline(inscripciones, cad)){
                    hayEspacio = false;
                    nL_insc++;
            
                    for (char c : cad) {
                        if (std::isspace(c)) {
                            hayEspacio = true;
                            break;
                        }
                    }

                    //se ha leido el id de una actividad
                    if(!hayEspacio && cad!=""){

                        if(opcion==std::stoi(cad)){
                            //se ha leido en Inscripciones el id de la actividad que se quiere modificar
                            nL_id=nL_insc;

                            //leemos todos las inscripciones que hay en la actividad
                            for(int i=0; i<act_orig.aforo; i++){
                                std::getline(inscripciones, cad);
                                nL_insc++;
                                if(cad==""){
                                    blanco.push_back(nL_insc);      //si leemos una linea en blanco, almacenamos su numero de linea por si el aforo se reduce
                                }
                            }
                        }
                    }
                }
                inscripciones.close();


                if(dif_aforo>0){
                    act_orig.plazas_disp+=dif_aforo;
                    //hay que añadir espacios en las inscripciones
                    for(int i=0; i<dif_aforo; i++){
                        if(sustituirStrInsc(user, nL_id, 4)){
                            std::cout<<"\nSe ha añadido una plaza\n";
                        }
                        else{
                            std::cout<<"\033[1;31mERROR al añadir plazas\033[1;31m\n";
                            ListaActividades.close();
                            exit(EXIT_FAILURE);
                        }
                    }
                }
                else{
                    if(dif_aforo<0){
                        act_orig.plazas_disp+=dif_aforo;
                        if(act_orig.plazas_disp<0){
                            std::cout<<"\n\033[1;31mERROR, las plazas son negativas\033[1;31m\n";
                            ListaActividades.close();
                            exit(EXIT_FAILURE);
                        }
                        //pongo dif_aforo en positivo para usar un contador positivo
                        dif_aforo-=2*dif_aforo;
                        //hay que quitar espacios de las inscripciones
                        for(int i=0; i<dif_aforo; i++){
                            if(sustituirStrInsc(user, blanco[i], 5)){
                                std::cout<<"Se ha reducido una plaza\n";
                            }
                            else{
                                std::cout<<"\033[1;31mERROR al reducir plazas\033[1;31m\n";
                                ListaActividades.close();
                                exit(EXIT_FAILURE);
                            }
                        }
                    }
                }
                act_new.plazas_disp=act_orig.plazas_disp;
                std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo
                std::cout<<"\nAl modificar el aforo se han modificado las plazas disponibles\n";
            }
            

            std::cout<<"\nIntroduzca el precio de la actividad\n";
            std::getline(std::cin, new_precio);
            
            
            std::cout<<"\nIntroduzca la fecha de la actividad\n";
            std::getline(std::cin, act_new.fecha);

            std::cout<<"\nIntroduzca la lugar para la actividad\n";
            std::getline(std::cin, act_new.lugar); 

            std::cout<<"\nIntroduzca el ponente de la actividad\n";
            std::getline(std::cin, act_new.ponente);


            std::cout<<"\nIntroduzca el correo del director académico de la actividad\n";
            std::getline(std::cin, act_new.director_academico);
            if(act_new.director_academico!=""){
                while(!comprobar_director(act_new)){
                    std::cout<<"\nCorreo no válido\n";
                    std::cout<<"\nIntroduzca el correo del director académico de la actividad\n";
                    std::getline(std::cin, act_new.director_academico);
                }
            }

            
            std::cout<<"\nIntroduzca el estado para la actividad\n";
            std::cout<<"1: Activa       2: Oculta       3: Caducada\n";
            std::getline(std::cin, new_estado);
            if(new_estado!=""){
                while(new_estado!="1" && new_estado!="2" && new_estado!="3"){
                    if(intento!=0){
                        std::cout<<"\nEstado no válido\n";
                    }
                    std::cout<<"\nIntroduzca el estado para la actividad\n";
                    std::cout<<"1: Activa       2: Oculta       3: Caducada\n";
                    std::getline(std::cin, new_estado);
                    intento++;
                }
                act_new.estado=std::stoi(new_estado);
            }
            

            //ya se han introducido todos los datos actualizados. Ahora debemos comprobar si estos datos estan en blanco (no se quieren actualizar)
            if(act_new.nombre==""){
                act_new.nombre=act_orig.nombre;
            }
            if(act_new.descripcion==""){
                act_new.descripcion=act_orig.descripcion;
            }
            if(new_aforo==""){
                act_new.aforo=act_orig.aforo;
            }
            if(act_new.aforo<0){
                std::cout<<"\033[1;31mERROR, el aforo no puede ser negativo\033[1;31m\n";
                ListaActividades.close();
                exit(EXIT_FAILURE);
            }


            if(new_precio==""){
                act_new.precio=act_orig.precio;
            }
            else{
                act_new.precio=std::stoi(new_precio);
            }
            if(act_new.precio<0){
                std::cout<<"\033[1;31mERROR, el precio no puede ser negativo\033[1;31m\n";
                ListaActividades.close();
                exit(EXIT_FAILURE);
            }

            if(act_new.fecha==""){
                act_new.fecha=act_orig.fecha;
            }
            if(act_new.lugar==""){
                act_new.lugar=act_orig.lugar;
            }
            if(act_new.ponente==""){
                act_new.ponente=act_orig.ponente;
            }
            if(act_new.director_academico==""){
                act_new.director_academico=act_orig.director_academico;
            }
            if(new_estado==""){
                act_new.estado=act_orig.estado;
            }

            ListaActividades.close();

            std::cout<<"\nVamos a imprimir la actividad actualizada\n\n";

            //se deben leer las lineas de caracteristicas de la actividad
            std::cout<<"Nombre: "<<act_new.nombre <<std::endl;
            std::cout<<"Descripción: "<<act_new.descripcion <<std::endl;
            std::cout<<"Aforo: "<<act_new.aforo <<std::endl;
            std::cout<<"Plazas disponibles: "<<act_new.plazas_disp<<std::endl;
            std::cout<<"Precio: "<<act_new.precio <<std::endl;
            std::cout<<"Fecha: "<<act_new.fecha <<std::endl;
            std::cout<<"Lugar: "<<act_new.lugar <<std::endl;
            std::cout<<"Director Académico: "<<act_new.director_academico <<std::endl;
            std::cout<<"Ponente: "<<act_new.ponente <<std::endl;
            switch(act_new.estado){
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
            //ahora se debe sobreescribir la nueva estructura actualizada en el fichero
            if(!sustituirStr("ListaActividades.txt", act_new, nLinea)){
                std::cout<<"\033[1;31mNo se ha podido editar la actividad\033[1;31m\n";
                exit(EXIT_FAILURE);
            }
            else{
                std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo
                std::cout<<"\033[1;32mSe ha actualizado la actividad correctamente\033[0m\n";
            }
        }
    }
    if(!encontrado){
        std::cout<<"\033[1;31mNo se ha encontrado la actividad\033[1;31m\n";
        ListaActividades.close();
        exit(EXIT_FAILURE);
    }   
}           



int inscripcion(Usuario &user, struct act_academica &act){
    std::ifstream ListaInscripciones("Inscripciones.txt");
    int nacts, nLinea=0, id_act;
    std::vector <int> nblanco;
    std::string cad, cad2, dni;
    bool encontrado, hayEspacio=false;

    //si no se ha abierto el fichero, error
    fallo_fichero(ListaInscripciones);

    //hay que recorrer el fichero hasta encontrar la actividad, entonces, comprobamos si el usuario ya esta inscrito en esa actividad
    while(std::getline(ListaInscripciones, cad)){
        hayEspacio = false;
        nLinea++;       //tenemos el nLinea del id de la actividad
        for (char c : cad) {
            if (std::isspace(c)) {
                hayEspacio = true;
                break;
            }
        }

        //comprobamos que en cad hay el id de una actividad, para hacer stoi, sino, falla
        if(!hayEspacio && cad!=""){
            //hemos leido la id de una actividad, comprobamos si es la que estamos buscando
            if(act.id==std::stoi(cad)){
                
                encontrado=true;
                std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo
                std::cout<<"\n\033[1;32mSe ha encontrado la actividad\033[0m\n";

                //comprobamos que el usuario no este inscrito en la actividad
                for(int i=0; i<act.aforo; i++){
                    std::getline(ListaInscripciones, cad2);
                    hayEspacio=false;
                    nLinea++;       //contiene el numero de la linea que se acaba de leer

                    for (char c : cad2) {
                        if (std::isspace(c)) {
                            hayEspacio = true;
                            break;
                        }
                    }

                    if(hayEspacio){
                        // Usar std::istringstream para dividir la cadena
                        std::istringstream stream(cad2);
    
                        // Leer la primera palabra
                        stream >> dni;
                    }
                    else{
                        //la linea esta en blanco, la almaceno en el vector
                        nblanco.push_back(nLinea);
                    }

                    if(dni==user.GetDni()){
                        std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo
                        std::cout<<"\nYa estas inscrito en esa actividad\n";
                        ListaInscripciones.close();
                        return 2;
                    }
                }

                std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo
                std::cout<<"\nNo estas inscrito a esa actividad, inscribiendote...\n";

                //cerramos fichero
                ListaInscripciones.close();

                //el usuario no estaba inscrito en la actividad, vamos a hacer la preinscripcion (sustituir lineas de la actividad)
                if(sustituirStrInsc(user, nblanco[0], 1)){
                    std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo
                    std::cout<<"\033[1;32mTe acabas de inscribir a la actividad\033[0m\n";

                    std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo
                    //hay que actualizar las plazas de la actividad
                    std::cout<<"\nPlazas disponibles antes: "<<act.plazas_disp<<"\n";
                    act.plazas_disp--;
                    std::cout<<"\nPlazas disponibles despues: "<<act.plazas_disp<<"\n";
                    return 1;
                }
            }
        }
    }
    if(encontrado=false){
        std::cout<<"\033[1;31mNo se ha encontrado la actividad para realizar la inscripcion\033[0m\n";
        return 0;
    }
    std::cout<<"\033[1;31mNo ha podido realizarse la inscripcion\033[1;31m\n";
    exit(EXIT_FAILURE);
    return 0;
}



bool sustituirStrInsc(Usuario &user, int numeroLinea, int opcion){
    // Abrir el archivo en modo lectura
    std::ifstream archivoEntrada("Inscripciones.txt");


    fallo_fichero(archivoEntrada);

    // Leer el contenido del archivo línea por línea
    std::vector<std::string> lineas;
    std::string lineaActual, cad, dni;


    while (getline(archivoEntrada, lineaActual)) {
        lineas.push_back(lineaActual);
    }


    // Verificar si el número de línea es válido
    if (numeroLinea > 0 && numeroLinea <= static_cast<int>(lineas.size())) {
        // para hacer preinscripciones
        if(opcion==1){
            lineas[numeroLinea-1] = user.GetDni() + " 1";
        }
        else{
            //para eliminar inscripciones y poner la linea en blanco
            if(opcion==2){
                lineas[numeroLinea-1] = "";  
            }
            else{
                //para pasar de preinscrito a inscrito
                if(opcion==3){
                    cad=lineas[numeroLinea-1];
                    std::istringstream stream(cad);
    
                    // Leer la primera palabra
                    stream >> dni;

                    lineas[numeroLinea-1] = dni + " 2";
                }
                else{
                    //para añadir una linea detras de numeroLinea
                    if(opcion==4){
                        lineas[numeroLinea-1]+="\n";
                    }
                    else{
                        //para eliminar la linea numeroLinea
                        if(opcion==5){
                            lineas.erase(lineas.begin() + numeroLinea - 1); 
                        }
                    }
                }
            }
        }

        // Cerrar el archivo de entrada
        archivoEntrada.close();

        // Abrir el archivo en modo escritura para sobrescribir el contenido
        std::ofstream archivoSalida("Inscripciones.txt");
        fallo_fichero(archivoSalida);

        // Escribir el nuevo contenido de vuelta al archivo
        for (const std::string& linea : lineas) {
            archivoSalida << linea<<"\n";
        }

        archivoSalida.close();


        if(opcion==1){
            std::cout << "\033[1;32mSe ha creado la inscripcion\033[0m\n";
        }
        return true;
    }
    else {
        archivoEntrada.close();
        std::cout << "\033[1;31mNo se ha creado la inscripcion\033[0m\n";
        return false;
    }
}



void verMisActividades(Usuario &user){
    std::ifstream ListaInscripciones("Inscripciones.txt");
    std::ifstream ListaActividades("ListaActividades.txt");
    std::string cad, cad2, dni, estado, aux;
    bool hayEspacio=false, inscrito=false;
    struct act_academica act;


    fallo_fichero(ListaInscripciones);

    fallo_fichero(ListaActividades);


    //hay que recorrer el ficheroleyendo el id de las actividades, buscando en cuales esta inscrito el usuario
    std::getline(ListaInscripciones, cad);
    std::cout<<"\n\033[1;34mSe van a imprimir las actividades en las que estás inscrito\033[0m\n";
    std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo
    while(!hayEspacio && cad!=""){
        inscrito=false;
        hayEspacio = false;
        for (char c : cad) {
            if (std::isspace(c)) {
                hayEspacio = true;
                break;
            }
        }

        //comprobamos que en cad hay el id de una actividad, para hacer stoi, sino, falla
        if(!hayEspacio && cad!=""){
            //hemos leido la id de una actividad

            //comprobamos que el usuario este inscrito en la actividad
            std::getline(ListaInscripciones, cad2);
            hayEspacio=false;
                
            for (char c : cad2) {
                if (std::isspace(c)) {
                    hayEspacio = true;
                    break;
                }
            }

            while(cad2=="" || hayEspacio){
                hayEspacio=false;
                
                for (char c : cad2) {
                    if (std::isspace(c)) {
                        hayEspacio = true;
                        break;
                    }
                }

                if(hayEspacio){
                    // Usar std::istringstream para dividir la cadena
                    std::istringstream stream(cad2);

                    // Leer la primera palabra
                    stream >> dni;
                    stream >> estado;
                
                    if(dni==user.GetDni()){
                        //el usuario esta inscrito en esta actividad
                        inscrito=true;

                        //volvemos a leer ListaActividades desde el principio
                        ListaActividades.clear();
                        ListaActividades.seekg(0, std::ios::beg);
                        while((leerStrAct(ListaActividades, act))==1){
                            if(std::stoi(cad)==act.id){
                                std::cout<<act.id<<". "<<act.nombre<<"\nEstado: ";
                                switch(std::stoi(estado)){
                                    case 1:
                                        std::cout<<"Preinscrito\n\n";
                                        break;
                                    case 2:
                                        std::cout<<"Inscrito\n\n";
                                        break;
                                    default:
                                        std::cout<<"\033[1;31mEstado no válido\033[0m\n\n";
                                        break;
                                }
                            }
                        }
                    }
                }
                if(!std::getline(ListaInscripciones, cad2)){
                    ListaActividades.close();
                    ListaInscripciones.close();
                    std::cout<<"\nYa se han leido todas las actividades\n";
                    return;
                }
                if(!hayEspacio){
                    cad=cad2;
                }
            }
            if(!inscrito){
                //el usuario no esta inscrito en la actividad inscrita
                ListaActividades.close();
                ListaInscripciones.close();
            }
        }
    }
    
}



//al borrar la actividad, tambien hay que borrarla de la lista de inscripciones
void eliminar_Actividad(Usuario &user){
    std::string cad;
    int opcion, nLinea=-10, nLinea2=1;
    bool hayEspacio=false;

    if(user.listarActividadesBasico(2)){
        std::cout<<"No hay actividades\n";
        return;
    }

    //busco la actividad
    struct act_academica act;

    //abro el fichero en el que se encuentran listadas las actividades en modo lectura
    std::ifstream ListaActividades("ListaActividades.txt");
    std::ifstream ListaInscripciones("Inscripciones.txt");


    fallo_fichero(ListaActividades);

    fallo_fichero(ListaInscripciones);

    std::cout<<"\n\033[1;34mIndique el id de la actividad que desea eliminar\033[0m\n";
    if(std::cin>>opcion){
    }
    else{
        std::cout<<"\033[1;31mERROR, entrada no válida\033[1;31m\n";
        ListaActividades.close();
        ListaInscripciones.close();
        exit(EXIT_FAILURE);
    }

    //
    while((leerStrAct(ListaActividades, act))==1){
        nLinea+=11;         //tenemos el nLinea del id de la actividad leida

        if(act.id==opcion){
            //estamos en la actividad que queremos borrar. Hay que borrar primero la actividad de Inscripciones
            while(std::getline(ListaInscripciones, cad)){
                hayEspacio = false;
                nLinea2++;
                for (char c : cad) {
                    if (std::isspace(c)) {
                        hayEspacio = true;
                        break;
                    }
                }
                //comprobamos que en cad hay el id de una actividad, para hacer stoi, sino, falla
                if(!hayEspacio && cad!=""){
                    //hemos leido la id de una actividad, comprobamos si es la que estamos buscando
                    if(act.id==std::stoi(cad)){
                        
                        //hay que mandar nLinea2-1 ya que apunta a la siguiente linea
                        if(borrar(nLinea2-1, "Inscripciones.txt", act.aforo)){
                            std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo
                            std::cout<<"\n\033[1;32mSe ha eliminado la actividad de la lista de Inscripciones\033[0m\n";
                        }
                        else{
                            std::cout<<"\n\033[1;31mNo se ha podido eliminar la actividad de la lista de Inscripciones\033[1;31m\n";
                            ListaActividades.close();
                            ListaInscripciones.close();
                            exit(EXIT_FAILURE);
                        }
                    }
                }
            }

            ListaInscripciones.close();
            ListaActividades.close();
            if(borrar(nLinea, "ListaActividades.txt", 10)){
                std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo
                std::cout<<"\n\033[1;32mSe ha eliminado la actividad\033[0m\n";
                return;
            }
            else{
                std::cout<<"\033[1;31mNo se ha eliminado la actividad\033[1;31m\n";
                exit(EXIT_FAILURE);
            }
        }
    }
    std::cout<<"\nNo se ha encontrado la actividad\n";
}



bool borrar(int numeroLinea, std::string nombreArchivo, int borrarLineas){
    std::ifstream archivoEntrada(nombreArchivo);

    fallo_fichero(archivoEntrada);

    // Leer líneas del archivo y almacenarlas en un vector
    std::vector<std::string> lineas;
    std::string linea;
    while (std::getline(archivoEntrada, linea)) {
        lineas.push_back(linea);
    }

    archivoEntrada.close();

    // Eliminar desde la primera linea de la actividad hasta la ultima linea de la actividad

    lineas.erase(lineas.begin() + numeroLinea - 1, lineas.begin() + numeroLinea + borrarLineas);

    // Abrir el archivo en modo de escritura para sobrescribir
    std::ofstream archivoSalida(nombreArchivo);

    fallo_fichero(archivoSalida);

    // Escribir las líneas restantes en el archivo
    for (const auto& l : lineas) {
        archivoSalida << l << std::endl;
    }

    archivoSalida.close();

    std::cout << "\n\033[1;32mLíneas eliminadas con éxito.\033[0m" << std::endl;

    return true;
}



void eliminarInscripcion(Usuario &user){
    verMisActividades(user);

    std::ifstream ListaInscripciones("Inscripciones.txt");
    int nacts, numeroLinea=-10, nLinea=1, id_act;
    std::string cad, cad2, dni;
    bool encontrado, hayEspacio=false;


    fallo_fichero(ListaInscripciones);


    std::cout<<"\n\033[1;34mSeleccione la actividad para eliminar la inscripcion\033[0m\n";
    int opcion;
    if(std::cin>>opcion){
    }
    else{
        std::cout<<"\033[1;31mERROR, entrada no válida\033[1;31m\n";
        ListaInscripciones.close();
        exit(EXIT_FAILURE);
    }

    std::ifstream ListaActividades("ListaActividades.txt");
    struct act_academica act;

    fallo_fichero(ListaActividades);

    while((leerStrAct(ListaActividades, act))==1){
        numeroLinea+=11;
        if(act.id==opcion){
            break;
        }
    }
    ListaActividades.close();

    if(act.id!=opcion){
        //el numero de la actividad introducido no corresponde a ninguna actividad
        std::cout<<"\nNo se ha encontrado la actividad\n";
        user.mostrarMenu();
    }


    

    //hay que recorrer el fichero hasta encontrar la actividad, entonces, comprobamos si el usuario ya esta inscrito en esa actividad
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
            if(act.id==std::stoi(cad)){
    
                encontrado=true;
                std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo
                std::cout<<"\n\033[1;32mSe ha encontrado la actividad\033[0m\n";

                //comprobamos que el usuario este inscrito en la actividad
                for(int i=0; i<act.aforo; i++){
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
                        // Usar std::istringstream para dividir la cadena
                        std::istringstream stream(cad2);
    
                        // Leer la primera palabra
                        stream >> dni;
                    }

                    if(dni==user.GetDni()){
                        if(sustituirStrInsc(user, nLinea-1, 2)){
                            std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo
                            std::cout<<"\n\033[1;32mInscripción borrada con éxito\033[0m\n";
                            //HAY QUE SUMAR 1 A LAS PLAZAS DISPONIBLES DE LA ACTIVIDAD
                            act.plazas_disp++;
                            if(sustituirStr("ListaActividades.txt", act, numeroLinea)){
                                //cerramos fichero
                                ListaInscripciones.close();
                                std::this_thread::sleep_for(std::chrono::seconds(1));  // Pausa de 1 segundo
                                std::cout<<"\nSe ha sumado 1 a las plazas disponibles de la actividad\n";
                                return;
                            }
                        }
                    }
                }


                //cerramos fichero
                ListaInscripciones.close();

                //el usuario no estaba inscrito en la actividad
                std::cout<<"\nNo estas inscrito en esa actividad\n";
            }
        }
    }
    if(encontrado=false){
        std::cout<<"\n\033[1;31mNo se ha encontrado la actividad\033[1;31m\n";
        ListaInscripciones.close();
        exit(EXIT_FAILURE);
    }
    ListaInscripciones.close();
    exit(EXIT_FAILURE);
}



void fallo_fichero(std::ifstream &fichero){
    //si no se ha abierto el fichero, error
    if(!fichero){
        std::cout<<"\n\033[1;31mError al abrir fichero\033[1;31m\n";
        exit(EXIT_FAILURE);
    }


    if(fichero.eof()){
        std::cout<<"\n\033[1;31mError de fichero\033[1;31m\n";
        exit(EXIT_FAILURE);   
    }
}



void fallo_fichero(std::ofstream &fichero){
    //si no se ha abierto el fichero, error
    if(!fichero){
        std::cout<<"\n\033[1;31mError al abrir fichero\033[1;31m\n";
        exit(EXIT_FAILURE);
    }


    if(fichero.eof()){
        std::cout<<"\n\033[1;31mError de fichero\033[1;31m\n";
        exit(EXIT_FAILURE);   
    }
}



void enviarCorreo(Usuario &user){
    std::cout<<"\nVas a enviar un correo\n";
    std::cout<<"Introduzca el correo del destinatario\n";
    std::string correo, asunto, mensaje;

    std::getline(std::cin, correo);
    std::getline(std::cin, correo);
    if(correo==""){
        std::cout<<"\033[1;31mNo has introducido ningun correo\033[1;31m\n";
        exit(EXIT_FAILURE);
    }
    //debemos asegurarnos de que el correo se lee correctamente
    if(correo[correo.length() -1 ] == '\n'){
        correo[correo.length() -1 ] = '\0';
    }

    if(!comprobar_correo(correo)){
        exit(EXIT_FAILURE);
    }

    std::cout<<"Introduzca el asunto del correo\n";
    std::getline(std::cin, asunto);
    if(asunto==""){
        std::cout<<"\033[1;31mEl asunto no puede estar vacío\033[1;31m\n";
        user.mostrarMenu();
    }
    //quitamos la \n final
    if(asunto[asunto.length() -1 ] == '\n'){
        asunto[asunto.length() -1 ] = '\0';
    }

    std::cout<<"Introduzca el cuerpo del correo. Recuerde que debe ser sin saltos de línea\n";
    std::getline(std::cin, mensaje);
    if(mensaje==""){
        std::cout<<"\033[1;31mEl mensaje no puede estar vacío\033[1;31m\n";
        user.mostrarMenu();
    }
    //quitamos la \n final
    if(mensaje[mensaje.length() -1 ] == '\n'){
        mensaje[mensaje.length() -1 ] = '\0';
    }

    //se han recogido todos los datos necesarios para mandar el correo, ahora se plasma en el fichero Correos.txt
    //hay que abrir el fichero de correos para añadir e introducir el correo
    std::ofstream correos("Correos.txt", std::ios::app);
    fallo_fichero(correos);
    correos<<"Remitente: " + user.GetCorreo() + "\n";
    correos<<"Receptor: " + correo + "\n";
    correos<<"Asunto: " + asunto + "\n";
    correos<<"Mensaje: " + mensaje + "\n";

    correos.close();
    std::cout<<"\n\033[1;32mSe ha enviado el correo correctamente\033[0m\n";
}



void difusion(Usuario &user){
    std::cout<<"\nSeleccione la opción que desee\n";
    std::cout<<"1. Difusión por facultad\n";
    std::cout<<"2. Difusión por carrera\n";
    int opcion;

    if(std::cin>>opcion){
    }
    else{
        std::cout<<"\033[1;31mERROR, entrada no válida\033[1;31m\n";
        exit(EXIT_FAILURE);
    }

    switch(opcion){
        case 1:
            difusion_facultad(user);
            break;
        case 2:
            difusion_carrera(user);
            break;
        default:
            std::cout<<"\033[1;31mOpción no válida\033[0m\n";
            user.mostrarMenu();
            break;
    }
}


void difusion_facultad(Usuario &user){
    int opcion;
    struct usuario1 u;
    std::string correo, receptores, asunto, mensaje;
    Facultad facultad;
    std::cout<<"Seleccione la facultad que desee\n";
    std::cout<<"1. Educación\n2. Derecho\n3. Politecnica\n4. Ciencias\n";

    if(std::cin>>opcion){
    }
    else{
        std::cout<<"\033[1;31mERROR, entrada no válida\033[1;31m\n";
        exit(EXIT_FAILURE);
    }

    switch(opcion){
        case 1:
            facultad=Facultad::Educacion;
            break;
        case 2:
            facultad=Facultad::Derecho;
            break;
        case 3:
            facultad= Facultad::Politecnica;
            break;
        case 4:
            facultad=Facultad::Ciencias;
            break;
        default:
            std::cout<<"\033[1;31mOpción no válida\033[0m\n";
            user.mostrarMenu();
            break;
    }

    std::ifstream ListaActividades("ListaActividades.txt");
    while(leerStrUser(ListaActividades, u)){
        if(u.facultad==facultad){
            correo=u.correo;
            if(correo[correo.length() -1 ] == '\n'){
                correo[correo.length() -1 ] = '\0';
            }
            receptores+=correo + " ";
        }
    }

    ListaActividades.close();

    std::cout<<"Introduzca el asunto del correo\n";
    std::getline(std::cin, asunto);
    if(asunto==""){
        std::cout<<"\033[1;31mEl asunto no puede estar vacío\033[1;31m\n";
        user.mostrarMenu();
    }
    //quitamos la \n final
    if(asunto[asunto.length() -1 ] == '\n'){
        asunto[asunto.length() -1 ] = '\0';
    }

    std::cout<<"Introduzca el cuerpo del correo. Recuerde que debe ser sin saltos de línea\n";
    std::getline(std::cin, mensaje);
    if(mensaje==""){
        std::cout<<"\033[1;31mEl mensaje no puede estar vacío\033[1;31m\n";
        user.mostrarMenu();
    }
    //quitamos la \n final
    if(mensaje[mensaje.length() -1 ] == '\n'){
        mensaje[mensaje.length() -1 ] = '\0';
    }

    //se han recogido todos los datos necesarios para mandar el correo, ahora se plasma en el fichero Correos.txt
    //hay que abrir el fichero de correos para añadir e introducir el correo
    std::ofstream correos("Correos.txt", std::ios::app);
    fallo_fichero(correos);
    correos<<"Remitente: " + user.GetCorreo() + "\n";
    correos<<"Receptores: " + receptores + "\n";
    correos<<"Asunto: " + asunto + "\n";
    correos<<"Mensaje: " + mensaje + "\n";

    correos.close();
    std::cout<<"\n\033[1;32mSe ha enviado el correo correctamente\033[0m\n";
}



void difusion_carrera(Usuario &user){
    int opcion;
    struct usuario1 u;
    std::string correo, receptores, asunto, mensaje;
    Carrera carrera;
    std::cout<<"Seleccione la carrera que desee\n";
    std::cout<<"1. Ingenieria Informatica\n2. Ingenieria Mecanica\n3. Ingenieria Electrica\n4. Ingenieria Electronica\n";
    std::cout<<"5. Matematicas\n6. ADE\n7. Fisica\n8. Quimica\n";

    if(std::cin>>opcion){
    }
    else{
        std::cout<<"\033[1;31mERROR, entrada no válida\033[1;31m\n";
        exit(EXIT_FAILURE);
    }

    switch(opcion){
        case 1:
            carrera=Carrera::Ingenieria_Informatica;
            break;
        case 2:
            carrera=Carrera::Ingenieria_Mecanica;
            break;
        case 3:
            carrera= Carrera::Ingenieria_Electrica;
            break;
        case 4:
            carrera=Carrera::Ingenieria_Electronica;
            break;
        case 5:
            carrera=Carrera::Matematicas;
            break;
        case 6:
            carrera=Carrera::ADE;
            break;
        case 7:
            carrera= Carrera::Fisica;
            break;
        case 8:
            carrera=Carrera::Quimica;
            break;
        default:
            std::cout<<"\033[1;31mOpción no válida\033[0m\n";
            user.mostrarMenu();
            break;
    }

    std::ifstream ListaActividades("ListaActividades.txt");
    while(leerStrUser(ListaActividades, u)){
        if(u.carrera==carrera){
            correo=u.correo;
            if(correo[correo.length() -1 ] == '\n'){
                correo[correo.length() -1 ] = '\0';
            }
            receptores+=correo + " ";
        }
    }

    ListaActividades.close();

    std::cout<<"Introduzca el asunto del correo\n";
    std::getline(std::cin, asunto);
    if(asunto==""){
        std::cout<<"\033[1;31mEl asunto no puede estar vacío\033[1;31m\n";
        user.mostrarMenu();
    }
    //quitamos la \n final
    if(asunto[asunto.length() -1 ] == '\n'){
        asunto[asunto.length() -1 ] = '\0';
    }

    std::cout<<"Introduzca el cuerpo del correo. Recuerde que debe ser sin saltos de línea\n";
    std::getline(std::cin, mensaje);
    if(mensaje==""){
        std::cout<<"\033[1;31mEl mensaje no puede estar vacío\033[1;31m\n";
        user.mostrarMenu();
    }
    //quitamos la \n final
    if(mensaje[mensaje.length() -1 ] == '\n'){
        mensaje[mensaje.length() -1 ] = '\0';
    }

    //se han recogido todos los datos necesarios para mandar el correo, ahora se plasma en el fichero Correos.txt
    //hay que abrir el fichero de correos para añadir e introducir el correo
    std::ofstream correos("Correos.txt", std::ios::app);
    fallo_fichero(correos);
    correos<<"Remitente: " + user.GetCorreo() + "\n";
    correos<<"Receptores: " + receptores + "\n";
    correos<<"Asunto: " + asunto + "\n";
    correos<<"Mensaje: " + mensaje + "\n";

    correos.close();
    std::cout<<"\n\033[1;32mSe ha enviado el correo correctamente\033[0m\n";
}