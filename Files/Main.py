# Proyecto Integrador
# Alexei Delgado De Gante A01637405
# Francisco Mustico A00344930

# Library Imports
import sys

from time import sleep
import pandas as pd
import webbrowser
import random
import os
clear = lambda: os.system('clear')
clear()


def main():

    print("\nBienvenido! "
    "En este programa podrás poner a prueba tus conocimientos en matemáticas para prepararte para tu prueba\n")

    print('El programa cuenta con los siguientes temas para practicar \n')

    opciones_tema = ['Tutorial', 'Tema 1: Aritmética', 'Tema 2: Álgebra',
                        'Tema 3: Trigonometría', 'Tema 4: Geometría', 'Tema 5: Funciones',
                        'Repaso General', 'Salir']

    opciones_sel = ['(ingrese 0 para seleccionar)', '(ingrese 1 para seleccionar)',
                        '(ingrese 2 para seleccionar)', '(ingrese 3 para seleccionar)',
                        '(ingrese 4 para seleccionar)', '(ingrese 5 para seleccionar)',
                        '(ingrese 6 para seleccionar)', '(ingrese 7 para seleccionar)']

    df_opciones = pd.DataFrame()
    df_opciones['tema'] = opciones_tema
    df_opciones['input'] = opciones_sel
    print(df_opciones)

    print('\nPara consultar el módulo de ayuda, solo escriba “ayuda” en el '
            'espacio de respuesta dentro del tema que se está evaluando')

    print('Para hacer tu selección, introduce el número de opción a ejecutar, '
            'si es tu primera vez utilizando el programa inicia con el tutorial! \n ')

    opc = 0
    while True:
        try:
            opc = int(input('Introduce el número de tema deseado para practicar: '))
            if opc in range(0, 9):
                break
            else:
                print('Error, El programa solo contiene 8 opciones para seleccionar')
                continue
        except ValueError:
            print('Error, asegurese que su respuesta sea numérica correspondiente a la opción que quiere ejecutar')
            continue

    if opc == 0:
        init_math.tutorial()
    elif opc == 1:
        init_math.aritmetica()
    elif opc == 2:
        init_math.algebra()
    elif opc == 3:
        init_math.trigonometria()
    elif opc == 4:
        init_math.geometria()
    elif opc == 5:
        init_math.funciones()
    elif opc == 6:
        init_math.repaso_general()
    elif opc == 7:
        print('\n¡Gracias por utilizar el programa!')
    elif opc == 8:
        print('\n¡Encontraste los creditos!\nEste programa fue elaborado por: \nAlexei Delgado De Gante '
              'y \nFrancisco Mustico')
    else:
        print('Error asegurese de introducir el número correspondiente a la opción que quiere ejecutar')


