# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 12:57:13 2021

Nombre: Gustavo Reyes Herrera
RUT: oculto

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""

rut = input("Ingrese un RUT para calcular su dígito verificador: ")
rut = int(rut)

y = 0

# Extraemos cada dígito del RUT obtenido anteriormente (tope 8 dígitos)
separa8 = rut % 10  # Extraemos el octavo dígito
separa7 = (rut // 10) % 10  # Extraemos el septimo dígito
separa6 = (rut // 100) % 10  # Extraemos el sexto dígito
separa5 = (rut // 1000) % 10  # Extraemos el quinto dígito
separa4 = (rut // 10000) % 10  # Extraemos el cuarto dígito
separa3 = (rut // 100000) % 10  # Extraemos el tercer dígito
separa2 = (rut // 1000000) % 10  # Extraemos el segundo dígito
separa1 = (rut // 10000000) % 10  # Extraemos el primer dígito

# Aplicamos fórmula para calcular el dígito verificador
verificador = (separa8 * 2) + (separa7 * 3) + (separa6 * 4) + (separa5 * 5) + \
    (separa4 * 6) + (separa3 * 7) + (separa2 * 2) + (separa1 * 3)
verificador = verificador % 11
verificador = 11 - verificador

# Comparamos el resultado del dígito verificador para clasificar de la siguiente manera:
if (verificador == 11):
    # Si el resultado es 11, el dígito verificador será 0 (cero).
    verificador = 0
    print(f'El dígito verificador de este RUT es: {verificador}')
elif (verificador == 10):
    # Si el resultado es 10, el dígito verificador será K.
    verificador = "K"
    print(f'El dígito verificador de este RUT es: {verificador}')
else:
    # En otro caso, el resultado será el propio dígito verificador.
    print(f'El dígito verificador de este RUT es: {verificador}')
