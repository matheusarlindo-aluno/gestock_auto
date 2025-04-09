usuarios = []

def soma(a,b):
    # função para somar
    return a+b

def is_par(a):
    if a%2 == 0:
        return True
    else:
        return False
    
def fatorial(n):
    resultado = 1
    count = 1

    while count <= n:
        resultado *= count 
        count +=1

    if n < 0:
        raise ValueError("Não é possível fatorar números negativos")
    return resultado

def contar_vogais(texto):
    vogais= "aeiouAEIOU"
    contador = 0

    for vogal in texto:
        if vogal in vogais:
            contador +=1

    return contador


def cadastro_usuario(nome, email):
    for usuario in usuarios:
        if usuario["email"] == email:
            return "email ja existe"

    novo_usuario ={
        "nome":nome,
        "email":email
    }

    usuarios.append(novo_usuario)
    return "sucesso"

#controller
def cadastro(nome , cpf):
    new_user = {
        "nome":nome,
        "cpf":cpf
    }
    return save(new_user)

#service
def save(new_user):
    if new_user["nome"] and new_user["cpf"]:
        return True #salvo no DB
    return False #erro ao salvar no DB