class Retroalimentacion:

    # Mod variables are used by the program to know from what part of the program it was called

    @staticmethod
    def feedback_to_user(mod, tema):
        global respuestas_correctas
        porcentaje_dominio = (respuestas_correctas * 100)/9
        print('Ha concluido tu evaluación')
        print(f'Tu nivel de dominio del tema {mod} es de {porcentaje_dominio:.2f}%\n')

        # recommended study plan based on performance
        if porcentaje_dominio < 33.34:
            print(f'Se recomienda estudiar el tema {tema} de {mod}\n')
        elif porcentaje_dominio < 66.67:
            print(f'Se recomienda estudiar el tema {tema} de {mod}\n')
        elif porcentaje_dominio <= 99.99:
            print(f'Se recomienda estudiar el tema {tema} de {mod}\n')
        elif porcentaje_dominio == 100:
            print(f'Felicidades! ha dominado el tema de {mod}\n')

        # Practice more option
        print('Deseas intentar de nuevo?')
        continue_option = str.lower(input('Escribe "si" para continuar, Escribe "no" para finalizar\n'))
        if continue_option == 'si':
            respuestas_correctas = 0
            main()
        else:
            sys.exit()

    @staticmethod
    def evaluate_gral():
        global respuestas_correctas
        porcentaje_dominio = (respuestas_correctas * 100) / 5
        print('Ha concluido tu evaluación')
        print(f'Tu nivel de dominio de los temas es de {porcentaje_dominio:.2f}%\n')
        pass

    def help(self, mod):

        print('\nBienvenido al módulo de ayuda!\n')
        print(f'Para el tema de {mod} te recomendamos consultar el siguiente link: ')

        if mod == "aritmetica":
            print('Deseas abrir el link de ayuda?')
            open_link = str.lower(input('\nEscribe "si" para abrir el link, Escribe "no" para continuar: '))

            if open_link == 'si':
                webbrowser.open('https://es.khanacademy.org/math/arithmetic')
                print('Desea regresar a el módulo de evaluación?')
                return_to_problem = str.lower(
                    input('\nEscribe "si" para regresar, Escribe "no" para finalizar el programa: '))

                if return_to_problem == 'si':
                    print('\nRegresando...\n')
                    pass
                else:
                    print('Gracias por utilizar el programa!')
                    sys.exit()

            elif open_link == 'no':
                print('Desea regresar a el módulo de evaluación?')
                return_to_problem = str.lower(input('\nEscribe "si" para regresar, Escribe "no" para finalizar el programa: '))

                if return_to_problem == 'si':
                    print('\nRegresando...\n')
                    pass
                else:
                    print('Gracias por utilizar el programa!')
                    sys.exit()

        elif mod == 'tutorial':
            print('Así se vera el módulo de ayuda que te proveerá con un link de ayuda'
                    ' y podrás decidir si continuar practicando o terminar tu intento')
            sleep(4)
            pass

        elif mod == 'algebra':
            print('Deseas abrir el link de ayuda?')
            open_link = str.lower(input('\nEscribe "si" para abrir el link, Escribe "no" para continuar: '))

            if open_link == 'si':
                webbrowser.open('https://es.khanacademy.org/math/algebra')
                print('Desea regresar a el módulo de evaluación?')
                return_to_problem = str.lower(
                    input('\nEscribe "si" para regresar, Escribe "no" para finalizar el programa: '))

                if return_to_problem == 'si':
                    print('\nRegresando...\n')
                    pass
                else:
                    print('Gracias por utilizar el programa!')
                    sys.exit()

            elif open_link == 'no':
                print('Desea regresar a el módulo de evaluación?')
                return_to_problem = str.lower(
                    input('\nEscribe "si" para regresar, Escribe "no" para finalizar el programa: '))

                if return_to_problem == 'si':
                    print('\nRegresando...\n')
                    pass
                else:
                    print('Gracias por utilizar el programa!')
                    sys.exit()

        elif mod == 'trigonometria':
            print('Deseas abrir el link de ayuda?')
            open_link = str.lower(input('\nEscribe "si" para abrir el link, Escribe "no" para continuar: '))

            if open_link == 'si':
                webbrowser.open('https://es.khanacademy.org/math/trigonometry')
                print('Desea regresar a el módulo de evaluación?')
                return_to_problem = str.lower(
                    input('\nEscribe "si" para regresar, Escribe "no" para finalizar el programa: '))

                if return_to_problem == 'si':
                    print('\nRegresando...\n')
                    pass
                else:
                    print('Gracias por utilizar el programa!')
                    sys.exit()

            elif open_link == 'no':
                print('Desea regresar a el módulo de evaluación?')
                return_to_problem = str.lower(
                    input('\nEscribe "si" para regresar, Escribe "no" para finalizar el programa: '))

                if return_to_problem == 'si':
                    print('\nRegresando...\n')
                    pass
                else:
                    print('Gracias por utilizar el programa!')
                    sys.exit()

        elif mod == 'geometria':
            print('Deseas abrir el link de ayuda?')
            open_link = str.lower(input('\nEscribe "si" para abrir el link, Escribe "no" para continuar: '))

            if open_link == 'si':
                webbrowser.open('https://es.khanacademy.org/math/geometry/hs-geo-analytic-geometry')
                print('Desea regresar a el módulo de evaluación?')
                return_to_problem = str.lower(
                    input('\nEscribe "si" para regresar, Escribe "no" para finalizar el programa: '))

                if return_to_problem == 'si':
                    print('\nRegresando...\n')
                    pass
                else:
                    print('Gracias por utilizar el programa!')
                    sys.exit()

            elif open_link == 'no':
                print('Desea regresar a el módulo de evaluación?')
                return_to_problem = str.lower(
                    input('\nEscribe "si" para regresar, Escribe "no" para finalizar el programa: '))

                if return_to_problem == 'si':
                    print('\nRegresando...\n')
                    pass
                else:
                    print('Gracias por utilizar el programa!')
                    sys.exit()

        elif mod == 'funciones':
            print('Deseas abrir el link de ayuda?')
            open_link = str.lower(input('\nEscribe "si" para abrir el link, Escribe "no" para continuar: '))

            if open_link == 'si':
                webbrowser.open('https://es.khanacademy.org/math/algebra-home/alg-functions')
                print('Desea regresar a el módulo de evaluación?')
                return_to_problem = str.lower(
                    input('\nEscribe "si" para regresar, Escribe "no" para finalizar el programa: '))

                if return_to_problem == 'si':
                    print('\nRegresando...\n')
                    pass
                else:
                    print('Gracias por utilizar el programa!')
                    sys.exit()

            elif open_link == 'no':
                print('Desea regresar a el módulo de evaluación?')
                return_to_problem = str.lower(
                    input('\nEscribe "si" para regresar, Escribe "no" para finalizar el programa: '))

                if return_to_problem == 'si':
                    print('\nRegresando...\n')
                    pass
                else:
                    print('Gracias por utilizar el programa!')
                    sys.exit()


