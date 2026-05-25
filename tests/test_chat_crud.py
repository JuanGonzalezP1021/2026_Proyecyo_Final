import unittest
import os

from agente_chat import AgenteChat
from chat_dao import ChatDAO


class TestChatCRUD(unittest.TestCase):

    def setUp(self):

        self.dao = ChatDAO()

        if os.path.exists(self.dao.FILE):
            os.remove(self.dao.FILE)

    def test_01_crear(self):

        a = AgenteChat("C001", "TL", 200, 2)

        self.assertTrue(self.dao.crear(a))

    def test_02_no_duplicar(self):

        a = AgenteChat("C001", "TL", 200, 2)

        self.dao.crear(a)

        self.assertFalse(self.dao.crear(a))

    def test_03_obtener(self):

        a = AgenteChat("C002", "TL", 100, 1)

        self.dao.crear(a)

        self.assertIsNotNone(self.dao.obtener("C002"))

    def test_04_obtener_none(self):

        self.assertIsNone(self.dao.obtener("X"))

    def test_05_actualizar(self):

        a = AgenteChat("C003", "TL", 100, 1)

        self.dao.crear(a)

        a.set_chat_aht(500)

        self.assertTrue(self.dao.actualizar(a))

    def test_06_actualizar_inexistente(self):

        a = AgenteChat("X", "TL", 0, 1)

        self.assertFalse(self.dao.actualizar(a))

    def test_07_eliminar(self):

        a = AgenteChat("C004", "TL", 100, 1)

        self.dao.crear(a)

        self.assertTrue(self.dao.eliminar("C004"))

    def test_08_eliminar_inexistente(self):

        self.assertFalse(self.dao.eliminar("X"))

    def test_09_listar(self):

        self.dao.crear(
            AgenteChat("C005", "TL", 100, 1)
        )

        self.dao.crear(
            AgenteChat("C006", "TL", 200, 2)
        )

        self.assertEqual(
            len(self.dao.obtener_todos()),
            2
        )

    def test_10_aht(self):

        a = AgenteChat("C007", "TL", 420, 2)

        self.assertEqual(a.calcular_aht(), 420)


if __name__ == "__main__":
    unittest.main()
