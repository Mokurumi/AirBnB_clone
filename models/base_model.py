import uuid
from datetime import datetime

class BaseModel:
    """
    This is a base class that defines common attributes
        and methods for other classes.
    """

    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.

        Attributes:
            id (str): A unique identifier generated using uuid.uuid4().
            created_at (datetime): Date n time the instance is created.
            updated_at (datetime): Date n time the instance is last updated.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
            str: A string in the format
                '[<class name>] (<self.id>) <self.__dict__>'.
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
                )

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the object.

        Returns:
            dict: A dictionary containing all attributes of the instance,
                    including class name, 'created_at',
                        and 'updated_at' in ISO format.
        """
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data
