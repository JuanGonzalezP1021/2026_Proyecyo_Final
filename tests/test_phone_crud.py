import unittest, os
from modelo.agente_phone import AgentePhone
from repositorio.phone_dao import PhoneDAO

class TestPhoneCRUD(unittest.TestCase):
    def setUp(self):
        self.dao = PhoneDAO()
        self.dao.FILE = "data/test_phone.json"
        if os.path.exists(self.dao.FILE):
            os.remove(self.dao.FILE)

    def tearDown(self):
        if os.path.exists(self.dao.FILE):
            os.remove(self.dao.FILE)

    def test_01_crear_agente(self):
        self.assertTrue(self.dao.crear(AgentePhone("P001", "TL_Maria", 5000.0, 25)))

    def test_02_no_duplicar(self):
        a = AgentePhone("P001", "TL_Maria", 5000.0, 25)
        self.dao.crear(a)
        self.assertFalse(self.dao.crear(a))

    def test_03_leer_agente(self):
        self.dao.crear(AgentePhone("P002", "TL_Juan", 3000.0, 15))
        self.assertEqual(self.dao.obtener("P002").get_agent_id(), "P002")

    def test_04_leer_inexistente(self):
        self.assertIsNone(self.dao.obtener("ZZZZ"))

    def test_05_actualizar(self):
        a = AgentePhone("P003", "TL_Ana", 1000.0, 10)
        self.dao.crear(a)
        a.set_handle_time(2000.0)
        self.dao.actualizar(a)
        self.assertEqual(self.dao.obtener("P003").get_handle_time(), 2000.0)

    def test_06_actualizar_inexistente(self):
        self.assertFalse(self.dao.actualizar(AgentePhone("ZZZZ", "TL", 0, 0)))

    def test_07_eliminar(self):
        self.dao.crear(AgentePhone("P004", "TL_Luis", 800.0, 8))
        self.assertTrue(self.dao.eliminar("P004"))
        self.assertIsNone(self.dao.obtener("P004"))

    def test_08_eliminar_inexistente(self):
        self.assertFalse(self.dao.eliminar("ZZZZ"))

    def test_09_listar_todos(self):
        self.dao.crear(AgentePhone("P005", "TL_A", 500, 5))
        self.dao.crear(AgentePhone("P006", "TL_B", 600, 6))
        self.assertEqual(len(self.dao.obtener_todos()), 2)

    def test_10_aht_correcto(self):
        self.assertEqual(AgentePhone("P007", "TL_C", 1000.0, 5).calcular_aht(), 200.0)

if __name__ == "__main__":
    unittest.main()