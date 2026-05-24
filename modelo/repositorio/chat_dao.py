import json
import os


class ChatDAO:

    FILE = "data/chat_data.json"

    def _cargar(self):

        if not os.path.exists(self.FILE):
            return {}

        with open(self.FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    def _guardar(self, data):

        os.makedirs("data", exist_ok=True)

        with open(self.FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def crear(self, agente):

        data = self._cargar()

        if agente.get_agent_id() in data:
            return False

        data[agente.get_agent_id()] = agente.to_dict()

        self._guardar(data)

        return True

    def obtener(self, agent_id):

        from modelo.agente_chat import AgenteChat

        data = self._cargar()

        if agent_id in data:
            return AgenteChat.from_dict(data[agent_id])

        return None

    def obtener_todos(self):

        from modelo.agente_chat import AgenteChat

        data = self._cargar()

        return [
            AgenteChat.from_dict(value)
            for value in data.values()
        ]

    def actualizar(self, agente):

        data = self._cargar()

        if agente.get_agent_id() not in data:
            return False

        data[agente.get_agent_id()] = agente.to_dict()

        self._guardar(data)

        return True

    def eliminar(self, agent_id):

        data = self._cargar()

        if agent_id not in data:
            return False

        del data[agent_id]

        self._guardar(data)

        return True
