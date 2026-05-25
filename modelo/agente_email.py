class AgenteEmail:

    def __init__(self, agent_id, team_manager,
                 handle_time=0.0,
                 inbound_tx=0,
                 acw=0.0):

        self._agent_id = agent_id
        self._team_manager = team_manager
        self._handle_time = handle_time
        self._inbound_tx = inbound_tx
        self._acw = acw

    # GETTERS
    # Metodos para calcular indicadores del agente
    def get_agent_id(self):
        return self._agent_id

    def get_team_manager(self):
        return self._team_manager

    def get_handle_time(self):
        return self._handle_time

    def get_inbound_tx(self):
        return self._inbound_tx

    def get_acw(self):
        return self._acw

    # SETTERS
    def set_handle_time(self, v):
        self._handle_time = v

    def set_acw(self, v):
        self._acw = v

    # CALCULOS
    def calcular_aht(self):

        if self._inbound_tx == 0:
            return 0.0

        return round(self._handle_time / self._inbound_tx, 2)

    def calcular_acw_promedio(self):

        if self._inbound_tx == 0:
            return 0.0

        return round(self._acw / self._inbound_tx, 2)

    # JSON
    def to_dict(self):

        return {
            "agent_id": self._agent_id,
            "team_manager": self._team_manager,
            "handle_time": self._handle_time,
            "inbound_tx": self._inbound_tx,
            "acw": self._acw,
            "canal": "Email"
        }

    @classmethod
    def from_dict(cls, d):

        return cls(
            d["agent_id"],
            d["team_manager"],
            d.get("handle_time", 0.0),
            d.get("inbound_tx", 0),
            d.get("acw", 0.0)
        )

    def __repr__(self):

        return f"AgenteEmail(id={self._agent_id}, aht={self.calcular_aht()}s)"