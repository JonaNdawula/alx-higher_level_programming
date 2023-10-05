#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    hidden_names = dir(hidden_4)
    for names in hidden_names:
        if names[:2] != "__":
            print(names)
