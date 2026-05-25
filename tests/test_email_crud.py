import unittest
import os

from modelo.agente_email import AgenteEmail
from repositorio.email_dao import EmailDAO


class TestEmailCRUD(unittest.TestCase):

    def setUp(self):

        self.dao = EmailDAO()

        self.dao.FILE = "data/test_email.json"

        if os.path.exists(self.dao.FILE):
            os.remove(self.dao.FILE)

    def tearDown(self):

        if os.path.exists(self.dao.FILE):
            os.remove(self.dao.FILE)

    # 1
    def test_01_crear_agente(self):

        a = AgenteEmail("E001", "TL_Sara", 7200.0, 30)

        self.assertTrue(self.dao.crear(a))

    # 2
    def test_02_no_duplicar(self):

        a = AgenteEmail("E001", "TL_Sara", 7200.0, 30)

        self.dao.crear(a)

        self.assertFalse(self.dao.crear(a))

    # 3
    def test_03_leer_agente(self):

        self.dao.crear(
            AgenteEmail("E002", "TL_Marco", 5000.0, 20)
        )

        r = self.dao.obtener("E002")

        self.assertEqual(r.get_agent_id(), "E002")

    # 4
    def test_04_leer_inexistente(self):

        self.assertIsNone(self.dao.obtener("ZZZZ"))

    # 5
    def test_05_actualizar_handle_time(self):

        a = AgenteEmail("E003", "TL_Ines", 3000.0, 15)

        self.dao.crear(a)

        a.set_handle_time(6000.0)

        self.dao.actualizar(a)

        self.assertEqual(
            self.dao.obtener("E003").get_handle_time(),
            6000.0
        )

    # 6
    def test_06_actualizar_inexistente(self):

        self.assertFalse(
            self.dao.actualizar(
                AgenteEmail("ZZZZ", "TL", 0, 0)
            )
        )

    # 7
    def test_07_eliminar(self):

        self.dao.crear(
            AgenteEmail("E004", "TL_Dario", 2000.0, 10)
        )

        self.assertTrue(self.dao.eliminar("E004"))

        self.assertIsNone(self.dao.obtener("E004"))

    # 8
    def test_08_eliminar_inexistente(self):

        self.assertFalse(self.dao.eliminar("ZZZZ"))

    # 9
    def test_09_listar_todos(self):

        self.dao.crear(
            AgenteEmail("E005", "TL_A", 500, 5)
        )

        self.dao.crear(
            AgenteEmail("E006", "TL_B", 1000, 10)
        )

        self.assertEqual(
            len(self.dao.obtener_todos()),
            2
        )

    # 10
    def test_10_aht_email_correcto(self):

        a = AgenteEmail("E007", "TL_Z", 3000.0, 10)

        self.assertEqual(a.calcular_aht(), 300.0)


if __name__ == "__main__":
    unittest.main()