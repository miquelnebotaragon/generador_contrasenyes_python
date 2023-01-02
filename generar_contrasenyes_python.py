#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Mòduls a importar:
import random

# Presentació:
print('\nBenvinguts al generador automàtic de contrasenyes!\n')

# Variables:
caracters_windows = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~@#_/+:' # Més informació https://ibm.co/3jFcXlj
caracters_linux = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~@#_^*%/.+:;=' 
numero_contrasenyes = int(input('Quantes contrasenyes vols generar? ')) 
numero_caracters = int(input('Introdueix la llargària (número) de caràcters que vols que tengui... '))
so = int(input('Finalment, és una contrasenya a emprar a un sistema Windows (1) o Linux (2)? (Si no ho tens clar tria l\'opció 1) '))


# Execució:
if so == 1:
    for password_index in range(numero_contrasenyes):
        contrasenyes = ""
        
        for index in range(numero_caracters):
            contrasenyes = contrasenyes + random.choice(caracters_windows)
        
        print("{}".format(contrasenyes))
    
elif so == 2:
    for password_index in range(numero_contrasenyes):
        contrasenyes = ""
        
        for index in range(numero_caracters):
            contrasenyes = contrasenyes + random.choice(caracters_linux)
        
        print("{}".format(contrasenyes))

else:
   print('Opció escollida desconeguda. Torna a repetir el procés!')
