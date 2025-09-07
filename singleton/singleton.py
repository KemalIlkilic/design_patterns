from __future__ import annotations
from threading import Lock

class Database:
    """
        The Singleton's constructor should be hidden from the client code.
        Calling the get_instance method should be the only way of getting the Singleton object.
    """
    # instance is instance of Database (Singleton) class
    # instance : Database
    _instance: Database | None = None
    _lock = Lock()

    def __init__(self):
        raise RuntimeError("Use get_instance() instead of direct constructor")

    # Class instance method
    def _connect_to_server(self):
        self.connection = "Connected to database"

    # Class instance method
    def query(self, sql: str)   :
        print(f"Executing query: {sql} on {self.connection}")

    # Class method
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            # __new__ is called before __init__. It's responsible for creating (allocating) the object.
            # Responsible for creating a new instance of the class.
            """
                When instance EXISTS, multiple threads can safely read the same instance so no lock is needed.
                When instance is NULL, multiple threads will try to CREATE a new instance which involves WRITING/MODIFYING the cls._instance variable, so lock IS needed because writing is NOT thread-safe.
            """
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    # It shows you might want to do some work only once when the singleton is first created.
                    cls._instance._connect_to_server()
        return cls._instance


