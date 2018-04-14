class PrintableClass:
    def __printable_attributes__() -> list:
        """Function returning attributes which fields and properties
        should be printed. Other classes can inherit from this one and overload
        this method.

        Returns:
        -------
        list
            list of str, each denoting a property
        """
        return []

    def __str__(self) -> str:
        atts = self.__printable_attributes__()
        vals = ["{}: {}".format(at, getattr(self, at)) for at in atts]
        vals_str = ", ".join(vals)

        return "<{}.{} instance at {} with attributes {}>".format(self.__class__.__module__,
                                                                  self.__class__.__name__,
                                                                  hex(id(self)), vals_str)
