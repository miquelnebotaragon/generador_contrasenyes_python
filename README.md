<h1 align="center"><b>Generador contrasenyes amb Python</b></h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://www.gnu.org/licenses/gpl-3.0.html" target="_blank">
    <img alt="License: GPL--3+" src="https://img.shields.io/badge/License-GPL--3+-yellow.svg" />
  </a>
  <a href="https://twitter.com/miquelnebot" target="_blank">
    <img alt="Twitter: Miquel Nebot" src="https://img.shields.io/twitter/follow/miquelnebot.svg?style=social" />
  </a>
</p>
<div align="center"><img src="https://user-images.githubusercontent.com/57944755/210279972-392516c7-5147-472a-9325-21bab75d3b9c.png"></div>

# 👁️‍🗨️ Introducció

Generador de contrasenyes amb Python.

# 💻 Escenari
Kubuntu 22.04

# 0️⃣ Abans de començar
1. Haurem de tenir instal·lat Python en el nostre ordinador. Verificarem si disposam d'ell i la seva versió mitjançant la comanda següent a dins el Terminal (Ctrl+Alt+T): 

```console
user@kubuntu-mnebot:~$ python3 -V
```
Si no el tenim instal·lat, el podem aconseguir fàcilment mitjançant la comanda:
```console
user@kubuntu-mnebot:~$ sudo apt install python3
```
2. Per a la importació del mòduls necessaris (**random**) és imprescindible disposar al nostre ordinador de l'administrador de paquets **PIP**, per això, i si no ho hem fet amb anterioritat, l'instal·larem a través de la terminal de la següent maner
```console
user@kubuntu-mnebot:~$ sudo apt install python3-pip
```
3. Instal·larem finalment els mòduls necessaris responsables de generar el codi QR sol·licitat:
```console
user@kubuntu-mnebot:~$ sudo pip install random
```

# 👇 Descàrrega i execució
Copiarem el codi següent 👇 a un arxiu amb extensió **.py** al nostre ordinador (per exemple **generar_qr_python.py**) per a la seva posterior execució: 
<p></p>📝 Descàrrega de l'arxiu .py des d'<a href="" target="_blank">aquí</a>.

# 🏆 Vull saber-ne més
Desglosam el codi:
## Part 1:
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Mòduls a importar:
import random


# Presentació:
print('\nBenvinguts al generador automàtic de contrasenyes!\n')

# Variables:
caracters_windows = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~@#_/+:'
caracters_linux = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~@#_^*%/.+:;='
numero_contrasenyes = int(input('Quantes contrasenyes vols generar? '))
numero_caracters = int(input('Introdueix la llargària (número) de caràcters que vols que tengui... '))
so = int(input('Finalment, és una contrasenya a emprar a un sistema Windows (1) o Linux (2)? (Si no ho tens clar tria l\'opció 1) '))

```
## Part 2:

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
```

# ➕ Informació
1️⃣ L'arxiu **.py** ha estat comentat al detall (#) per tal de possibilitar l'anàlisi del seu funcionament.<p></p>
2️⃣ Aquesta aplicació ha estat creada únicament amb finalitat d'estudi i divulgació. No em faig responsable dels possibles problemes ni prejudicis que pugui provocar el seu ús.<p></p>
