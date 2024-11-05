_data_store = {}
_config_store = {}


class GlobalDataStore:
    @staticmethod
    def set_val(key: str, val):
        global _data_store
        _data_store[key] = val

    @staticmethod
    def get_val(key: str, default_val=None):
        global _data_store
        return _data_store.get(key, default_val)

    @staticmethod
    def delete_val(key: str):
        global _data_store
        del _data_store[key]


class GlobalConfigStore:
    @staticmethod
    def set_val(key: str, val):
        global _config_store
        _config_store[key] = val

    @staticmethod
    def get_val(key: str, default_val=None):
        global _config_store
        return _config_store.get(key, default_val)

    @staticmethod
    def delete_val(key: str):
        global _config_store
        del _config_store[key]

    @staticmethod
    def set_config(config: dict):
        global _config_store
        _config_store = config
