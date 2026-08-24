class Singleton:
    _instance = None

    def __init__(self):
        if Singleton._instance is not None:
            raise Exception("This class is a singleton")
        else:
            Singleton._instance = self
        self.configuration = {}

    @staticmethod
    def getInstance():
        if Singleton._instance is None:
            Singleton._instance = Singleton()
        return Singleton._instance

    def set_config(self, key, value):
        self.configuration[key] = value

    def get_config(self, key):
        return self.configuration.get(key, None)

    def display_config(self):
        for key, value in self.configuration.items():
            print(f"{key}: {value}")

if __name__ == '__main__':
    print("Instance 1:")
    singleton_instance = Singleton.getInstance()
    singleton_instance.set_config("database", "PostgreSQL")
    singleton_instance.set_config("cache", "Redis")
    singleton_instance.set_config("API", "Flask")
    singleton_instance.display_config()

    print('\nInstance 2:')
    another_instance = Singleton.getInstance()
    another_instance.display_config()

    assert singleton_instance is another_instance
    print("\nInstances are the same:", singleton_instance is another_instance)