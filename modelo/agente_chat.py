class AgenteChat:

    def __init__(self, agent_id, team_manager,
                 chat_aht=0.0, concurrent_chats=1):

        self._agent_id = agent_id
        self._team_manager = team_manager
        self._chat_aht = chat_aht
        self._concurrent_chats = concurrent_chats

    def get_agent_id(self):
        return self._agent_id

    def get_team_manager(self):
        return self._team_manager

    def get_chat_aht(self):
        return self._chat_aht

    def get_concurrent_chats(self):
        return self._concurrent_chats

    def set_chat_aht(self, value):
        self._chat_aht = value

    def set_concurrent_chats(self, value):
        self._concurrent_chats = value

    def calcular_aht(self):
        return round(self._chat_aht, 2)

    def to_dict(self):

        return {
            "agent_id": self._agent_id,
            "team_manager": self._team_manager,
            "chat_aht": self._chat_aht,
            "concurrent_chats": self._concurrent_chats,
            "canal": "Chat"
        }

    @classmethod
    def from_dict(cls, data):

        return cls(
            data["agent_id"],
            data["team_manager"],
            data.get("chat_aht", 0.0),
            data.get("concurrent_chats", 1)
        )
