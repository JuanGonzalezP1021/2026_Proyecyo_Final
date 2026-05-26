import unittest
import os

from modelo.agente_chat import AgenteChat
from repositorio.chat_dao import ChatDAO


class TestChatCRUD(unittest.TestCase):

    def setUp(self):

        self.dao = ChatDAO()
        self.dao.FILE = "data/test_chat.json"

        if os.path.exists(self.dao.FILE):
            os.remove(self.dao.FILE)

    def tearDown(self):

        if os.path.exists(self.dao.FILE):
            os.remove(self.dao.FILE)

    # 1
    def test_01_crear_agente_chat(self):

        a = AgenteChat("C001", "TL_Rosa", 280.5, 2)

        self.assertTrue(self.dao.crear(a))

    # 2
    def test_02_no_duplicar_agente_chat(self):

        a = AgenteChat("C001", "TL_Rosa", 280.5, 2)

        self.dao.crear(a)

        self.assertFalse(self.dao.crear(a))

    # 3
    def test_03_leer_agente_chat(self):

        self.dao.crear(
            AgenteChat("C002", "TL_Pedro", 310.0, 3)
        )

        r = self.dao.obtener("C002")

        self.assertEqual(
            r.get_agent_id(),
            "C002"
        )

    # 4
    def test_04_leer_agente_inexistente(self):

        self.assertIsNone(
            self.dao.obtener("ZZZZ")
        )

    # 5
    def test_05_actualizar_chat_aht(self):

        a = AgenteChat("C003", "TL_Eva", 200.0, 2)

        self.dao.crear(a)

        a.set_chat_aht(350.0)

        self.dao.actualizar(a)

        self.assertEqual(
            self.dao.obtener("C003").get_chat_aht(),
            350.0
        )

    # 6
    def test_06_actualizar_agente_inexistente(self):

        self.assertFalse(
            self.dao.actualizar(
                AgenteChat("ZZZZ", "TL", 0, 1)
            )
        )

    # 7
    def test_07_eliminar_agente_chat(self):

        self.dao.crear(
            AgenteChat("C004", "TL_Gus", 190.0, 1)
        )

        self.assertTrue(
            self.dao.eliminar("C004")
        )

        self.assertIsNone(
            self.dao.obtener("C004")
        )

    # 8
    def test_08_eliminar_agente_inexistente(self):

        self.assertFalse(
            self.dao.eliminar("ZZZZ")
        )

    # 9
    def test_09_listar_todos_los_agentes_chat(self):

        self.dao.crear(
            AgenteChat("C005", "TL_A", 100, 1)
        )

        self.dao.crear(
            AgenteChat("C006", "TL_B", 200, 2)
        )

        self.assertEqual(
            len(self.dao.obtener_todos()),
            2
        )

    # 10
    def test_10_calcular_aht_chat_correcto(self):

        a = AgenteChat("C007", "TL_X", 420.0, 2)

        self.assertEqual(
            a.calcular_aht(),
            420.0
        )


if __name__ == "__main__":
    unittest.main()