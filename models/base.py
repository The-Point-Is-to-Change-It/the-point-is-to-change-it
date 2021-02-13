class Base():
    """
    Base Model is for serialization
    """

    def __init__(self, *args, **kwargs):
        from uuid import uuid4
        for (k, v) in kwargs.items():
            setattr(self, k, v)
        if not 'id' in kwargs.items():
            self.id = str(uuid4())

    def to_dict(self):
        """
        Turn the object into a dictionary
        """
        return self.__dict__