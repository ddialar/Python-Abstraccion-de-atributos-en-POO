class MyClass:
    def __init__(self, x = 0):
        self.x = x
        # At the end of the class script, the 'x' attribute which is been
        # used as input parameter, will be turned into a "property" type
        # object.

    # I'm going to declare the '__x' attribute as "private" through
    # two underscores. This operation is going to be dinamically run
    # into the same methods.
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @x.deleter
    def x(self):
        del self.__x

    # The last three methods are equivalent to this one:
    # x = property(get_x, set_x, del_x)

if __name__ == "__main__":
    object = MyClass()
    print("[RES ] Initial value:", object.x)            # This line returns 0
    print("[INFO] Setting a new value")
    object.x = 78                                       # Using the setter method
    print("[RES ] Getting the new value:", object.x)    # Using the getter method
    # print("[RES ] Getting the new value:", object.__x)  # This line will threw an AttributeError
                                                        # exception because we cannot directly
                                                        # access to a double underscored attribute.
    print("[INFO] Set of attributes:", object.__dict__) # Listing the set of attributes {'_MyClass__x': 78}

    # Whit these lines, we can remove the attribute from the class. So,
    # due to that, if we try to print the value of the 'x' property type
    # attribute, an AttributeError exception will be thrown.
    # print("Deleting the value")
    # del object.x
    # print("Deleted value:", object.x)
