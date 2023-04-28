from unittest import TestCase, main

from project.team import Team


class Test(TestCase):
    def test_team_init(self):
        team_name = 'Team'
        team = Team(team_name)
        self.assertEqual(team_name, team.name)
        self.assertEqual({}, team.members)

    def test_name_if_contains_only_letters(self):
        with self.assertRaises(ValueError) as context:
            team = Team("dsf43@@")
        self.assertEqual('Team Name can contain only letters!', str(context.exception))

    def test_add_member_only_new_members(self):
        team_name = 'Team'
        team = Team(team_name)
        team.members["ivan"] = 18

        result = team.add_member(ivan=18, pesho=12, gosho=32, ivo=17)

        self.assertEqual("Successfully added: pesho, gosho, ivo", result)
        self.assertEqual(18, team.members['ivan'])
        self.assertEqual(12, team.members['pesho'])
        self.assertEqual(32, team.members['gosho'])
        self.assertEqual(17, team.members['ivo'])

    def test_remove_member_from_team(self):
        team_name = 'Team'
        team = Team(team_name)
        team.members["ivan"] = 18
        team.members["gosho"] = 32

        result = team.remove_member("ivan")
        self.assertEqual("Member ivan removed", result)

    def test_remove_member_from_team_when_name_not_exist(self):
        team_name = 'Team'
        team = Team(team_name)
        team.members["ivan"] = 18
        team.members["gosho"] = 32

        result = team.remove_member("dido")
        self.assertEqual("Member with name dido does not exist", result)
        self.assertEqual(18, team.members["ivan"])
        self.assertTrue(result not in team.members)

    def test_return_true_if_team1_greater_team2(self):
        team_name1 = 'Teamone'
        team1 = Team(team_name1)
        team1.members["ivan"] = 18
        team1.members["gosho"] = 32
        team1.members["dido"] = 19
        team_name2 = 'Teamtwo'
        team2 = Team(team_name2)
        team2.members["ivan1"] = 18
        team2.members["gosho1"] = 32

        self.assertTrue(len(team1.members) > len(team2.members))

    def test_return_false_if_team1_equal_team2(self):
        team_name1 = 'Teamone'
        team1 = Team(team_name1)

        team1.members["gosho"] = 32
        team1.members["dido"] = 19
        team_name2 = 'Teamtwo'
        team2 = Team(team_name2)
        team2.members["ivan1"] = 18
        team2.members["gosho1"] = 32

        self.assertFalse(len(team1.members) > len(team2.members))

    def test_return_false_if_team1_smaller_team2(self):
        team_name1 = 'Teamone'
        team1 = Team(team_name1)

        team1.members["dido"] = 19
        team_name2 = 'Teamtwo'
        team2 = Team(team_name2)
        team2.members["ivan1"] = 18
        team2.members["gosho1"] = 32

        self.assertFalse(len(team1.members) > len(team2.members))

    def test_return_len_team(self):
        team_name1 = 'Teamone'
        team1 = Team(team_name1)
        team1.members["ivan"] = 18
        team1.members["gosho"] = 32
        team1.members["dido"] = 19

        self.assertEqual(3, len(team1.members))

    def test_return_combined_teams_in_new_team(self):
        team_name1 = 'Teamone'
        team1 = Team(team_name1)
        team1.members["ivan"] = 18
        team1.members["gosho"] = 32
        team1.members["dido"] = 19
        team2 = 'Teamtwo'
        team2 = Team(team2)
        team2.members["ivan1"] = 18
        team2.members["gosho1"] = 31
        new_team = team1 + team2
        expexted_members = {
            "ivan": 18,
            "gosho": 32,
            "dido": 19,
            "ivan1": 18,
            "gosho1": 31,
        }

        self.assertEqual(expexted_members, new_team.members)
        self.assertEqual("TeamoneTeamtwo", new_team.name)

    def test_return_string_team(self):
        team1 = 'Teamone'
        team1 = Team(team1)
        team1.members["dido"] = 19
        team2 = 'Teamtwo'
        team2 = Team(team2)
        team2.members["ivan"] = 18
        team2.members["gosho"] = 31
        new_team = team1 + team2
        result = str(new_team)
        expected = "Team name: TeamoneTeamtwo" + '\n' + "Member: gosho - 31-years old" + '\n' + \
                 "Member: dido - 19-years old" + '\n' + 'Member: ivan - 18-years old'
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
