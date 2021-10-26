
import dataclasses
import json
import logging
from json import JSONEncoder
from typing import Dict, List

logging.basicConfig(level=logging.INFO)
# use the below logger
logger = logging.getLogger(__name__)


@dataclasses.dataclass
class User:
    name: str
    user_id: str
    address: str = dataclasses.field(default="")

    def __post_init__(self):
        if not self.name or self.name.strip() == "":
            raise ValueError("Name for the user cannot be empty")
        # do more validations


class CustomJSONEncoder(JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        else:
            return JSONEncoder.default(self, o)


@dataclasses.dataclass
class UserManager:
    _state: Dict[str, User] = dataclasses.field(default_factory=dict)

    def create_user(self, user: User):
        """
        Handles creation of user
        :param user:
        :return:
        """
        if user.user_id in self._state:
            raise ValueError("User already exists")
        logger.info("Created User")
        self._state[user.user_id] = user

    def update_user(self, user: User) -> User:
        """
        Updates user information
        :param user:
        :return:
        """
        pass

    def read_user(self, user_id: str) -> User:
        """
        Reads user
        :param user_id:
        :return:
        :raises: ValueError if user cannot be found
        """
        if user_id not in self._state:
            raise ValueError("User not found")
        return self._state[user_id]

    def read_all_users(self) -> List[User]:
        """
        Returns all users
        :return:
        """
        return list(self._state.values())

    def serialize(self, f_name: str):
        with open(f_name, "w") as fout:
            json.dump(self, fout, cls=CustomJSONEncoder)

    @classmethod
    def deserialize(cls, f_name: str) -> "UserManager":
        with open(f_name, "r") as fin:
            state = json.load(fin)["_state"]
            return UserManager({k: User(**v) for k, v in state.items()})


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    user_1 = User(name="jas", user_id="abcd")
    user_2 = User(name="jas", user_id="abcde")
    user_manager = UserManager()
    user_manager.create_user(user_1)
    user_manager.create_user(user_2)
    user_manager.serialize("data.txt")
    user_manager_from_file = UserManager.deserialize("data.txt")
    logger.info(f"Retrieving User {user_manager_from_file.read_user(user_2.user_id)}")
    logger.info(f"All users {user_manager_from_file.read_all_users()}")
    user_3 = User(name="jas", user_id="abcdef")
    user_manager_from_file.create_user(user_3)
    logger.info(f"All users {user_manager_from_file.read_all_users()}")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
