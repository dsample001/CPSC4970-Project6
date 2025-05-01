from Curling_League_Manager.model.exceptions import DuplicateOid, DuplicateEmail
from Curling_League_Manager.model.identified_object import IdentifiedObject
from Curling_League_Manager.tests.model_tests.fake_emailer import FakeEmailer
from Curling_League_Manager.model.emailer import Emailer


class Team(IdentifiedObject):
    """Team class"""

    def __init__(self, oid, name):
        """
        Initialization method for TeamMember.
        Args:
            oid: Team ID.
            name: String team name.
        """
        super().__init__(oid)
        self._name = name
        self._members = []

    @property
    def name(self):
        """
        Team name property
        Returns:
            Team name property.
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of the team.
        Args:
            name: String name of the team.

        Returns:

        """
        if name is not None:
            self._name = name

    @property
    def members(self):
        """
        List of team members.
        Returns:
            List of team members.
        """
        return self._members

    def add_member(self, member):
        """
        Adds a team member to the team if the team member is not already on the team.
        Args:
            member: TeamMember object to add to Team.

        Returns:
        Throws: DuplicateOid if member oid is already on the team.
                DuplicateEmail if a member of team has the same email address.

        """
        # Check for identical oid and email.
        for mem in self.members:
            if mem.oid == member.oid:
                raise DuplicateOid("Member has same Oid as other member", member.oid)
            if member.email.lower() in mem.email.lower():
                raise DuplicateEmail("Member has same email as other member", member.email)

        # Moved this check after exceptions so that I could throw DuplicateOid
        if member not in self.members:
            self.members.append(member)

    def member_named(self, s):
        """
        Returns the member of this name whose name is "s" or None if no such member exists.
        Args:
            s: String name of the team member.

        Returns:
            Team member with name "s" if on team.
        """
        for member in self.members:
            if s == member.name:
                return member
        return None

    def remove_member(self, member):
        """
        Removes the specified member from the team.
        Args:
            member: Member of the team to remove.

        Returns:

        """
        if member in self.members:
            self.members.remove(member)

    def send_email(self, emailer, subject, message):
        """
        Sends an email to each member of the team.
        Args:
            emailer: emailer object to send the email.
            subject: String subject of the email.
            message: String email message.

        Returns:

        """
        emails = []
        for mem in self.members:
            emails.append(mem.email)
        emailer.send_plain_email(emails, subject, message)

    def __str__(self):
        """
        Returns a string like the following "Team Name: N members"
        Returns:
            String with team info.
        """
        return f"{self.name}: {len(self.members)} members"
