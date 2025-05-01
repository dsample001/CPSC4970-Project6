import unittest

from Curling_League_Manager.model.league import League
from Curling_League_Manager.model.league_database import LeagueDatabase


class LeagueTests(unittest.TestCase):

    def test_load_league(self):
        ld = LeagueDatabase()
        ld.load("test.dat")

    def test_load_league_with_file_not_found(self):
        ld = LeagueDatabase()
        ld.load("Teams_1.csv")
        self.assertTrue(True)   # asserting true that no un handled exceptions are raised.

    def test_import_leage_teams(self):
        ld = LeagueDatabase()
        new_league = League(ld.next_oid(), "New League")
        ld.import_league_teams(new_league, "Teams.csv")
        print(new_league)
        self.assertTrue(True)

    def test_save_league_database(self):
        ld = LeagueDatabase()
        new_league = League(ld.next_oid(), "New League")
        ld.import_league_teams(new_league, "Teams.csv")
        ld.save("test.dat")
        self.assertTrue(True)

    def test_load_league_database(self):
        ld = LeagueDatabase()
        new_league = League(ld.next_oid(), "New League")
        ld.import_league_teams(new_league, "Teams.csv")
        ld.save("test.dat")
        ld.load("test.dat")
        print(new_league)

    def test_export_league_database(self):
        ld = LeagueDatabase()
        new_league = League(ld.next_oid(), "New League")
        ld.import_league_teams(new_league, "Teams.csv")
        ld.export_league_teams(new_league,"Teams_new.csv")
        print(new_league)
