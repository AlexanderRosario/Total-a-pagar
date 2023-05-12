week = ['MO', 'TU', 'WE', 'TH', 'FR']
weekend = ['SA','SU']

def calcular_pago(file):
    pagos = {}

    for employ in file.split('\n'):
        pago_total = 0

        empleados_horario = employ.split('=')
        nombre = empleados_horario[0]

        horarios_trabajado = {horario[:2]: horario[2:] for horario in empleados_horario[1].split(',')}

        for dia, horario in horarios_trabajado.items():

            hora_de_inicio = int(horario.split('-')[0].split(':')[0])
            minuto_de_inicio = int(horario.split('-')[0].split(':')[1])

            hora_de_finalizacion = int(horario.split('-')[1].split(':')[0])
            minuto_de_finalizacion = int(horario.split('-')[1].split(':')[1])

            duracion_en_horas = (hora_de_finalizacion - hora_de_inicio) + ((minuto_de_finalizacion - minuto_de_inicio) / 60)
            
            if dia in week:

                print(dia,duracion_en_horas, hora_de_inicio)
               
                if 0 < hora_de_inicio < 9:
                    pago_total += duracion_en_horas * 25
                    
                elif 9 <= hora_de_inicio < 18:
                    pago_total += duracion_en_horas * 15
                
                elif 18 <= hora_de_inicio:
                    pago_total += duracion_en_horas * 20
            
            elif dia in weekend:
            
                if 0 < hora_de_inicio < 9:
                    pago_total += duracion_en_horas * 30
            
                elif 9 < hora_de_inicio < 18:
                    pago_total += duracion_en_horas * 20
            
                elif 18 <= hora_de_inicio:
                    pago_total += duracion_en_horas * 25


        pagos[nombre] = pago_total

    return pagos

archivo = "data.txt"  # Ruta y nombre del archivo que deseas leer

try:
    with open(archivo, 'r') as f:
        contenido = f.read()
except FileNotFoundError:
    print("No se pudo encontrar el archivo:", archivo)
except IOError:
    print("Error al leer el archivo:", archivo)

pagos = calcular_pago(contenido)
for empleado, pago in pagos.items():
    print(f"El monto a pagar de {empleado} es: {pago} USD")
