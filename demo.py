class DB:
    def __init__(self):
        self._db = {}

    def put(self, key: str, value: any):
        self._db[key] = value

    def get(self, key: str) -> any | None:
        if key not in self._db.keys():
            raise KeyError(f"Key {key} not found")
        else:
            return self._db[key]

    def exists(self, key: str) -> bool:
        return key in self._db

    def delete(self, key: str):
        self._db.pop(key)
