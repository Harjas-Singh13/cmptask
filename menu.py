import atexit
import copy
import dataclasses
import logging
import os

from user import User, UserManager

logging.basicConfig(level=logging.INFO)
# use the below logger
logger = logging.getLogger(__name__)


def read_user_from_prompt() -> User:
    user_name = input("Enter user name: ").strip()
    address = input("Enter address: ")
    user_id = input("Enter user id: ")
    return User(name=user_name, user_id=user_id, address=address)


def update_user_info_prompt(user: User) -> User:
    user_copy = copy.deepcopy(user)
    user_copy.name = input(f"Enter new user name:[{user.name}] ").strip() or user.name
    user_copy.address = (
        input(f"Enter new address:[{user.address}] ").strip() or user.address
    )
    return user_copy


def user_menu(user_manager: UserManager):

    while 1:
        option = input(
            """What would you like to do? \n
           1.Create User
           2.Update User 
           3.List all users
           Ctrl-c to exit
           """
        )
        if option == "1":
            user = read_user_from_prompt()
            try:
                user_manager.create_user(user)
            except ValueError:
                print(f"User with id {user.user_id} already exists skipping \n")

        elif option == "2":
            user_id = input("Enter user id to update")
            try:
                user = user_manager.read_user(user_id=user_id)
                updated_user = update_user_info_prompt(user)
                user_manager.update_user(updated_user)
            except ValueError:
                print(f"User {user_id} does not exist \n")
        elif option == "3":
            all_users = "\n".join(
                [str(dataclasses.asdict(v)) for v in user_manager.read_all_users()]
            )
            print(f"All users \n {all_users}")
        else:
            print(f"Invalid option: {option}")


def load_or_init_user_manager(f_name: str) -> UserManager:
    """
    Loads or initializes the user manager
    :param f_name:
    :return:
    """
    if os.path.exists(f_name):
        logger.info(f"loading existing user manager from {f_name}\n")
        return UserManager.deserialize(f_name)
    return UserManager()


def save_user_state(f_name: str, user_manager: UserManager):
    """
    Saves user state at exit
    :param f_name: the location where to serialize
    :param user_manager: the user manager to serialize
    :return:
    """
    user_manager.serialize(f_name=f_name)


if __name__ == "__main__":
    f_name = input("where would you like to save/initialize the user file: ")
    user_manager = load_or_init_user_manager(f_name=f_name)
    atexit.register(save_user_state, f_name=f_name, user_manager=user_manager)
    user_menu(user_manager=user_manager)

    # just shows how to update user info
