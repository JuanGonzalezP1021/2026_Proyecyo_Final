import json
import os

from modelo.agente_email import AgenteEmail

_BASE = os.path.dirname(os.path.abspath(__file__))


class EmailDAO:
    """DAO canal Email. CRUD sobre email_data.json."""

    FILE = os.path.join(_BASE, "..", "data", "email_data.json")

    def __init__(self, archivo=None):
        self.archivo = archivo if archivo else self.FILE

    # --- Acceso a datos (lo unico que cambiaria al migrar a SQLite) ---
    def _cargar(self):
        # Archivo inexistente o vacio -> lista vacia (evita JSONDecodeError)
        if not os.path.exists(self.archivo) or os.path.getsize(self.archivo) == 0:
            return []
        with open(self.archivo, encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                # JSON corrupto: no tumbamos el programa, arrancamos vacio
                return []

    def _guardar(self, registros):
        carpeta = os.path.dirname(self.archivo)
        if carpeta:
            os.makedirs(carpeta, exist_ok=True)
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(registros, f, ensure_ascii=False, indent=2)

    # --- CRUD ---
    def crear(self, agente):
        registros = self._cargar()
        if any(r["agent_id"] == agente.get_agent_id() for r in registros):
            return False
        registros.append(agente.to_dict())
        self._guardar(registros)
        return True

    def obtener(self, agent_id):
        for r in self._cargar():
            if r["agent_id"] == agent_id:
                return AgenteEmail.from_dict(r)
        return None

    def obtener_todos(self):
        return [AgenteEmail.from_dict(r) for r in self._cargar()]

    def actualizar(self, agente):
        registros = self._cargar()
        for i, r in enumerate(registros):
            if r["agent_id"] == agente.get_agent_id():
                registros[i] = agente.to_dict()
                self._guardar(registros)
                return True
        return False

    def eliminar(self, agent_id):
        registros = self._cargar()
        nuevos = [r for r in registros if r["agent_id"] != agent_id]
        if len(nuevos) == len(registros):
            return False
        self._guardar(nuevos)
        return True