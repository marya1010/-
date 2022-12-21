import os
import pickle
from typing import Union

from models import User, AuthUser
from utils import hasher


class Storage:

    def __init__(self, file_path: str = "./code/data/dump.pickle") -> None:
        self.file_path = file_path
        self.data = []
        self.read_collection()

    def read_collection(self) -> None:
    #Reading data from file
        if os.path.getsize(self.file_path) > 0:
            with open(self.file_path, 'rb') as stream:
                buf = pickle.load(stream)
        else:
            buf = []
        self.data = buf

    def write_collection(self) -> None:
        #Write data to file
        with open(self.file_path, 'wb') as stream:
            pickle.dump(self.data, stream, protocol=pickle.HIGHEST_PROTOCOL)

    def user_auth(self, check_user: AuthUser) -> Union[User, None]:
        #Log in method
        for user in self.data:
            if user.email == check_user.email and user.password == hasher(check_user.password):
                return user
        return None

    def user_reg(self, user: User) -> None:
        #register
        user.password = hasher(user.password)
        self.data.append(user)
        self.write_collection()

    def clear(self) -> None:
        #drop all notes
        self.data = []
        self.write_collection()
