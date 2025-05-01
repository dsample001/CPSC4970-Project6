from Curling_League_Manager.model.identified_object import IdentifiedObject
from Curling_League_Manager.tests.model_tests.fake_emailer import FakeEmailer
from Curling_League_Manager.model.emailer import Emailer


class Competition(IdentifiedObject):
    """Competition class"""

    def __init__(self, oid, teams, location, datetime=None):
        """
        Initializes Competition object that sets the oid, teams, location, and datetime properties as specified in the
        arguments.
        Args:
            oid: id of the object
            teams: list of the two teams that are competing against each other.
            location: String location of the competition
            datetime: optional Python datetime object indicating when the competition will begin.
        """
        super().__init__(oid)
        self._teams = teams
        self._location = location
        self._datetime = datetime

    @property
    def teams_competing(self):
        """
        Read only property of the competition object.
        Returns:
            list of the two teams that are competing against each other.

        """
        return self._teams

    @property
    def location(self):
        """
        Property location of the competition.
        Returns:
            String location of the competition.
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of the competition.
        Args:
            location: String location of the competition.

        Returns:

        """
        if location is not None:
            self._location = location

    @property
    def date_time(self):
        """
        Property date time of the competition.
        Returns:
            The datetime of the competition.
        """
        return self._datetime

    @date_time.setter
    def date_time(self, datetime):
        """
        Sets the date time of the competition.
        Args:
            datetime: datetime

        Returns:

        """
        if datetime is not None:
            self._datetime = datetime

    def send_email(self, emailer, subject, message):
        """
        Send email to all members of all teams in this competition without duplicates.
        Args:
            emailer: Emailer object to send email.
            subject: String subject of the email.
            message: String message of the email.

        Returns:

        """
        emails = set()
        for mem in self.teams_competing.members:
            emails.add(mem.email)
        emailer.send_plain_email(emails, subject, message)

    def __str__(self):
        """
        Returns a string like the following "Competition at location on date_time with N teams"
        Returns:
            String with competition info.
        """
        # "12/31/1995 19:30"
        if self.date_time is None:
            temp_datetime = "TBD"
        else:
            temp_datetime = self.date_time.strftime("%m/%d/%G %H:%M")
        return (f"Competition at {self.location} on {temp_datetime} "
                f"with {self.teams_competing[0].name} "
                f"against {self.teams_competing[1].name}.")
