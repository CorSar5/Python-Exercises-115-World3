def voto(n):
    from datetime import datetime
    i = datetime.now().year - n
    if i >= 18:
        return f'Com {i} anos: o voto é OBRIGATÓRIO.'
    elif i >= 65:
        return f'Com {i} anos: o voto é OPCIONAL.'
    elif i < 18:
        return f'Com {i} anos: o voto é NEGADO!'


idade= int(input('Digite o seu ano de nascimento: '))
print(voto(idade))