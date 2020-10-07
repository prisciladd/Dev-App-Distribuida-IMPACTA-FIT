import unittest

agenda_testes1 = {
    'joao': 22222222,
    'jose': 33333333,
}

# Agendas melhoradas.
agenda1 = {}
alfabeto  = 'abcde'
for c in alfabeto:
    agenda1[c] = {'telefones': [1122233344]} # Uma agenda cujas pessoas são as primeiras 5 letras.

agenda2 = {}
vogais  = 'aeiouy'
for c in vogais:
    agenda2[c] = {'telefones': [11321321321]} # Uma agenda cujas pessoas são todas as vogais.
agenda2['fulano'] = {'email': 'fulano@exemplo.com', 'telefones': [1144440000]}

agenda3 = {}
pessoas = ['marcia', 'ana', 'marcos', 'heitor'] 
for p in pessoas:
    agenda3[p] = {'telefones': [1123232323]}
agenda3['fulano'] = {'email': 'fulano@exemplo.com', 'telefones': [11777888999, 1122222222]}

class TestPartOne(unittest.TestCase):

    def test_01_consulta(self):
        self.assertEqual(consulta(agenda_testes1, 'joao'), 22222222)
        self.assertEqual(consulta(agenda_testes1, 'jose'), 33333333)

    def test_02_adiciona(self):
        agenda_testes1 = {
           'joao': 2,
           'jose': 3,
        }
        adiciona(agenda_testes1, 'marcia', 55555555)
        self.assertEqual(consulta(agenda_testes1, 'marcia'), 55555555)
        adiciona(agenda_testes1, 'antonio', 88888888)
        self.assertEqual(consulta(agenda_testes1, 'antonio'), 88888888)

    def test_03_verifica(self):
        self.assertFalse(verifica(agenda_testes1, 'marcia'))
        self.assertFalse(verifica(agenda_testes1, 'antonio'))
        self.assertTrue(verifica(agenda_testes1, 'joao'))
        self.assertTrue(verifica(agenda_testes1, 'jose'))

    def test_04_conta_letras(self):
        self.assertEqual(conta_letras('banana'), {'b': 1, 'n': 2, 'a': 3})
        self.assertEqual(conta_letras(''), {})
        self.assertEqual(conta_letras('a' * 5 + 'b' * 3 + 'c' * 10 + 'a'), {'a': 6, 'b': 3, 'c': 10})

    def test_05_email(self):
        self.assertEqual(email(agenda1, 'lucas'), 'lucas.goncalves@faculdadeimpacta.com.br')
        self.assertEqual(email(agenda1, 'maria'), 'maria.aparecida@exemplo.com')
        self.assertEqual(email(agenda2, 'fulano'), 'fulano@exemplo.com')
        self.assertEqual(email(agenda3, 'fulano'), 'fulano@exemplo.com')

    def test_06_telefone_principal(self):
        self.assertEqual(telefone_principal(agenda1, 'lucas'), 11999888999)
        self.assertEqual(telefone_principal(agenda1, 'maria'), 84999777444)
        self.assertEqual(telefone_principal(agenda1, 'lucas'), 1177788899)
        self.assertEqual(telefone_principal(agenda1, 'a'), 1122233344)
        self.assertEqual(telefone_principal(agenda2, 'a'), 11321321321)
        self.assertEqual(telefone_principal(agenda3, 'ana'), 1123232323)
        self.assertEqual(telefone_principal(agenda3, 'fulano'), 11777888999)

    def test_07_sem_email(self):
        self.assertEqual(set(sem_email(agenda1)), set(list(alfabeto)))
        self.assertEqual(set(sem_email(agenda2)), set(list(vogais)))
        self.assertEqual(set(sem_email(agenda3)), set(pessoas))

    def test_08_conta_telefones(self):
        self.assertEqual(conta_telefones(agenda1), 5)
        self.assertEqual(conta_telefones(agenda2), 7)
        self.assertEqual(conta_telefones(agenda3), 6)
    
    def test_09_conta_ocorrencias(self):
        self.assertEqual(conta_ocorrencias(agenda1), {1122233344: 5})
        self.assertEqual(conta_ocorrencias(agenda2), {11321321321: 6, 1144440000: 1})
        self.assertEqual(conta_ocorrencias(agenda3), {1123232323: 4, 11777888999: 1, 1122222222: 1})

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestPartOne)
    unittest.TextTestRunner(verbosity = 2, failfast = True).run(suite)

try:
    from ex_dicionarios import *
except:
    pass

runTests()
