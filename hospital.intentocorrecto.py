import json
import os

def datos_pacientes():
    datos_paciente = {}
    datos_paciente['nombre'] = input("Ingrese el nombre del paciente: ")
    datos_paciente['apellido'] = input("Ingrese el apellido del paciente: ")
    datos_paciente['edad'] = input("Ingrese la edad del paciente: ")
    datos_paciente['rut'] = input("Ingrese el RUT del paciente: ")
    datos_paciente['sexo'] = input("Ingrese el sexo del paciente: ")
    datos_paciente['telefono'] = input("Ingrese el teléfono del paciente: ")
    datos_paciente['sangre'] = input("Ingrese el tipo de sangre del paciente: ")
    datos_paciente['razon'] = input("Ingrese la razón de la consulta: ")
    datos_paciente['medicamentos'] = input("Ingrese los medicamentos a recetar: ")
    return datos_paciente

def borrar_json(info_pacientes):
    if os.path.exists(info_pacientes):
        os.remove(info_pacientes)
        print(f"Archivo {info_pacientes} eliminado")
    else:
        print(f"El archivo {info_pacientes} ya se elimino o no existe")

opc =0

while opc != 6:


    opc = int(input("MENU\n1-ingresar ficha de paciente\n2-buscar ficha por rut\n3-buscar medicamentos por rut\n4-eliminar ficha del paciente\n5-lista de pacientes atendidos\n6-salir\nopcion: "))
    
    if opc ==1:
        if opc == 1:
            datos_paciente = datos_pacientes()
        datos_json = json.dumps(datos_paciente)

        with open('datos_paciente.json', 'w') as info_pacientes:
            json.dump(datos_paciente, info_pacientes)
        
        print("Datos del paciente")

    elif opc == 2:
        rut_buscar = input("Ingrese el RUT del paciente: ")
        with open('datos_paciente.json', 'r') as info_pacientes:
            datos = json.load(info_pacientes)
            if datos['rut'] == rut_buscar:
                print("Datos del paciente:")
                for key, value in datos.items():
                    print(f"{key}: {value}")
            else:
                print("rut incorrecto/ no se encontro")

    elif opc == 3:
        rut_buscar = input("Ingrese el RUT del paciente a buscar: ")
        with open('datos_paciente.json', 'r') as info_pacientes:
            datos = json.load(info_pacientes)
            if datos['rut'] == rut_buscar:
                print(f"Medicamentos recetados: {datos['medicamentos']}")
            else:
                print("rut incorrecto/ no se encontro")

    elif opc == 4:
        nombre_buscar = input("ingrese nombre del paciente: ")
        with open('datos_paciente.json', 'r' )as info_pacientes:
            datos = json.load(info_pacientes)
            if 'nombre' in datos and datos['nombre'] ==nombre_buscar:
                borrar_json('datos_paciente.json')
            print(f"los datos del paciente {nombre_buscar} fueron borrados")
            
            
      


       
    
    else:
        print("Opción no válida")

        
       
    


