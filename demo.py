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
        keys = self._db.keys()
        for k in keys:
            if k == key:
                return True
        return False
