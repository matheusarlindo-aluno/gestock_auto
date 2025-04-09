import unittest
from unittest.mock import patch

# Importa as funções que criamos
from src.mock_app import (
    cadastro_email, get_preco, salvar_usuario, processar_pagamento,
    enviar_sms, processar_arquivo, registrar_log, autenticar_usuario,
    agendar_tarefa, buscar_usuario, processar_imagem, gerar_relatorio,
    criar_usuario, sincronizar_dados
)

class TestServices(unittest.TestCase):

    @patch("src.mock_app.send_email")
    def test_cadastro_email(self, mock_send_email):
        mock_send_email.return_value = "E-mail enviado para teste@teste.com"
        result = cadastro_email("teste@teste.com")
        self.assertEqual(result, "E-mail enviado para teste@teste.com")

    @patch("src.mock_app.consultar_api_preco")
    def test_get_preco(self, mock_consultar_api_preco):
        mock_consultar_api_preco.return_value = {"produto_id": 1, "preco": 100.0}
        result = get_preco(1)
        self.assertEqual(result, {"produto_id": 1, "preco": 100.0})

    @patch("src.mock_app.salvar_no_db")
    def test_salvar_usuario(self, mock_salvar_no_db):
        mock_salvar_no_db.return_value = "Usuário salvo no banco"
        result = salvar_usuario("Lucas", "12345678900")
        self.assertEqual(result, "Usuário salvo no banco")

    @patch("src.mock_app.gateway_pagamento")
    def test_processar_pagamento(self, mock_gateway_pagamento):
        mock_gateway_pagamento.return_value = "Pagamento aprovado"
        result = processar_pagamento("4111-1111-1111-1111", 50)
        self.assertEqual(result, "Pagamento aprovado")

    @patch("src.mock_app.sms_service")
    def test_enviar_sms(self, mock_sms_service):
        mock_sms_service.return_value = "SMS enviado para 99999-9999"
        result = enviar_sms("99999-9999", "Teste de SMS")
        self.assertEqual(result, "SMS enviado para 99999-9999")

    @patch("src.mock_app.ler_arquivo")
    def test_processar_arquivo(self, mock_ler_arquivo):
        mock_ler_arquivo.return_value = "Conteúdo do arquivo data.txt"
        result = processar_arquivo("data.txt")
        self.assertEqual(result, "Conteúdo do arquivo data.txt")

    @patch("src.mock_app.salvar_log")
    def test_registrar_log(self, mock_salvar_log):
        mock_salvar_log.return_value = "Log registrado com sucesso"
        result = registrar_log("Erro crítico no sistema")
        self.assertEqual(result, "Log registrado com sucesso")

    @patch("src.mock_app.servico_autenticacao")
    def test_autenticar_usuario(self, mock_servico_autenticacao):
        mock_servico_autenticacao.return_value = "Autenticação bem-sucedida"
        result = autenticar_usuario("admin", "1234")
        self.assertEqual(result, "Autenticação bem-sucedida")

    @patch("src.mock_app.servico_agendamento")
    def test_agendar_tarefa(self, mock_servico_agendamento):
        mock_servico_agendamento.return_value = "Tarefa 'Backup' agendada para 22:00"
        result = agendar_tarefa("Backup", "22:00")
        self.assertEqual(result, "Tarefa 'Backup' agendada para 22:00")

    @patch("src.mock_app.consultar_db")
    def test_buscar_usuario(self, mock_consultar_db):
        mock_consultar_db.return_value = {"nome": "Lucas", "cpf": "12345678900"}
        result = buscar_usuario("Lucas")
        self.assertEqual(result, {"nome": "Lucas", "cpf": "12345678900"})

    @patch("src.mock_app.servico_imagem")
    def test_processar_imagem(self, mock_servico_imagem):
        mock_servico_imagem.return_value = "Imagem foto.jpg processada com sucesso"
        result = processar_imagem("foto.jpg")
        self.assertEqual(result, "Imagem foto.jpg processada com sucesso")

    @patch("src.mock_app.servico_relatorio")
    def test_gerar_relatorio(self, mock_servico_relatorio):
        mock_servico_relatorio.return_value = "Relatório PDF gerado com sucesso"
        result = gerar_relatorio("PDF")
        self.assertEqual(result, "Relatório PDF gerado com sucesso")

    @patch("src.mock_app.cadastrar_usuario")
    def test_criar_usuario(self, mock_cadastrar_usuario):
        mock_cadastrar_usuario.return_value = "Usuário criado. E-mail enviado. SMS enviado."
        result = criar_usuario("Lucas", "lucas@email.com", "99999-9999")
        self.assertEqual(result, "Usuário criado. E-mail enviado. SMS enviado.")

    @patch("src.mock_app.servico_sincronizacao")
    def test_sincronizar_dados(self, mock_servico_sincronizacao):
        mock_servico_sincronizacao.return_value = "Sincronização concluída"
        result = sincronizar_dados("Servidor A", "Servidor B")
        self.assertEqual(result, "Sincronização concluída")

if __name__ == "__main__":
    unittest.main()
