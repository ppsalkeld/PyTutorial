from typing import List, Any, Union, Dict


def word_length(self):  # The argument would be a list or string
    # like ['cat', 'window', 'defenestrate']
    words = self
    for w in words:  # 'for' statement iterates by each element of a list
        # and each letter of a string.
        # Any variable name may be used for 'w'
        print(w, 'has', len(w), 'letters.')


def copy_and_mod_collection(items=None):
    users: List[Union[List[str], Any]] = [['Deschler', 'active'], ['Chandler', 'active'],
             ['Siebenlist', 'active'], ['Hollister', 'inactive'],
             ['Bagamery', 'active'], ['Ogechukwu', 'inactive'],
             ['Negri', 'inactive'], ['Malek', 'inactive'],
             ['Chen', 'active'], ['Murphy', 'active'],
             ['Dobson', 'active']]

    print("\nThis method makes a copy of a collection 'users' and then modifies the"
          " copy to include only the active users.")
    active_users: Dict[Any, Any] = {}
    for user, status in users:
        if status == 'active':
            active_users[user] = status
    print('The new list, active_users:', active_users)

    print("\nThis method revises the list 'users' to include only the active users.")

    for user, status in users[:]:
        if status == 'inactive':
            users.remove([user, status])    # Must both the index and property
    print('This modified the users list to:', users)

