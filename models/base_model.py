#!/usr/bin/python3
"""This script is the base model"""

import uuid
from datetime import datetime


class BaseModel:

    """Class from which all other classes will inherit"""

    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self, *args, **kwargs):
        """Initialise instance attributes

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-value arguments
        """
        if kwargs is not NONE and Kwarg != {}:
            return

    def __str__(self):
        """Return official string representation"""

        return "[{}] ({}) {}"\
                .format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all Key/values"""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isodormat()

        return my_dict
