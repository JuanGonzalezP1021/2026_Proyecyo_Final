import json, os

class PhoneDAO:
    """
    PATRÓN DAO: encapsula toda operación de persistencia para AgentePhone.
    SOLID - S: solo gestiona phone_data.json.
    SOLID - O: abierto para extender a BD sin cambiar la interfaz.
    """
    FILE = "data/phone_data.json"

    def _cargar(self) -> dict:
        if not os.path.exists(self.FILE):
            return {}
        with open(self.FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    def _guardar(self, data: dict):
        os.makedirs("data", exist_ok=True)
        with open(self.FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def crear(self, agente) -> bool:
        data = self._cargar()
        if agente.get_agent_id() in data:
            return False
        data[agente.get_agent_id()] = agente.to_dict()
        self._guardar(data)
        return True

    def obtener(self, agent_id: str):
        from modelo.agente_phone import AgentePhone
        data = self._cargar()
        return AgentePhone.from_dict(data[agent_id]) if agent_id in data else None

    def obtener_todos(self) -> list:
        from modelo.agente_phone import AgentePhone
        return [AgentePhone.from_dict(v) for v in self._cargar().values()]

    def actualizar(self, agente) -> bool:
        data = self._cargar()
        if agente.get_agent_id() not in data:
            return False
        data[agente.get_agent_id()] = agente.to_dict()
        self._guardar(data)
        return True

    def eliminar(self, agent_id: str) -> bool:
        data = self._cargar()
        if agent_id not in data:
            return False
        del data[agent_id]
        self._guardar(data)
        return True