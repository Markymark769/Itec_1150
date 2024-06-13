"""
Mark Porraz, 4/9/2023, estupido.py
This program runs a loop created by the while true statement.
This program is identical to idiot.py, however putting things in
another language requires validation.
"""

import pyinputplus as pyip

while True:

    #You can also make use of the inputYesNo() function in non-English
    # languages by passing yesVal and noVal keyword arguments.
    prompt = '¿Quieres saber cómo mantener ocupado a un idiota durante horas?\n'
    response = pyip.inputYesNo(prompt, yesVal='sí', noVal='no')
    if response == 'no':
        break

print('Gracias. Que Tenga un Ben Dia.')