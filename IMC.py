
peso = float(input('informar o seu peso: '))
altura = float(input('informar a sua altura: '))
calculo = peso / (altura * altura)
calculo = round(calculo,2)
print(calculo)

if (calculo <= 18.5) :
    print('Abaixo do peso!')
elif (calculo > 18.5 and calculo <= 24.9) :
    print('Peso normal!')
elif (calculo > 25.0 and calculo <= 29.9) :
    print('Pre obesidade!')
elif (calculo > 30.0 and calculo <= 34.9) :
    print('Obesidade grau 1!')
elif (calculo > 35.0 and calculo <= 39.9) :
    print('Obesidade grau 2!')
else : print('Obesidade grau 3!')
