class DB:
    def __init__(self):
        self._db = {}

    def put(self, key: str, value: any):
        self._db[key] = value

    def get(self, key: str) -> any | None:
        return self._db.get(key)

    def exists(self, key: str) -> bool:
        return key in self._db
