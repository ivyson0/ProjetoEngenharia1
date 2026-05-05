from django.test import TestCase
from .models import Divida, Cliente, Endereco
from unittest.mock import patch

class DividaTest(TestCase):

    def setUp(self):
        self.endereco = Endereco.objects.create(
            logradouro="Rua A",
            numero="123",
            bairro="Bairro Y",
            cidade="Cidade X",
            estado="Estado Z",
            cep="12345-678"
        )

        self.cliente = Cliente.objects.create(
            nome="João",
            cpf="123",
            endereco=self.endereco
        )

    def test_criar_divida(self):
        divida = Divida.objects.create(cliente=self.cliente, valor=100)
        self.assertEqual(divida.valor, 100)

    def test_listar_dividas(self):
        Divida.objects.create(cliente=self.cliente, valor=100)
        self.assertEqual(Divida.objects.count(), 1)

    def test_atualizar_divida(self):
        divida = Divida.objects.create(cliente=self.cliente, valor=100)
        divida.valor = 200
        divida.save()
        self.assertEqual(Divida.objects.get().valor, 200)

    def test_deletar_divida(self):
        divida = Divida.objects.create(cliente=self.cliente, valor=100)
        divida.delete()
        self.assertEqual(Divida.objects.count(), 0)


class DividaMockTest(TestCase):

    @patch('antiveaco.models.Divida.objects.create')
    def test_criar_divida(self, mock_create):
        mock_create.return_value.valor = 100

        divida = Divida.objects.create(valor=100)

        self.assertEqual(divida.valor, 100)
        mock_create.assert_called_once()


    @patch('antiveaco.models.Divida.objects.count')
    def test_listar_dividas(self, mock_count):
        mock_count.return_value = 1

        total = Divida.objects.count()

        self.assertEqual(total, 1)

    @patch('antiveaco.models.Divida.save')
    def test_atualizar_divida(self, mock_save):
        divida = Divida(valor=100)
        divida.valor = 200
        divida.save()

        self.assertEqual(divida.valor, 200)
        mock_save.assert_called_once()

    @patch('antiveaco.models.Divida.delete')
    def test_deletar_divida(self, mock_delete):
        divida = Divida(valor=100)
        divida.delete()

        mock_delete.assert_called_once()