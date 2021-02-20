
class Vector:
    content = []

    def __init__(self, content: list):
        """Basic constructor for a vector object"""
        self.content.clear()
        for entry in content:
            if not isinstance(entry, (int, float)):
                raise TypeError(
                "List entries cannot be {}, they should be int or float".format(type(entry))
                )
            else:
                self.content.append(float(entry))

    def __len__(self):
        return len(self.content)

    def __getitem__(self, index):
        """Get a specified dimension value inside the vector"""
        if index < 0:
            raise IndexError("Cannot access with negative index")
        return self.content[index]


    def __setitem__(self, index, value):
        """Update specified dimension value inside the vector"""
        if index < 0:
            raise IndexError("Cannot set with negative index")

        if  not isinstance(value, (int, float)):
            raise TypeError("Cannot set entries with type {}".format(type(value)))

        self.content[index] = value

    def append(self, appendage):
        """Add extra dimensions based on passed Vector
        These dimensions are appended to the current vector"""
        test = self.content
        if isinstance(appendage, Vector):
            self.content.extend(appendage.content)
        elif isinstance(appendage, (int, float)):
            self.content.append(appendage)
        else:
            raise TypeError("Cannot not append entries with type {}".format(type(appendage)))
            
