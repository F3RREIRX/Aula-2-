operacao= int(input('1.Soma , 2. Subtração , 3. Multiplicação , 4. Divisão '))

n1= int(input('Digite o primeiro número: '))

n2= int(input('Digite o segundo número: '))

soma = n1+n2 
Subtracao = n1-n2
Multiplicacao = n1*n2
divisao = n1/n2

if operacao==1 :
    print('o resultado é' ,soma)
elif operacao==2:
    print('o resultado é' ,Subtracao)
elif operacao ==4:
    print('o resultado é' ,divisao)
elif operacao==3:
    print('o resultado é' ,Multiplicacao)
else:
    ('ERRO')
