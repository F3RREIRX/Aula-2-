print('Faça seu cadastro')
email=input('coloque seu E-mail: ')
senha=input('crie sua senha: ')

print('Coloque sua conta Novamente')
email1 = input('Email: ')
senha1 =input('Senha: ')

if email1==email and senha1==senha:
    print('usuario e senha corretos')
elif senha1==senha and email1!=email:
    print('E-mail incorreto')
elif senha1!=senha and email1==email: 
    print('Senha Incorreta')
else:
    print('cadastro não encontrado')
    
