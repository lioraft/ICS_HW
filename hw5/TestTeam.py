from unittest import TestCase
from Team import Team
from NaivePlayer import NaivePlayer
from MaxScorePlayer import MaxScorePlayer
from Hand import Hand
from Domino import Domino
from Board import Board


class TestTeam(TestCase):
    def setUp(self):
        """
        setup for tests
        """
        self.center = MaxScorePlayer("Reynolds", 25, Hand([Domino(6, 6), Domino(6, 6)]))
        self.point_guard = NaivePlayer("Evans", 25, Hand([Domino(5, 3), Domino(2, 6)]))
        self.guard = NaivePlayer("Wilbekin", 25, Hand([Domino(4, 2), Domino(3, 4)]))
        self.maccabi = Team("Maccabi", [self.center, self.point_guard, self.guard])

    def test_init(self):
        """
        Test for init
        """
        self.assertIsInstance(self.maccabi, Team)
        self.assertIsInstance(self.maccabi.name, str)

    def test_get_team(self):
        """
        Test for get_team
        """
        testing_team = [self.center, self.point_guard, self.guard]
        lst_of_players = self.maccabi.get_team()
        # Testing it returned the correct list and all attributes are equal
        for i in range(0, len(lst_of_players)):
            self.assertEqual(lst_of_players[i].name, testing_team[i].name)
            self.assertEqual(lst_of_players[i].age, testing_team[i].age)
            self.assertEqual(lst_of_players[i].hand, testing_team[i].hand)
        # Testing objects are the same
        self.assertEqual(str(lst_of_players), str(testing_team))

    def test_score_team(self):
        """
        Test for score_team
        """
        self.assertEqual(self.maccabi.score_team(), 53)

    def test_has_dominoes_team(self):
        """
        Test for has_dominoes_team
        """
        self.assertTrue(self.maccabi.has_dominoes_team())
        empty_team = Team("empty", [])
        self.assertFalse(empty_team.has_dominoes_team())

    def test_play(self):
        """
        Test for play
        """
        b = Board(8)
        for i in range(0, 6):
            self.assertTrue(self.maccabi.play(b))
        # Testing it played the right moves
        self.assertEqual(str(b), "[6|6][6|6][6|2][2|4][4|3][3|5]")
        # No more moves
        self.assertFalse(self.maccabi.play(b))

    def test_str(self):
        """
        Test for str
        """
        correct_str = "Name Maccabi, Score team: 53, Players: Name: Reynolds, Age: 25, Hand: [6|6][6|6], Score: 24," \
                      " I can win the game! Name: Evans, Age: 25, Hand: [5|3][2|6], Score: 16 Name: Wilbekin, Age: " \
                      "25, Hand: [4|2][3|4], Score: 13"
        self.assertEqual(str(self.maccabi), correct_str)

    def test_repr(self):
        """
        Test for str
        """
        correct_str = "Name Maccabi, Score team: 53, Players: Name: Reynolds, Age: 25, Hand: [6|6][6|6], Score: 24," \
                      " I can win the game! Name: Evans, Age: 25, Hand: [5|3][2|6], Score: 16 Name: Wilbekin, Age: " \
                      "25, Hand: [4|2][3|4], Score: 13"
        self.assertEqual(repr(self.maccabi), correct_str)
