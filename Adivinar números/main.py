from random import randint
import sys


def adivinaNumero():
    adivina=input('Adivina el número del 1 al 100: ')
    adivinaInt=int(adivina)
    puntuacion=100
    numeleg=randint(1,100)

    while adivinaInt!=numeleg:
        puntuacion-=10
        print('--- Incorrecto, sigue intentandolo ---')


        if puntuacion==90:
            parImpar=numeleg%2

            if parImpar==0:
                print('PISTA: Te damos una pista: el número es par')

            else:
                print('PISTA: El número es impar')
        

        if puntuacion==70:
            if numeleg >= 50:
                print('PISTA: El número es mayor o igual que 50')

            else:
                print('PISTA: El número es menor que 50')

        
        if puntuacion==50:
            div3=numeleg%3

            if div3==0:
                print('El número es múltiplo de 3')

            else:
                print('El número no es múltiplo de 3')


        if puntuacion==30:
            numeleg2=str(numeleg)
            cifra1=numeleg2[0]
            cifra2=numeleg2[1]
            listcifra=[cifra1,cifra2]

            if (len(listcifra)) == 2:
                cifraI=int(cifra1)
                cifra2I=int(cifra2)
                suma=cifraI+cifra2I
                
                print('La suma de las cifras da',suma)

            else:
                print('La suma de sus cifras da',numeleg)

        
        if puntuacion==10:
            if cifra2I >=5:
                print('La segunda cifra es mayor o igual que 5')

            else:
                print('La segunda cifra es menor que 5')

        if puntuacion==0:
            print('Has perdido')
            sys.exit()


        adivina=input('Adivina el número: ')
        adivinaInt=int(adivina)

    print('Correcto, has acertado el número')
    print('Puntuación:',puntuacion)


if __name__=='__main__':
    print('BIENVENIDO A -- ADIVINA EL NÚMERO --')
    adivinaNumero()