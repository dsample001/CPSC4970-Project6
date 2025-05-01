class IdentifiedObject:
    """abstract class of Identified Objects"""

    def __init__(self, oid):
        """
        initialization method that sets the oid property as specified by the argument.
        Args:
            oid: id number for the object.
        """
        self._oid = oid

    @property
    def oid(self):
        """id for this object."""
        return self._oid

    def __eq__(self, other):
        """
        Overrides the equality operator for two IdentifiedObjects.  They are equal if they have the same type and
        same oid.
        Args:
            other: The second IdentifiedObject to compare.

        Returns:
            Boolean indicating if the two objects are equal.
        """
        if self is other:
            return True
        if type(self) is type(other) and self.oid == other.oid:
            return True
        else:
            return False

    def __hash__(self):
        """
        Defines the hash code for the IdentifiedObject.
        Returns:
            Hash code based on the oid for the IdentifiedObject.
        """
        return hash(self.oid)
