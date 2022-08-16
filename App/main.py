banco_de_dados = {}

# TODO: crie uma função que peça nome, sobrenome, email, senha, confirmar senha


def set_usuarios():
    primeiro_nome = input('Nome: ')
    sobrenome = input('Sobrenome: ')
    email = input('E-mail: ') + '@gmail.com'
    senha = input('Senha: ')
    confirmar_senha = input('Confirmar senha: ')

    if len(primeiro_nome) < 3:
        return {'msg': f'Muito curto: {primeiro_nome}'}

    banco_de_dados['Nome'] = primeiro_nome
    banco_de_dados['sobrenome'] = sobrenome
    banco_de_dados['E-mail'] = email
    banco_de_dados['Senha'] = senha
    banco_de_dados['Confirmar senha: '] = confirmar_senha

print(set_usuarios())
print(banco_de_dados)
