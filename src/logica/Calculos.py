print("Seleccioné del opcion del 1 al 3: ")
print("1. Ingreso sus datos")
print("2. Calculo de sueldo a pagar")
print("3. Imprime boleta")
opcion = input("Ingrese opcion: ")
if opcion == "1":
    nombreTrabajador = input("Ingrese su nombre: ")
    sueldoBasico = float(input("ingrese su sueldo basico: "))
    diasFalta = float(input("ingrese la cantidad de dias que falto: "))
    minutosTarde = float(input("ingrese la cantidad de minutos de tardanza: "))
    horasExtra = float(input("ingrese la cantdad de horas extra: "))
    pagoHorasExtras = 1.5 * horasExtra * sueldoBasico / 8 / 30
    movilidad = 1000
    bonificacionSuplementaria = 0.03 * sueldoBasico
    bonificaciones = bonificacionSuplementaria + movilidad + pagoHorasExtras
    remunercionCompuable = sueldoBasico + bonificacionSuplementaria + movilidad
    remuneracionMinima = sueldoBasico + bonificaciones
    descuentoFaltas = remunercionCompuable / 30 * diasFalta
    descuentoTardanza = remunercionCompuable / 30 / 8 / 60 * minutosTarde
    descuentos = descuentoFaltas + descuentoTardanza
    SueldoNeto = sueldoBasico + bonificaciones - descuentos

if opcion ==3:
    print(f"señor(a) {nombreTrabajador} su sueldo a pagar es {SueldoNeto}")
    print(f"Tiene bonificaciones igual a: {bonificaciones}")
    print(f"Tiene descuentos igual a: {descuentos}")
