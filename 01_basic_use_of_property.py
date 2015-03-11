class MyClass:
    def __init__(self, x = 0):
        self._x = x

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def del_x(self):
        del self._x

    x = property(get_x, set_x, del_x, "This is the 'x' property")

if __name__ == "__main__":
    object = MyClass()
    print("[RES ] Initial value:", object.x)            # This line returns 0
    print("[INFO] Setting a new value")
    object.x = 78                                       # Using the setter method
    print("[RES ] Getting the new value:", object.x)    # Using the getter method
    print("[RES ] Getting the new value:", object._x)   # Direct access to the "private" attribute
    print("[INFO] Set of attributes:", object.__dict__) # Listing the set of attributes {'_x': 78}

    # Whit these lines, we can remove the attribute from the class. So,
    # due to that, if we try to print the value of the 'x' property type
    # attribute, an AttributeError exception will be thrown.
    # print("Deleting the value")
    # del object.x
    # print("Deleted value:", object.x)
