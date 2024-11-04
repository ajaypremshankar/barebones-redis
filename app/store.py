_store = {}


class Store:
    @staticmethod
    def set_val(key: str, val):
        global _store
        _store[key] = val

    @staticmethod
    def get_val(key: str, default_val=None):
        global _store
        return _store.get(key, default_val)

    @staticmethod
    def delete_val(key: str):
        Store.set_val(key, None)
