class ConversationManager:
    """
    Memory session provider tracking multi-turn chama debate histories.
    """
    def __init__(self):
        self.sessions = {}

    def get_history(self, session_id: str):
        return self.sessions.get(session_id, [])

    def add_message(self, session_id: str, message: dict):
        if session_id not in self.sessions:
            self.sessions[session_id] = []
        self.sessions[session_id].append(message)
