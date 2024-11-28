class Config:
    OPERATIONS = {
        'add': 'ADD',
        'subtract': 'SUBTRACT',
        'multiply': 'MULTIPLY',
        'divide': 'DIVIDE',
        'mamas' : 'MAMAS'
    }
    MAMAS = 6
    @staticmethod
    def get_mamas():
        return Config.MAMAS
    @staticmethod
    def get_operations():
        return Config.OPERATIONS
    