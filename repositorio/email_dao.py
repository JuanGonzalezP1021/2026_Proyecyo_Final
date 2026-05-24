import json
import os


class EmailDAO:

    FILE = "data/email_data.json"

    # LEER JSON
    def _cargar(self):

        if not os.path.exists(self.FILE):
            return {}

        with open(self.FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    # GUARDAR JSON
    def _guardar(self, data):

        os.makedirs("data", exist_ok=True)

        with open(self.FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    # CREATE
    def crear(self, agente):

        data = self._cargar()

        if agente.get_agent_id() in data:
            return False

        data[agente.get_agent_id()] = agente.to_dict()

        self._guardar(data)

        return True

    # READ
    def obtener(self, agent_id):

        from modelo.agente_email import AgenteEmail

        data = self._cargar()

        if agent_id in data:
            return AgenteEmail.from_dict(data[agent_id])

        return None

    # READ TODOS
    def obtener_todos(self):

        from modelo.agente_email import AgenteEmail

        return [
            AgenteEmail.from_dict(v)
            for v in self._cargar().values()
        ]

    # UPDATE
    def actualizar(self, agente):

        data = self._cargar()

        if agente.get_agent_id() not in data:
            return False

        data[agente.get_agent_id()] = agente.to_dict()

        self._guardar(data)

        return True

    # DELETE
    def eliminar(self, agent_id):

        data = self._cargar()

        if agent_id not in data:
            return False

        del data[agent_id]

        self._guardar(data)

        return True