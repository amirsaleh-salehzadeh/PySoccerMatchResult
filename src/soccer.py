'''
Created on Jul 6, 2022

@author: AMIR
'''
from numpy.ma.testutils import assert_equal

teamsDic = {}


def getMatchRes(user_input):
    team1 = user_input.split(", ")[0].split(" ")
    team2 = user_input.split(", ")[1].split(" ")
    res1 = team1[len(team1) - 1]
    res2 = team2[len(team2) - 1]
    del team1[-1]
    del team2[-1]
    if int(res1) > int(res2):
        return " ".join(team1), 3, " ".join(team2), 0
    elif int(res1) == int(res2):
        return " ".join(team1), 1, " ".join(team2), 1
    else:
        return " ".join(team1), 0, " ".join(team2), 3


def getDataFromUser(user_input):
    team1, res1, team2, res2 = getMatchRes(user_input)
    if team1 in teamsDic.keys():
        teamsDic[team1] = res1 + teamsDic[team1]
    else:
        teamsDic[team1] = res1
    if team2 in teamsDic.keys():
        teamsDic[team2] = res2 + teamsDic[team2]
    else:
        teamsDic[team2] = res2
    return str(teamsDic)


def testCode():
    test_input = ["Lions 3, Snakes 3", "Tarantulas 1, FC Awesome 0",
                  "Lions 1, FC Awesome 1", "Tarantulas 3, Snakes 1", "Lions 4, Grouches 0"]
    assert_equal(getDataFromUser("Lions 3, Snakes 3"), "{'Lions': 1, 'Snakes': 1}", "Not matched")
    assert_equal(getDataFromUser("Tarantulas 1, FC Awesome 0"), "{'Lions': 1, 'Snakes': 1, 'Tarantulas': 3, 'FC Awesome': 0}", "Not matched")
    assert_equal(getDataFromUser("Lions 1, FC Awesome 1"), "{'Lions': 2, 'Snakes': 1, 'Tarantulas': 3, 'FC Awesome': 1}", "Not matched")
    assert_equal(getDataFromUser("Tarantulas 3, Snakes 1"), "{'Lions': 2, 'Snakes': 1, 'Tarantulas': 6, 'FC Awesome': 1}", "Not matched")
    assert_equal(getDataFromUser("Lions 4, Grouches 0"), "{'Lions': 5, 'Snakes': 1, 'Tarantulas': 6, 'FC Awesome': 1, 'Grouches': 0}", "Not matched")

    
if __name__ == '__main__':
    testCode()
    teamsDic = {}
    while True:
        user_input = input('Enter a match result ')
        if len(user_input) > 0:
            getDataFromUser(user_input)
        else:
            print('User pressed Enter')
            break
    print(teamsDic)
    # print(getDataFromUser())