# class object math functions
class Math:

    # static method or function for tutorial
    @staticmethod
    def tutorial():

        # Argument for module 'aritmetica' to recognize where the program is
        mod = 'tutorial'

        tema = 'Tutorial'
        num_pregunta = 1
        attempt = 0
        pregunta = '¿Cuanto es 2 + 2?'

        print("\nBienvenido al tutorial!\n")
        sleep(2)

        print('En los módulos de evaluación así se verán las preguntas\n')

        print(f'\nTema: {tema}, \t Pregunta número {num_pregunta}, \t Intento número {attempt+1}\n')
        print(pregunta)
        print('Respuesta: en este espacio escribes tu respuesta\n')

        sleep(3)

        print('Tambíen podrás solicitar ayuda en el tema seleccionado simplemente escribiendo ‘'
            'ayuda’ en el espacio de Respuesta de la siguiente manera ')
        print('Respuesta: ayuda\n')

        sleep(2)

        print('Cada tema contiene 3 subtemas principales que comprenden el aréa  a evaluar')
        sleep(2)
        print('Se evaluarán 3 preguntas por subtema y Tendrás 3 intentos por pregunta\n')

        sleep(3)
        print('Intenta responder la siguiente pregunta o llamar el módulo de ayuda\n')

        # answer validation
        print(f'\nTema: {tema}, \t Pregunta número {num_pregunta}, \t Intento número {attempt+1}\n')
        print(pregunta)
        respuesta = input('Respuesta: ')

        if respuesta == '4':
            print('\nRespuesta Correcta!')
        elif respuesta == 'ayuda':
            init_feedback.help(mod)
        else:
            print('\nRespuesta Incorrecta')
            attempt += 1

            while attempt < 3:
                print(f'\nTema: {tema}, \t Pregunta número {num_pregunta}, \t Intento número {attempt+1}\n')
                print(pregunta)
                respuesta = input('Respuesta: ')

                if respuesta == '4':
                    print('\nRespuesta Correcta!')
                    break
                else:
                    print('\nRespuesta Incorrecta')
                    attempt += 1
                    continue
        sleep(2)

        print('\nFinalmente para las respuestas que requieran el uso de raíces cuadradas escribe la '
            'respuesta de la siguiente manera')
        print('sqrt( Respuesta )\n')

        sleep(3)

        print('Para expresar fracciones utiliza el carácter / mostrado de la siguiente manera \n'
            '¿Cuánto es 0.50 en fracción? ')
        print('Respuesta: 1/2\n')

        sleep(3)

        print('Para expresar valores o puntos en una gráfica utiliza paréntesis de la siguiente manera')
        print('Respuesta: (x, y)\n')

        sleep(3)

        print('Para expresar el valor de pi simplemente escribe ‘pi’ en tu respuesta')
        print('Respuesta: 23pi/18\n')

        print('Ha concluido el tutorial!\nregresando al menú principal\n')
        main()

    # static method or function for aritmetica
    @staticmethod
    def aritmetica():

        # Argument for module 'aritmetica' to recognize where the program is
        mod = 'aritmetica'

        def subtema_uno_ar():

            global respuestas_correctas

            # answer validation variables
            attempt = 0
            num_pregunta = 1

            # variable to store previous question
            previous_questions = set()

            # legacy DataFrame // still used for print(NombreTema) at start of while loop
            subtema1 = df_preguntas.iloc[0:18, 0:4]
            tema = subtema1.iloc[0, 1]

            # Preguntas subtema 1 :: 3 intentos por pregunta
            while attempt < 3:
                print(f'\nTema: {tema}, \t Pregunta número {num_pregunta}, \t Intento número {attempt+1}\n')

                # Grab random question from pool
                pool = random.randint(0, 17)
                pregunta = subtema1.iloc[pool, 3]

                # check if the question was previously asked
                if pregunta not in previous_questions:
                    # if the question wasn't previously asked add the question to the set
                    previous_questions.add(pregunta)
                    print(pregunta)
                else:
                    # if the question was previously asked (question IS found in the set)
                    # grab another question from pool
                    pool = random.randint(0, 17)
                    pregunta = subtema1.iloc[pool, 3]
                    print(pregunta)

                # grab answer [pool, column] :: usar base de datos completa
                df_respuesta = df_preguntas.iloc[pool, 4]

                # validate numeric answer
                try:
                    respuesta = str.lower(input("Respuesta: "))

                    # validate correct answer
                    if respuesta == df_respuesta:
                        print('\nRespuesta correcta!')
                        # add +1 to number of correct answers
                        num_pregunta += 1
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/9 preguntas')
                        # reset attempts to have 3 attempts per question
                        attempt = 0
                    elif respuesta == 'ayuda':
                        init_feedback.help(mod)

                    elif respuesta == answer_key:
                        print('\n Answer_Key:Pass!')
                        num_pregunta += 1
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/9 preguntas')
                        attempt = 0
                    else:
                        print('\nRespuesta Incorrecta')
                        # if the answer is wrong add one attempt
                        attempt += 1
                except ValueError:
                    print('\nError! Respuesta Incorrecta')
                    # if the input is not numeric add one attempt
                    attempt += 1
                    # if the number of attempts is greater than 3

                if attempt == 3:
                    # call function retroalimentacion()
                    print('\nHas agotado el número máximo de intentos\n')
                    print(f'La respuesta correcta es {df_respuesta}')
                    init_feedback.feedback_to_user(mod, tema)
                    continue

                if num_pregunta > 3:
                    break

            # Call next module
            if num_pregunta > 3:
                subtema_dos_ar()

        def subtema_dos_ar():

            global respuestas_correctas

            # answer validation variables
            attempt = 0
            num_pregunta = 1

            # variable to store previous question
            previous_questions = set()

            # legacy DataFrame // still used for print(NombreTema) at start of while loop
            subtema2 = df_preguntas.iloc[18:34, 0:4]
            tema = subtema2.iloc[0, 1]

            # Preguntas subtema 2 :: 3 intentos por pregunta
            while attempt < 3:
                print(f'\nTema: {tema}, \t Pregunta número {num_pregunta}, \t Intento número {attempt+1}\n')

                # Grab random question from pool
                pool = random.randint(18, 34)
                pregunta = df_preguntas.iloc[pool, 3]

                # check if the question was previously asked
                if pregunta not in previous_questions:
                    # if the question wasn't previously asked add the question to the set
                    previous_questions.add(pregunta)
                    print(pregunta)
                else:
                    # if the question was previously asked (question IS found in the set) grab another question from pool
                    pool = random.randint(18, 34)
                    pregunta = df_preguntas.iloc[pool, 3]
                    print(pregunta)

                # grab answer [pool, column] :: usar base de datos completa
                df_respuesta = df_preguntas.iloc[pool, 4]

                # validate numeric answer
                try:
                    respuesta = str.lower(input("Respuesta: "))
                    # validate correct answer
                    if respuesta == df_respuesta:
                        print('\nRespuesta correcta!')
                        # add +1 to number of correct answers
                        num_pregunta += 1
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/9 preguntas')
                        # reset attempts to have 3 attempts per question
                        attempt = 0
                    elif respuesta == 'ayuda':
                        init_feedback.help(mod)
                    elif respuesta == answer_key:
                        print('\n Answer_Key:Pass!')
                        num_pregunta += 1
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/9 preguntas')
                        attempt = 0
                    else:
                        print('\nRespuesta Incorrecta')
                        # if the answer is wrong add one attempt
                        attempt += 1
                except ValueError:
                    print('\nError! Respuesta Incorrecta')
                    # if the input is not numeric add one attempt
                    attempt += 1
                    # if the number of attempts is greater than 3
                if attempt == 3:
                    # call function retroalimentacion()
                    print('\nHas agotado el número máximo de intentos\n')
                    print(f'La respuesta correcta es {df_respuesta}')
                    init_feedback.feedback_to_user(mod, tema)
                    continue

                if num_pregunta > 3:
                    break

            # Call next module
            if num_pregunta > 3:
                subtema_tres_ar()

        def subtema_tres_ar():

            global respuestas_correctas

            # legacy DataFrame // still used for print(NombreTema) at start of while loop
            subtema3 = df_preguntas.iloc[35:41, :4]
            tema = subtema3.iloc[0, 1]

            # Variables
            attempt = 0
            num_pregunta = 1

            # variable to store previous question
            previous_questions = set()

            # Preguntas subtema 3 :: 3 intentos por pregunta
            while attempt < 3:
                print(f'\nTema: {tema}, \t Pregunta número {num_pregunta}, \t Intento número {attempt+1}\n')

                # Grab random question from pool
                pool = random.randint(35, 41)
                pregunta = df_preguntas.iloc[pool, 3]

                # check if the question was previously asked
                if pregunta not in previous_questions:
                    # if the question wasn't previously asked add the question to the set
                    previous_questions.add(pregunta)
                    print(pregunta)
                else:
                    # if the question was previously asked (question IS found in the set) grab another question from pool
                    pool = random.randint(35, 41)
                    pregunta = df_preguntas.iloc[pool, 3]
                    print(pregunta)

                # grab answer [pool, column] :: usar base de datos completa
                df_respuesta = df_preguntas.iloc[pool, 4]

                # validate numeric answer
                try:
                    respuesta = str.lower(input("Respuesta: "))
                    # validate correct answer
                    if respuesta == df_respuesta:
                        print('\nRespuesta correcta!')
                        # add +1 to number of correct answers
                        num_pregunta += 1
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/9 preguntas')
                        # reset attempts to have 3 attempts per question
                        attempt = 0
                    elif respuesta == 'ayuda':
                        init_feedback.help(mod)
                    elif respuesta == answer_key:
                        print('\n Answer_Key:Pass!')
                        num_pregunta += 1
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/9 preguntas')
                        attempt = 0
                    else:
                        print('\nRespuesta Incorrecta')
                        # if the answer is wrong add one attempt
                        attempt += 1
                except ValueError:
                    print('\nError! Respuesta Incorrecta')
                    # if the input is not numeric add one attempt
                    attempt += 1
                    # if the number of attempts is greater than 3
                if attempt == 3:
                    # call function retroalimentacion()
                    print('\nHas agotado el número máximo de intentos\n')
                    print(f'La respuesta correcta es {df_respuesta}')
                    init_feedback.feedback_to_user(mod, tema)
                    continue

                if num_pregunta > 3:
                    break

            # Call next modul
            if num_pregunta > 3:
                init_feedback.feedback_to_user(mod, tema)

        print(f'\nMódulo seleccionado: {mod}')
        subtema_uno_ar()

    # static method or function for algebra
    @staticmethod
    def algebra():
        # Argument for module 'algebra' to recognize where the program is
        mod = 'algebra'

        def subtema_uno_alg():
            # Standard module builder template
            global respuestas_correctas

            # answer validation variables
            attempt = 0
            num_pregunta = 1

            # variable to store previous question
            previous_questions = set()

            # tema
            tema = df_preguntas.iloc[42, 1]

            # attempt & questions loop
            while attempt < 3:
                print(f'\nTema: {tema}, \t Pregunta número {num_pregunta}, \t Intento número {attempt + 1}\n')

                # Grab random question from pool
                pool = random.randint(42, 56)
                pregunta = df_preguntas.iloc[pool, 3]

                # check if the question was previously asked
                if pregunta not in previous_questions:
                    previous_questions.add(pregunta)
                    print(pregunta)
                else:
                    pool = random.randint(42, 56)
                    pregunta = df_preguntas.iloc[pool, 3]
                    print(pregunta)

                df_respuesta = df_preguntas.iloc[pool, 4]

                # validate answer
                try:
                    respuesta = str.lower(input("Respuesta: "))
                    if respuesta == df_respuesta:
                        print('\nRespuesta correcta!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/9 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    elif respuesta == 'ayuda':
                        init_feedback.help(mod)

                    elif respuesta == answer_key:
                        print('\n Answer_Key:Pass!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/9 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    else:
                        print('\nRespuesta Incorrecta')
                        attempt += 1

                except ValueError:
                    print('\nError! Respuesta Incorrecta')
                    attempt += 1

                if attempt == 3:
                    print('\nHas agotado el número máximo de intentos\n')
                    print(f'La respuesta correcta es {df_respuesta}')
                    init_feedback.feedback_to_user(mod, tema)
                    continue

                if num_pregunta > 3:
                    break

            # Call next module
            if num_pregunta > 3:
                subtema_dos_alg()

        def subtema_dos_alg():
            global respuestas_correctas

            # answer validation variables
            attempt = 0
            num_pregunta = 1

            # variable to store previous question
            previous_questions = set()

            # tema
            tema = df_preguntas.iloc[57, 1]

            # attempt & questions loop
            while attempt < 3:
                print(f'\nTema: {tema}, \t Pregunta número {num_pregunta}, \t Intento número {attempt + 1}\n')

                # Grab random question from pool
                pool = random.randint(57, 71)
                pregunta = df_preguntas.iloc[pool, 3]

                # check if the question was previously asked
                if pregunta not in previous_questions:
                    previous_questions.add(pregunta)
                    print(pregunta)
                else:
                    pool = random.randint(57, 71)
                    pregunta = df_preguntas.iloc[pool, 3]
                    print(pregunta)

                df_respuesta = df_preguntas.iloc[pool, 4]

                # validate answer
                try:
                    respuesta = str.lower(input("Respuesta: "))
                    if respuesta == df_respuesta:
                        print('\nRespuesta correcta!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/9 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    elif respuesta == 'ayuda':
                        init_feedback.help(mod)

                    elif respuesta == answer_key:
                        print('\n Answer_Key:Pass!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/9 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    else:
                        print('\nRespuesta Incorrecta')
                        attempt += 1

                except ValueError:
                    print('\nError! Respuesta Incorrecta')
                    attempt += 1

                if attempt == 3:
                    print('\nHas agotado el número máximo de intentos\n')
                    print(f'La respuesta correcta es {df_respuesta}')
                    init_feedback.feedback_to_user(mod, tema)
                    continue

                if num_pregunta > 3:
                    break

            # Call next module
            if num_pregunta > 3:
                subtema_tres_alg()

        def subtema_tres_alg():
            global respuestas_correctas

            # answer validation variables
            attempt = 0
            num_pregunta = 1

            # variable to store previous question
            previous_questions = set()

            # tema
            tema = df_preguntas.iloc[72, 1]

            # attempt & questions loop
            while attempt < 3:
                print(f'\nTema: {tema}, \t Pregunta número {num_pregunta}, \t Intento número {attempt + 1}\n')

                # Grab random question from pool
                pool = random.randint(72, 86)
                pregunta = df_preguntas.iloc[pool, 3]

                # check if the question was previously asked
                if pregunta not in previous_questions:
                    previous_questions.add(pregunta)
                    print(pregunta)
                else:
                    pool = random.randint(72, 86)
                    pregunta = df_preguntas.iloc[pool, 3]
                    print(pregunta)

                df_respuesta = df_preguntas.iloc[pool, 4]

                # validate answer
                try:
                    respuesta = str.lower(input("Respuesta: "))
                    if respuesta == df_respuesta:
                        print('\nRespuesta correcta!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/9 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    elif respuesta == 'ayuda':
                        init_feedback.help(mod)

                    elif respuesta == answer_key:
                        print('\n Answer_Key:Pass!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/9 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    else:
                        print('\nRespuesta Incorrecta')
                        attempt += 1

                except ValueError:
                    print('\nError! Respuesta Incorrecta')
                    attempt += 1

                if attempt == 3:
                    print('\nHas agotado el número máximo de intentos\n')
                    print(f'La respuesta correcta es {df_respuesta}')
                    init_feedback.feedback_to_user(mod, tema)
                    continue

                if num_pregunta > 3:
                    break

            # Call next module
            if num_pregunta > 3:
                init_feedback.feedback_to_user(mod, tema)

        print(f'\nMódulo seleccionado: {mod}')
        subtema_uno_alg()

    @staticmethod
    def trigonometria():
        # Argument for module 'trigonometria' to recognize where the program is
        mod = 'trigonometria'

        def subtema_uno_trig():
            # Standard module template
            global respuestas_correctas

            # answer validation variables
            attempt = 0
            num_pregunta = 1

            # variable to store previous question
            previous_questions = set()

            # tema
            tema = df_preguntas.iloc[87, 1]

            # attempt & questions loop
            while attempt < 3:
                print(f'\nTema: {tema}, \t Pregunta número {num_pregunta}, \t Intento número {attempt + 1}\n')

                # Grab random question from pool
                pool = random.randint(87, 101)
                pregunta = df_preguntas.iloc[pool, 3]

                # check if the question was previously asked
                if pregunta not in previous_questions:
                    previous_questions.add(pregunta)
                    print(pregunta)
                else:
                    pool = random.randint(87, 101)
                    pregunta = df_preguntas.iloc[pool, 3]
                    print(pregunta)

                df_respuesta = df_preguntas.iloc[pool, 4]

                # validate answer
                try:
                    respuesta = str.lower(input("Respuesta: "))
                    if respuesta == df_respuesta:
                        print('\nRespuesta correcta!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/9 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    elif respuesta == 'ayuda':
                        init_feedback.help(mod)

                    elif respuesta == answer_key:
                        print('\n Answer_Key:Pass!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/9 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    else:
                        print('\nRespuesta Incorrecta')
                        attempt += 1

                except ValueError:
                    print('\nError! Respuesta Incorrecta')
                    attempt += 1

                if attempt == 3:
                    print('\nHas agotado el número máximo de intentos\n')
                    print(f'La respuesta correcta es {df_respuesta}')
                    init_feedback.feedback_to_user(mod, tema)
                    continue

                if num_pregunta > 3:
                    break

            # Call next module
            if num_pregunta > 3:
                subtema_dos_trig()

        def subtema_dos_trig():
            # Standard module template
            global respuestas_correctas

            # answer validation variables
            attempt = 0
            num_pregunta = 1

            # variable to store previous question
            previous_questions = set()

            # tema
            tema = df_preguntas.iloc[102, 1]

            # attempt & questions loop
            while attempt < 3:
                print(f'\nTema: {tema}, \t Pregunta número {num_pregunta}, \t Intento número {attempt + 1}\n')

                # Grab random question from pool
                pool = random.randint(102, 116)
                pregunta = df_preguntas.iloc[pool, 3]

                # check if the question was previously asked
                if pregunta not in previous_questions:
                    previous_questions.add(pregunta)
                    print(pregunta)
                else:
                    pool = random.randint(102, 116)
                    pregunta = df_preguntas.iloc[pool, 3]
                    print(pregunta)

                df_respuesta = df_preguntas.iloc[pool, 4]

                # validate answer
                try:
                    respuesta = str.lower(input("Respuesta: "))
                    if respuesta == df_respuesta:
                        print('\nRespuesta correcta!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/9 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    elif respuesta == 'ayuda':
                        init_feedback.help(mod)

                    elif respuesta == answer_key:
                        print('\n Answer_Key:Pass!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/9 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    else:
                        print('\nRespuesta Incorrecta')
                        attempt += 1

                except ValueError:
                    print('\nError! Respuesta Incorrecta')
                    attempt += 1

                if attempt == 3:
                    print('\nHas agotado el número máximo de intentos\n')
                    print(f'La respuesta correcta es {df_respuesta}')
                    init_feedback.feedback_to_user(mod, tema)
                    continue

                if num_pregunta > 3:
                    break

            # Call next module
            if num_pregunta > 3:
                subtema_tres_trig()

        def subtema_tres_trig():
            # Standard module template
            global respuestas_correctas

            # answer validation variables
            attempt = 0
            num_pregunta = 1

            # variable to store previous question
            previous_questions = set()

            # tema
            tema = df_preguntas.iloc[117, 1]

            # attempt & questions loop
            while attempt < 3:
                print(f'\nTema: {tema}, \t Pregunta número {num_pregunta}, \t Intento número {attempt + 1}\n')

                # Grab random question from pool
                pool = random.randint(117, 131)
                pregunta = df_preguntas.iloc[pool, 3]

                # check if the question was previously asked
                if pregunta not in previous_questions:
                    previous_questions.add(pregunta)
                    print(pregunta)
                else:
                    pool = random.randint(117, 131)
                    pregunta = df_preguntas.iloc[pool, 3]
                    print(pregunta)

                df_respuesta = df_preguntas.iloc[pool, 4]

                # validate answer
                try:
                    respuesta = str.lower(input("Respuesta: "))
                    if respuesta == df_respuesta:
                        print('\nRespuesta correcta!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/9 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    elif respuesta == 'ayuda':
                        init_feedback.help(mod)

                    elif respuesta == answer_key:
                        print('\n Answer_Key:Pass!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/9 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    else:
                        print('\nRespuesta Incorrecta')
                        attempt += 1

                except ValueError:
                    print('\nError! Respuesta Incorrecta')
                    attempt += 1

                if attempt == 3:
                    print('\nHas agotado el número máximo de intentos\n')
                    print(f'La respuesta correcta es {df_respuesta}')
                    init_feedback.feedback_to_user(mod, tema)
                    continue

                if num_pregunta > 3:
                    break

            # Call next module
            if num_pregunta > 3:
                init_feedback.feedback_to_user(mod, tema)

        print(f'\nMódulo seleccionado: {mod}')
        subtema_uno_trig()

    @staticmethod
    def geometria():
        # Argument for module 'geometria' to recognize where the program is
        mod = 'geometria'

        def subtema_uno_geo():
            # Standard module template
            global respuestas_correctas

            # answer validation variables
            attempt = 0
            num_pregunta = 1

            # variable to store previous question
            previous_questions = set()

            # tema
            tema = df_preguntas.iloc[132, 1]

            # attempt & questions loop
            while attempt < 3:
                print(f'\nTema: {tema}, \t Pregunta número {num_pregunta}, \t Intento número {attempt + 1}\n')

                # Grab random question from pool
                pool = random.randint(132, 146)
                pregunta = df_preguntas.iloc[pool, 3]

                # check if the question was previously asked
                if pregunta not in previous_questions:
                    previous_questions.add(pregunta)
                    print(pregunta)
                else:
                    pool = random.randint(132, 146)
                    pregunta = df_preguntas.iloc[pool, 3]
                    print(pregunta)

                df_respuesta = df_preguntas.iloc[pool, 4]

                # validate answer
                try:
                    respuesta = str.lower(input("Respuesta: "))
                    if respuesta == df_respuesta:
                        print('\nRespuesta correcta!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/9 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    elif respuesta == 'ayuda':
                        init_feedback.help(mod)

                    elif respuesta == answer_key:
                        print('\n Answer_Key:Pass!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/9 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    else:
                        print('\nRespuesta Incorrecta')
                        attempt += 1

                except ValueError:
                    print('\nError! Respuesta Incorrecta')
                    attempt += 1

                if attempt == 3:
                    print('\nHas agotado el número máximo de intentos\n')
                    print(f'La respuesta correcta es {df_respuesta}')
                    init_feedback.feedback_to_user(mod, tema)
                    continue

                if num_pregunta > 3:
                    break

            # Call next module
            if num_pregunta > 3:
                subtema_dos_geo()

        def subtema_dos_geo():
            # Standard module template
            global respuestas_correctas

            # answer validation variables
            attempt = 0
            num_pregunta = 1

            # variable to store previous question
            previous_questions = set()

            # tema
            tema = df_preguntas.iloc[147, 1]

            # attempt & questions loop
            while attempt < 3:
                print(f'\nTema: {tema}, \t Pregunta número {num_pregunta}, \t Intento número {attempt + 1}\n')

                # Grab random question from pool
                pool = random.randint(147, 161)
                pregunta = df_preguntas.iloc[pool, 3]

                # check if the question was previously asked
                if pregunta not in previous_questions:
                    previous_questions.add(pregunta)
                    print(pregunta)
                else:
                    pool = random.randint(147, 161)
                    pregunta = df_preguntas.iloc[pool, 3]
                    print(pregunta)

                df_respuesta = df_preguntas.iloc[pool, 4]

                # validate answer
                try:
                    respuesta = str.lower(input("Respuesta: "))
                    if respuesta == df_respuesta:
                        print('\nRespuesta correcta!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/9 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    elif respuesta == 'ayuda':
                        init_feedback.help(mod)

                    elif respuesta == answer_key:
                        print('\n Answer_Key:Pass!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/9 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    else:
                        print('\nRespuesta Incorrecta')
                        attempt += 1

                except ValueError:
                    print('\nError! Respuesta Incorrecta')
                    attempt += 1

                if attempt == 3:
                    print('\nHas agotado el número máximo de intentos\n')
                    print(f'La respuesta correcta es {df_respuesta}')
                    init_feedback.feedback_to_user(mod, tema)
                    continue

                if num_pregunta > 3:
                    break

            # Call next module
            if num_pregunta > 3:
                subtema_tres_geo()

        def subtema_tres_geo():
            # Standard module template
            global respuestas_correctas

            # answer validation variables
            attempt = 0
            num_pregunta = 1

            # variable to store previous question
            previous_questions = set()

            # tema
            tema = df_preguntas.iloc[162, 1]

            # attempt & questions loop
            while attempt < 3:
                print(f'\nTema: {tema}, \t Pregunta número {num_pregunta}, \t Intento número {attempt + 1}\n')

                # Grab random question from pool
                pool = random.randint(162, 176)
                pregunta = df_preguntas.iloc[pool, 3]

                # check if the question was previously asked
                if pregunta not in previous_questions:
                    previous_questions.add(pregunta)
                    print(pregunta)
                else:
                    pool = random.randint(162, 176)
                    pregunta = df_preguntas.iloc[pool, 3]
                    print(pregunta)

                df_respuesta = df_preguntas.iloc[pool, 4]

                # validate answer
                try:
                    respuesta = str.lower(input("Respuesta: "))
                    if respuesta == df_respuesta:
                        print('\nRespuesta correcta!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/9 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    elif respuesta == 'ayuda':
                        init_feedback.help(mod)

                    elif respuesta == answer_key:
                        print('\n Answer_Key:Pass!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/9 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    else:
                        print('\nRespuesta Incorrecta')
                        attempt += 1

                except ValueError:
                    print('\nError! Respuesta Incorrecta')
                    attempt += 1

                if attempt == 3:
                    print('\nHas agotado el número máximo de intentos\n')
                    print(f'La respuesta correcta es {df_respuesta}')
                    init_feedback.feedback_to_user(mod, tema)
                    continue

                if num_pregunta > 3:
                    break

            # Call next module
            if num_pregunta > 3:
                init_feedback.feedback_to_user(mod, tema)

        print(f'\nMódulo seleccionado: {mod}')
        subtema_uno_geo()

    @staticmethod
    def funciones():
        # Argument for module 'funciones' to recognize where the program is
        mod = 'funciones'

        def subtema_uno_func():
            # Standard module template
            global respuestas_correctas

            # answer validation variables
            attempt = 0
            num_pregunta = 1

            # variable to store previous question
            previous_questions = set()

            # tema
            tema = df_preguntas.iloc[177, 1]

            # attempt & questions loop
            while attempt < 3:
                print(f'\nTema: {tema}, \t Pregunta número {num_pregunta}, \t Intento número {attempt + 1}\n')

                # Grab random question from pool
                pool = random.randint(177, 191)
                pregunta = df_preguntas.iloc[pool, 3]

                # check if the question was previously asked
                if pregunta not in previous_questions:
                    previous_questions.add(pregunta)
                    print(pregunta)
                else:
                    pool = random.randint(177, 191)
                    pregunta = df_preguntas.iloc[pool, 3]
                    print(pregunta)

                df_respuesta = df_preguntas.iloc[pool, 4]

                # validate answer
                try:
                    respuesta = str.lower(input("Respuesta: "))
                    if respuesta == df_respuesta:
                        print('\nRespuesta correcta!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/9 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    elif respuesta == 'ayuda':
                        init_feedback.help(mod)

                    elif respuesta == answer_key:
                        print('\n Answer_Key:Pass!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/9 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    else:
                        print('\nRespuesta Incorrecta')
                        attempt += 1

                except ValueError:
                    print('\nError! Respuesta Incorrecta')
                    attempt += 1

                if attempt == 3:
                    print('\nHas agotado el número máximo de intentos\n')
                    print(f'La respuesta correcta es {df_respuesta}')
                    init_feedback.feedback_to_user(mod, tema)
                    continue

                if num_pregunta > 3:
                    break

            # Call next module
            if num_pregunta > 3:
                subtema_dos_func()

        def subtema_dos_func():
            # Standard module template
            global respuestas_correctas

            # answer validation variables
            attempt = 0
            num_pregunta = 1

            # variable to store previous question
            previous_questions = set()

            # tema
            tema = df_preguntas.iloc[192, 1]

            # attempt & questions loop
            while attempt < 3:
                print(f'\nTema: {tema}, \t Pregunta número {num_pregunta}, \t Intento número {attempt + 1}\n')

                # Grab random question from pool
                pool = random.randint(192, 206)
                pregunta = df_preguntas.iloc[pool, 3]

                # check if the question was previously asked
                if pregunta not in previous_questions:
                    previous_questions.add(pregunta)
                    print(pregunta)
                else:
                    pool = random.randint(192, 206)
                    pregunta = df_preguntas.iloc[pool, 3]
                    print(pregunta)

                df_respuesta = df_preguntas.iloc[pool, 4]

                # validate answer
                try:
                    respuesta = str.lower(input("Respuesta: "))
                    if respuesta == df_respuesta:
                        print('\nRespuesta correcta!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/9 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    elif respuesta == 'ayuda':
                        init_feedback.help(mod)

                    elif respuesta == answer_key:
                        print('\n Answer_Key:Pass!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/9 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    else:
                        print('\nRespuesta Incorrecta')
                        attempt += 1

                except ValueError:
                    print('\nError! Respuesta Incorrecta')
                    attempt += 1

                if attempt == 3:
                    print('\nHas agotado el número máximo de intentos\n')
                    print(f'La respuesta correcta es {df_respuesta}')
                    init_feedback.feedback_to_user(mod, tema)
                    continue

                if num_pregunta > 3:
                    break

            # Call next module
            if num_pregunta > 3:
                init_feedback.feedback_to_user(mod, tema)

        print(f'\nMódulo seleccionado: {mod}')
        subtema_uno_func()

    @staticmethod
    def repaso_general():

        # Argument for module 'repaso_general' to recognize where the program is
        mod = 'repaso general'

        print(f'\nMódulo seleccionado: {mod}\n')

        print('\nEl repaso general consiste de una pregunta de cada tema principal')
        sleep(2)
        print('tendrás 3 intentos por pregunta y programa concluye una vez que has respondido las 5 preguntas')
        sleep(2)
        print('podrás repetir la evaluación de las veces que quieras\n')

        def gral_aritmetica():

            # Standard module template
            global respuestas_correctas
            tema = 'aritmetica'
            mod = 'aritmetica'

            # answer validation variables
            attempt = 0
            num_pregunta = 1

            # variable to store previous question
            previous_questions = set()

            while attempt < 3:
                print(f'\nTema: {tema}, \t Pregunta número {num_pregunta}, \t Intento número {attempt + 1}\n')

                pool = random.randint(0, 41)
                pregunta = df_preguntas.iloc[pool, 3]

                if pregunta not in previous_questions:
                    previous_questions.add(pregunta)
                    print(pregunta)
                else:
                    pool = random.randint(0, 41)
                    pregunta = df_preguntas.iloc[pool, 3]
                    print(pregunta)

                df_respuesta = df_preguntas.iloc[pool, 4]

                try:
                    respuesta = str.lower(input("Respuesta: "))
                    if respuesta == df_respuesta:
                        print('\nRespuesta correcta!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/5 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    elif respuesta == 'ayuda':
                        init_feedback.help(mod)

                    elif respuesta == answer_key:
                        print('\n Answer_Key:Pass!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/5 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    else:
                        print('\nRespuesta Incorrecta')
                        attempt += 1

                except ValueError:
                    print('\nError! Respuesta Incorrecta')
                    attempt += 1

                if attempt == 3:
                    print('\nHas agotado el número máximo de intentos\n')
                    print(f'La respuesta correcta es {df_respuesta}\n')
                    gral_algebra()
                    break
                elif num_pregunta == 2:
                    gral_algebra()

        def gral_algebra():

            # Standard module template
            global respuestas_correctas
            tema = 'algebra'
            mod = 'algebra'

            # answer validation variables
            attempt = 0
            num_pregunta = 1

            # variable to store previous question
            previous_questions = set()

            while attempt < 3:
                print(f'\nTema: {tema}, \t Pregunta número {num_pregunta}, \t Intento número {attempt + 1}\n')

                pool = random.randint(41, 86)
                pregunta = df_preguntas.iloc[pool, 3]

                if pregunta not in previous_questions:
                    previous_questions.add(pregunta)
                    print(pregunta)
                else:
                    pool = random.randint(41, 86)
                    pregunta = df_preguntas.iloc[pool, 3]
                    print(pregunta)

                df_respuesta = df_preguntas.iloc[pool, 4]

                try:
                    respuesta = str.lower(input("Respuesta: "))
                    if respuesta == df_respuesta:
                        print('\nRespuesta correcta!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/5 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    elif respuesta == 'ayuda':
                        init_feedback.help(mod)

                    elif respuesta == answer_key:
                        print('\n Answer_Key:Pass!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/5 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    else:
                        print('\nRespuesta Incorrecta')
                        attempt += 1

                except ValueError:
                    print('\nError! Respuesta Incorrecta')
                    attempt += 1

                if attempt == 3:
                    print('\nHas agotado el número máximo de intentos\n')
                    print(f'La respuesta correcta es {df_respuesta}')
                    gral_trig()
                    break
                elif num_pregunta == 2:
                    gral_trig()

        def gral_trig():

            # Standard module template
            global respuestas_correctas
            tema = 'trigonometria'
            mod = 'trigonometria'

            # answer validation variables
            attempt = 0
            num_pregunta = 1

            # variable to store previous question
            previous_questions = set()

            while attempt < 3:
                print(f'\nTema: {tema}, \t Pregunta número {num_pregunta}, \t Intento número {attempt + 1}\n')

                pool = random.randint(87, 131)
                pregunta = df_preguntas.iloc[pool, 3]

                if pregunta not in previous_questions:
                    previous_questions.add(pregunta)
                    print(pregunta)
                else:
                    pool = random.randint(87, 131)
                    pregunta = df_preguntas.iloc[pool, 3]
                    print(pregunta)

                df_respuesta = df_preguntas.iloc[pool, 4]

                try:
                    respuesta = str.lower(input("Respuesta: "))
                    if respuesta == df_respuesta:
                        print('\nRespuesta correcta!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/5 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    elif respuesta == 'ayuda':
                        init_feedback.help(mod)

                    elif respuesta == answer_key:
                        print('\n Answer_Key:Pass!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/5 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    else:
                        print('\nRespuesta Incorrecta')
                        attempt += 1

                except ValueError:
                    print('\nError! Respuesta Incorrecta')
                    attempt += 1

                if attempt == 3:
                    print('\nHas agotado el número máximo de intentos\n')
                    print(f'La respuesta correcta es {df_respuesta}')
                    gral_geo()
                    break
                elif num_pregunta == 2:
                    gral_geo()

        def gral_geo():

            # Standard module template
            global respuestas_correctas
            tema = 'geometria'
            mod = 'geometria'

            # answer validation variables
            attempt = 0
            num_pregunta = 1

            # variable to store previous question
            previous_questions = set()

            while attempt < 3:
                print(f'\nTema: {tema}, \t Pregunta número {num_pregunta}, \t Intento número {attempt + 1}\n')

                pool = random.randint(132, 176)
                pregunta = df_preguntas.iloc[pool, 3]

                if pregunta not in previous_questions:
                    previous_questions.add(pregunta)
                    print(pregunta)
                else:
                    pool = random.randint(132, 176)
                    pregunta = df_preguntas.iloc[pool, 3]
                    print(pregunta)

                df_respuesta = df_preguntas.iloc[pool, 4]

                try:
                    respuesta = str.lower(input("Respuesta: "))
                    if respuesta == df_respuesta:
                        print('\nRespuesta correcta!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/5 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    elif respuesta == 'ayuda':
                        init_feedback.help(mod)

                    elif respuesta == answer_key:
                        print('\n Answer_Key:Pass!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/5 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    else:
                        print('\nRespuesta Incorrecta')
                        attempt += 1

                except ValueError:
                    print('\nError! Respuesta Incorrecta')
                    attempt += 1

                if attempt == 3:
                    print('\nHas agotado el número máximo de intentos\n')
                    print(f'La respuesta correcta es {df_respuesta}')
                    gral_funciones()
                    break
                elif num_pregunta == 2:
                    gral_funciones()

        def gral_funciones():

            # Standard module template
            global respuestas_correctas
            tema = 'funciones'
            mod = 'funciones'

            # answer validation variables
            attempt = 0
            num_pregunta = 1

            # variable to store previous question
            previous_questions = set()

            while attempt < 3:
                print(f'\nTema: {tema}, \t Pregunta número {num_pregunta}, \t Intento número {attempt + 1}\n')

                pool = random.randint(177, 206)
                pregunta = df_preguntas.iloc[pool, 3]

                if pregunta not in previous_questions:
                    previous_questions.add(pregunta)
                    print(pregunta)
                else:
                    pool = random.randint(177, 206)
                    pregunta = df_preguntas.iloc[pool, 3]
                    print(pregunta)

                df_respuesta = df_preguntas.iloc[pool, 4]

                try:
                    respuesta = str.lower(input("Respuesta: "))
                    if respuesta == df_respuesta:
                        print('\nRespuesta correcta!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/5 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    elif respuesta == 'ayuda':
                        init_feedback.help(mod)

                    elif respuesta == answer_key:
                        print('\n Answer_Key:Pass!')
                        respuestas_correctas += 1
                        print(f'{respuestas_correctas}/5 preguntas')
                        num_pregunta += 1
                        attempt = 0

                    else:
                        print('\nRespuesta Incorrecta')
                        attempt += 1

                except ValueError:
                    print('\nError! Respuesta Incorrecta')
                    attempt += 1

                if attempt == 3:
                    print('\nHas agotado el número máximo de intentos\n')
                    print(f'La respuesta correcta es {df_respuesta}')
                    init_feedback.evaluate_gral()
                    sys.exit()
                elif num_pregunta == 2:
                    init_feedback.evaluate_gral()
                    sys.exit()

        gral_aritmetica()


# global variables
df_preguntas = pd.read_csv('df_preguntas.csv')
respuestas_correctas = 0

# this will override the correct answer and mark as correct for dev usability
answer_key = 'latte'

# create objects
init_math = Math()
init_feedback = Retroalimentacion()

# call main function
print('Para este programa se recomienda poner la consola en pantalla completa')
sleep(1.1)
main()