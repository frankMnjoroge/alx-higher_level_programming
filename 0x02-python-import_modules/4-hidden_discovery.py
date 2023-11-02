#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    module_path = 'C:\Users\Jackline Shali\Downloads\hidden_4.pyc'
    with open(module_path, 'rb') as file:
    code = marshal.load(file)
    for name in sorted(dir(hidden_4)):
       if name[:2] != '__':
            print("{}".format(name))
