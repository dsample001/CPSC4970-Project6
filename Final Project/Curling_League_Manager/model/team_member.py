from Curling_League_Manager.model.identified_object import IdentifiedObject
# from tests.fake_emailer import FakeEmailer
from Curling_League_Manager.model.emailer import Emailer


class TeamMember(IdentifiedObject):
    """TeamMember Class"""

    def __init__(self, oid, name, email):
        """
        Initializes TeamMember object that sets the oid, name, and email properties in the arguments
        Args:
            oid: object id
            name: String team member name.
            email: String email address for team member.
        """
        super().__init__(oid)
        self._name = name
        self._email = email

    @property
    def name(self):
        """
        team member name property.
        Returns:
            Team member name.

        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the team member name property.
        Args:
            name: String name for team member.

        Returns:

        """
        if name is not None:
            self._name = name

    @property
    def email(self):
        """
        team member email address property.
        Returns:
            Team member email address.
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the team member email address property.
        Args:
            email: String email address for team member.

        Returns:

        """
        if email is not None:
            self._email = email

    def send_email(self, emailer, subject, message):
        """
        Sends an email to the specified team member email address.
        Args:
            emailer: emailer object to send email.
            subject: String subject for the email.
            message: String message for the email.

        Returns:

        """
        emailer.send_plain_email([self.email], subject, message)

    def __str__(self):
        """
        String representation of team member like: "Name<Email>"
        Returns:
            String with team member name and email address.
        """
        return f"{self.name}<{self.email}>"
