class DomainError(Exception):
    code = "domain-error"
    status_code = 500

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

class GameFull(DomainError):
    code = "game-full"
    status_code = 409

class GameNotFound(DomainError):
    code = "game-not-found"
    status_code = 404