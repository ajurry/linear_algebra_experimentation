class Vector:
    content = []

    def __init__(self, content: list):
        """Basic constructor for a vector object"""
        for entry in content:
            if not isinstance(entry, (int, float)):
                raise TypeError("Entries should be of type int or float")
            else:
                self.content.append(float(entry))

    def append_dimensions(self, entry: list):
        """Add extra dimensions based on passed list
        These dimensions are appended to the current vector"""

    def __setitem__(self, key, value):
        """Update specified dimension value inside the vector"""
        # self.content[key] = value
