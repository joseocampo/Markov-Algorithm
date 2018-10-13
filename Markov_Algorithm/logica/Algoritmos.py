from logica.Ventana import * 

def markovAlgorim(cadena, reglas):
        reglaTerminal = False; 

        i = 0;
        esAplicable = False;  # Valida si una regla es aplicable
        posicion = -1;  # Posicion donde se va a sustituir
        sustitucion = "";  # Parte de la cadena que se sustituye
        buscado = 0;
        while (reglaTerminal != True | i <= reglas.__len__()):  # Se busca en todas las reglas o hasta que haye una terminal
            regla = reglas[i];  # regla actual
            patron = regla[0];
            
            if cadena.__contains__(patron):  # Si la cadena contiene al patron se busca donde lo tiene
                esAplicable = True;
                
                for j in range(cadena.__len__()):  # Recorre la cadena para buscar el patron
                    
                    if cadena[j] == patron[0]:
                        posicion = j;
                        for x in range(patron.__len__()):  # Recorre el patron 
                            if cadena[j + x] != patron[x]:
                                buscado = 0;
                                break;
                            else:
                                buscado += 1;
                    if buscado == patron.__len__():
                        break;
                if esAplicable:
                    sustitucion = regla[1];
                    parteIzquierda = cadena[:posicion];
                    parteDerecha = cadena[posicion + patron.__len__():];
                    cadena = parteIzquierda + sustitucion + parteDerecha;
                    esAplicable = False;
                    buscado = 0;
                    i=0;
                    if regla.__len__() == 3:
                            if regla[2] == ".":
                                reglaTerminal = True;
                            else:
                                continue;
            else:
                esAplicable = False;
                i += 1;
            
        return cadena;