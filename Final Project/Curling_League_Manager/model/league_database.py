import csv
import os.path
import pickle

from Curling_League_Manager.model.team import Team
from Curling_League_Manager.model.team_member import TeamMember


class LeagueDatabase:
    _sole_instance = None
    _last_oid: int = 0


    def __init__(self):
        super().__init__()


    @classmethod
    def instance(cls):
        """
        Returns the sole instance of this database, creating one if it doesn't exist

        :return: returns sole instance of LeagueDatabase or creates one if it does not exist.

        """
        if cls._sole_instance is None:
            _sole_instance = cls()
        return cls._sole_instance

    @classmethod
    def load(cls, file_name):
        """
        Loads a LeagueDatabase from the specified file and stores it in _sole_instance.  If file_name does not
        exist or an error occurs when reading it, display a console message (ugh, sorry, it would be better to use the
        logging framework here, but I don't want to go into it) and load the file from the backup (if it exists).
        See save() for information on the backup file.

        :param file_name:
        :return:

        """
        try:
            with open(file_name, mode="rb") as file_data:
                return pickle.load(file_data)
        except FileNotFoundError:
            print("ugh, sorry, it would be better to use the logging framework here but I don't want to go into it")

    @property
    def leagues(self):
        """
        list of the leagues being managed.
        Returns:

        """
        return self.leagues

    def add_league(self, league):
        """
        Add the specified league to the leagues list.
        Args:
            league:

        Returns:

        """
        self.leagues.append(league)

    def remove_league(self, league):
        """
        Remove the specified league from th leagues list.
        Args:
            league:

        Returns:

        """
        self.leagues.remove(league)

    def league_named(self, name):
        """
        Returns th league with the given name or None of no such league exists.
        Args:
            name:

        Returns:

        """
        for league in self.leagues:
            if league.name == name:
                return league
            else:
                return None

    def next_oid(self):
        """
        Increment _list_id and return its new value (used to generate oid for your object).
        Returns:

        """
        self._last_oid += 1
        return self._last_oid

    def save(self, file_name):
        """
        Save this database on the specified file.  Before saving, check if th efile exists and if it does, rename it
        to "file_name" with ".backup" added.
        Args:
            file_name:

        Returns:

        """
        path = './' + file_name
        if os.path.isfile(path):
            # rename file to back-up.
            dest = './' + file_name + ".backup"
            if os.path.isfile(dest):
                os.remove(dest)
            os.rename(path, dest)
        # save file
        with open(file_name, mode="wb") as file_data:
            pickle.dump(self, file_data)

    def import_league_teams(self, league, file_name):
        """
        Load the teams and team members in a league from a CSV formated file.  (The Python standard library has a
        nice CSV module.)  THe file will contain three columns: team name, team member name, email.  The first line
        of the file will be a "header"line and should be ignored.  The file will be UTF-8 encoded and may contain
        non-ASCII text.  Note that the first argument to this method must be a league object, not the name of a league.
        If an error occurs while loading a league, display a message on the console.
        Args:
            league:
            file_name:

        Returns:

        """
        try:
            with open(file_name, encoding='utf-8', mode='rt') as csv_file:
                csv_file = csv.reader(csv_file)

                next(csv_file)
                print(f"{league}  {league.oid}")
                for line in csv_file:
                    team_name = line[0]
                    team_member_name = line[1]
                    email = line[2]

                    # Add team to league
                    if league.team_named(team_name) is not None:
                        pass
                    else:
                        league.add_team(Team(self.next_oid(), team_name))

                    # Add team member
                    curr_team = league.team_named(team_name)
                    if curr_team.member_named(team_member_name) is not None:
                        pass
                    else:
                        curr_member = TeamMember(self.next_oid(), team_member_name, email)
                        curr_team.add_member(curr_member)

        except Exception as err:
            print(f"Something went wrong: {err}")

    def export_league_teams(self, league, file_name):
        """
        write the specified league to a CSV formatted file.  The first line of the file must be a "header" row
        containing the following text (without the leading spaces):
                Team name, Member name, Member email
        If an error occurs while writing a league, display a message on the console.
        Args:
            league:
            file_name:

        Returns:

        """
        header_string = "Team name,Member name,Member email"
        try:
            with open(file_name, mode='wt', encoding="utf-8") as csv_file:
                csv_file.write(f"{header_string}\n")
                for team in league.teams:
                    for member in team.members:
                        if "," in team.name:
                            csv_file.write(f'"{team.name}",')
                        else:
                            csv_file.write(f"{team.name},")
                        if "," in member.name:
                            csv_file.write(f'"{member.name}",')
                        else:
                            csv_file.write(f"{member.name},")
                        if "," in member.email:
                            csv_file.write(f'"{member.email}"\n')
                        else:
                            csv_file.write(f"{member.email}\n")
                # csv_file.write("")
        except Exception as err:
            print(f"Something went wrong: {err}")
