def calcular_horas(horario):
    """
    Esta función toma una cadena de horario de trabajo y calcula la hora de inicio y la duración del trabajo en horas.

    Parámetros:
    horario (str): Una cadena que representa el horario de trabajo en formato "HH:MM-HH:MM".

    Retorna:
    hora_de_inicio (int): La hora de inicio del trabajo.
    duracion_en_horas (float): La duración del trabajo en horas, con minutos convertidos a una fracción de hora.

    Ejemplo:
    >>> calcular_horas("08:30-17:00")
    (8, 8.5)
    """

    hora_de_inicio = int(horario.split('-')[0].split(':')[0])
    minuto_de_inicio = int(horario.split('-')[0].split(':')[1])

    hora_de_finalizacion = int(horario.split('-')[1].split(':')[0])
    minuto_de_finalizacion = int(horario.split('-')[1].split(':')[1])

    duracion_en_horas = (hora_de_finalizacion - hora_de_inicio) + ((minuto_de_finalizacion - minuto_de_inicio) / 60)
    
    return hora_de_inicio, duracion_en_horas

def calcular_pago(file):
    """
    Esta función calcula el pago total para cada empleado en función de sus horarios de trabajo.

    Parámetros:
    file (str): Una cadena que representa las horas trabajadas de cada empleado en un formato específico. 
                Cada línea representa un empleado y su horario en diferentes días de la semana. 
                Ejemplo: "JOHN=MO10:00-14:00,TH12:00-14:00,SU20:00-21:00".

    Retorna:
    pagos (dict): Un diccionario que contiene los nombres de los empleados como claves y el monto a pagar como valor.

    Ejemplo:
    >>> calcular_pago("JOHN=MO10:00-14:00,TH12:00-14:00,SU20:00-21:00")
    {'JOHN': 250}
    """
    
    pagos = {}
    tarifas = {
        'week': [25, 15, 20],
        'weekend': [30, 20, 25]
    }

    for employ in file.split('\n'):
        pago_total = 0
        
        empleados_horario = employ.split('=')
        nombre = empleados_horario[0]

        horarios_trabajado = {horario[:2]: horario[2:] for horario in empleados_horario[1].split(',')}

        for dia, horario in horarios_trabajado.items():

            hora_de_inicio, duracion_en_horas = calcular_horas(horario)
            
            if dia in ['MO', 'TU', 'WE', 'TH', 'FR']:
                if 0 <= hora_de_inicio < 9:
                    pago_total += duracion_en_horas * tarifas['week'][0]
                elif 9 <= hora_de_inicio < 18:
                    pago_total += duracion_en_horas * tarifas['week'][1]
                elif 18 <= hora_de_inicio:
                    pago_total += duracion_en_horas * tarifas['week'][2]
            elif dia in ['SA','SU']:
                if 0 <= hora_de_inicio < 9:
                    pago_total += duracion_en_horas * tarifas['weekend'][0]
                elif 9 <= hora_de_inicio < 18:
                    pago_total += duracion_en_horas * tarifas['weekend'][1]
                elif 18 <= hora_de_inicio:
                    pago_total += duracion_en_horas * tarifas['weekend'][2]

        pagos[nombre] = pago_total

    return pagos

def main():

    try:

        with open("data.txt", 'r') as f:
            contenido = f.read()
            pagos = calcular_pago(contenido)
            for empleado, pago in pagos.items():
                print(f"El monto a pagar de {empleado} es: {pago} USD")
    except (FileNotFoundError, IOError) as e:
        print(f"Error al leer el archivo: {e}")


if __name__ == "__main__":
    # Esto se ejecuta solo cuando se llama directamente al archivo
    main()


    