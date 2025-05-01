from Curling_League_Manager.model.exceptions import DuplicateOid
from Curling_League_Manager.model.identified_object import IdentifiedObject


class League(IdentifiedObject):
    """Class for League objects"""

    def __init__(self, oid: object, name: object) -> None:
        """
        Initialize a League object.
        Args:
            oid: object id for this League object
            name: name of this League object
        """
        super().__init__(oid)
        self._name = name
        self._teams = []
        self._competitions = []

    @property
    def name(self):
        """
        name property for the League object
        Returns:
            Name of the League object
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        name setter for the League object
        Args:
            name: name for the League object

        Returns:

        """
        if name is not None:
            self._name = name

    @property
    def teams(self):
        """
        teams property containing a list of teams for the League object
        Returns:
            list of teams for the League object.
        """
        return self._teams

    @property
    def competitions(self):
        """
        Competitions property containing a list of competitions for the League object
        Returns:

        """
        return self._competitions

    def add_team(self, team):
        """
        Adds a Team object to the list of teams for the League object
        Args:
            team: Team object to add to the list of Team objects for the League object.

        Returns:
        Throws: DuplicateOid if the team oid already exists in league.

        """
        # Check for identical oid.
        for league_teams in self.teams:
            if team.oid == league_teams.oid:
                raise DuplicateOid("Team has same Oid as team in league", team.oid)

        if team not in self.teams:
            self._teams.append(team)

    def remove_team(self, team):
        """
        Removes a Team object to the list of teams for the League object
        Args:
            team: Team object to be removed from the list of team objects for the League object.

        Returns:
        Throws: ValueError if the team has a competition scheduled.

        """
        # check if team is in league
        if team in self._teams:

            # get list of competitions for team.
            comp = self.competitions_for_team(team)

            # check if team has a competition scheduled, then raise error.
            if len(comp) > 0:
                raise ValueError(f"{team.name} cannot be removed, it has competitions")

            # remove team.
            self._teams.remove(team)

    def team_named(self, team_name):
        """
        Returns the team object if the team name (case-sensitive) is in the list of teams for the League object or None.
        Args:
            team_name: Name of Team object.

        Returns:
            Team object if the team name is in the list of teams for the League object, else None.
        """
        for name in self.teams:
            if team_name == name.name:
                return name
        return None

    def add_competition(self, competition):
        """
        Adds a Competition object to the list of competitions for the League object
        Args:
            competition: Competition object to be added to the list of competitions for the League object.

        Returns:

        Throws: ValueError exception if team in competition is not a member of this league.

        """
        # Make sure teams in competition are both members of this league.
        for team in competition.teams_competing:
            if team not in self.teams:
                raise ValueError(f"Team {team.name} is not a member of this league.")

        self._competitions.append(competition)

    def teams_for_member(self, member):
        """
        Returns a list of all Team objects for which the TeamMember object is part of.
        Args:
            member: TeamMember object

        Returns:
            List of Team object that the TeamMember object is a part of.
        """
        member_teams = []
        for team in self.teams:
            if member in team.members:
                member_teams.append(team)
        return member_teams

    def competitions_for_team(self, team):
        """
        Returns a list of all competitions in which the team is participating in.
        Args:
            team: Team object.

        Returns:
            List of competitions.
        """
        comp_set = []
        for comp in self.competitions:
            if team in comp.teams_competing:
                comp_set.append(comp)
        return comp_set

    def competitions_for_member(self, member):
        """
        Returns a list of all competitions for which a member is on one of the competing teams.
        Args:
            member: Member object

        Returns:
            List of competitions.
        """
        comp_set = []
        for comp in self.competitions:
            for team in comp.teams_competing:
                if member in team.members:
                    comp_set.append(comp)
        return comp_set

    def __str__(self):
        """
        Returns a string resembling the following "League Name: N teams, M competitions"
        Returns:
            String with league info.
        """
        return f"League {self.name}: {len(self.teams)} teams, {len(self.competitions)} competitions"
