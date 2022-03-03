#!/usr/bin/python3
"""This module defines a class to manage file storage for using a database
"""
import os

from models.base_model import Base, BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, session, scoped_session
# from importlib_metadata import metadata





class DBStorage:
    """This class manages storage of hbnb models in SQL format
    """

    __engine = None
    __session = None

    def __init__(self):
        """Instantiates Instance into DBStorage using env vars
        """
        dialect = "mysql"
        driver = "mysqldb"
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        
        self.__engine = create_engine('{}+{}://{}:{}@{}/{}'
                                .format(dialect, driver, user, passwd, host,
                            db), pool_pre_ping=True)
        env = os.getenv("HBNB_ENV")
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ import modules
        """
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        # query on the current database session (self.__session) all objects depending of the class name (argument cls)
        new_dict = {}

        if cls!=None:
            objects = self.__session.query(cls).all()
            for i in objects:
                key = object.__class__.__name__ + "." + object.id
                new_dict.update({key: i})
            return(new_dict)
        else:
            new_dict2 = {}
            state = self.all(State)
            new_dict2.update(new_dict)
            user = self.all(User)
            new_dict2.update(new_dict)
            user = self.all(City)
            new_dict2.update(new_dict)
            user = self.all(Amenity)
            new_dict2.update(new_dict)
            user = self.all(Place)
            new_dict2.update(new_dict)
            user = self.all(Review)
            new_dict2.update(new_dict)
            return(new_dict2)

    def new(self, obj):
        """ add an object to the session
        """
        self.__session.add(obj)

    def save(self, obj):
        """ save an object to the session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete an object from the session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ This method sets the engine and loads the session
        """
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
