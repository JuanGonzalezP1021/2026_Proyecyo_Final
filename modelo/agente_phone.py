class AgentePhone:
    """
    ENTIDAD: Agente del canal Phone.
    SOLID - S: solo representa datos del agente Phone.
    """
    def __init__(self, agent_id: str, team_manager: str,
                 handle_time: float = 0.0, inbound_tx: int = 0):
        self._agent_id     = agent_id
        self._team_manager = team_manager
        self._handle_time  = handle_time
        self._inbound_tx   = inbound_tx

    def get_agent_id(self):       return self._agent_id
    def get_team_manager(self):   return self._team_manager
    def get_handle_time(self):    return self._handle_time
    def get_inbound_tx(self):     return self._inbound_tx
    def set_handle_time(self, v): self._handle_time = v
    def set_inbound_tx(self, v):  self._inbound_tx = v

    def calcular_aht(self) -> float:
        if self._inbound_tx == 0: return 0.0
        return round(self._handle_time / self._inbound_tx, 2)

    def to_dict(self) -> dict:
        return {
            "agent_id":     self._agent_id,
            "team_manager": self._team_manager,
            "handle_time":  self._handle_time,
            "inbound_tx":   self._inbound_tx,
            "canal":        "Phone"
        }

    @classmethod
    def from_dict(cls, d: dict):
        return cls(d["agent_id"], d["team_manager"],
                   d.get("handle_time", 0.0), d.get("inbound_tx", 0))

    def __repr__(self):
        return f"AgentePhone(id={self._agent_id}, aht={self.calcular_aht()}s)"