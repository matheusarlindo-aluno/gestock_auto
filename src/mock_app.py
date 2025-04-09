#1
def cadastro_email(email):
    new_user = {"email": email}
    return send_email(new_user)

def send_email(new_user):
    if new_user["email"]:
        return f"E-mail enviado para {new_user['email']}"
    return "Erro ao enviar e-mail"


#2
def get_preco(produto_id):
    return consultar_api_preco(produto_id)

def consultar_api_preco(produto_id):
    if produto_id:
        return {"produto_id": produto_id, "preco": 100.0}  # Simulando resposta da API
    return None

#3
def salvar_usuario(nome, cpf):
    new_user = {"nome": nome, "cpf": cpf}
    return salvar_no_db(new_user)

def salvar_no_db(new_user):
    if new_user["nome"] and new_user["cpf"]:
        return "Usuário salvo no banco"
    return "Erro ao salvar usuário"

#4
def processar_pagamento(cartao, valor):
    pagamento = {"cartao": cartao, "valor": valor}
    return gateway_pagamento(pagamento)

def gateway_pagamento(pagamento):
    if pagamento["cartao"] and pagamento["valor"] > 0:
        return "Pagamento aprovado"
    return "Pagamento recusado"

#5
def enviar_sms(numero, mensagem):
    sms = {"numero": numero, "mensagem": mensagem}
    return sms_service(sms)

def sms_service(sms):
    if sms["numero"] and sms["mensagem"]:
        return f"SMS enviado para {sms['numero']}"
    return "Erro ao enviar SMS"

#6
def processar_arquivo(nome_arquivo):
    return ler_arquivo(nome_arquivo)

def ler_arquivo(nome_arquivo):
    if nome_arquivo:
        return f"Conteúdo do arquivo {nome_arquivo}"
    return "Erro ao ler arquivo"

#7
def registrar_log(mensagem):
    log = {"mensagem": mensagem}
    return salvar_log(log)

def salvar_log(log):
    if log["mensagem"]:
        return "Log registrado com sucesso"
    return "Erro ao registrar log"

#8
def autenticar_usuario(usuario, senha):
    credenciais = {"usuario": usuario, "senha": senha}
    return servico_autenticacao(credenciais)

def servico_autenticacao(credenciais):
    if credenciais["usuario"] == "admin" and credenciais["senha"] == "1234":
        return "Autenticação bem-sucedida"
    return "Usuário ou senha inválidos"

#9
def agendar_tarefa(tarefa, horario):
    evento = {"tarefa": tarefa, "horario": horario}
    return servico_agendamento(evento)

def servico_agendamento(evento):
    if evento["tarefa"] and evento["horario"]:
        return f"Tarefa '{evento['tarefa']}' agendada para {evento['horario']}"
    return "Erro ao agendar tarefa"

#10
def buscar_usuario(nome):
    return consultar_db(nome)

def consultar_db(nome):
    usuarios = [{"nome": "Lucas", "cpf": "12345678900"}]  # Simulando um banco de dados
    for usuario in usuarios:
        if usuario["nome"] == nome:
            return usuario
    return "Usuário não encontrado"

#11
def processar_imagem(imagem):
    return servico_imagem(imagem)

def servico_imagem(imagem):
    if imagem:
        return f"Imagem {imagem} processada com sucesso"
    return "Erro no processamento da imagem"

#12
def gerar_relatorio(tipo):
    return servico_relatorio(tipo)

def servico_relatorio(tipo):
    if tipo in ["PDF", "Excel"]:
        return f"Relatório {tipo} gerado com sucesso"
    return "Erro ao gerar relatório"

#13
def criar_usuario(nome, email, telefone):
    user = {"nome": nome, "email": email, "telefone": telefone}
    return cadastrar_usuario(user)

def cadastrar_usuario(user):
    if user["nome"] and user["email"]:
        email_status = send_email(user)
        sms_status = sms_service(user)
        return f"Usuário criado. {email_status}. {sms_status}"
    return "Erro ao criar usuário"

#14
def sincronizar_dados(origem, destino):
    dados = {"origem": origem, "destino": destino}
    return servico_sincronizacao(dados)

def servico_sincronizacao(dados):
    if dados["origem"] and dados["destino"]:
        return "Sincronização concluída"
    return "Erro na sincronização"
