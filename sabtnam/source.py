from string import ascii_letters


not_allowed = ["quera", "codecup"]


def clear(val):
    chars_len = len([i for i in str(val) if i in ascii_letters])
    if (
        val not in not_allowed
        and len(val) >= 4
        and not str(val).isnumeric()
        and chars_len > 4
    ):
        return True
    return False


def check_registration_rules(**kwargs):
    usernames = [str(k) for k, v in kwargs.items() if clear(str(v))]
    return usernames
