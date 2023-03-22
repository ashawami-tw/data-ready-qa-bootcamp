from faker import Faker
import sys
from random import randint
from random import uniform

def create_new_player_record():
    # Create a new player record and return a list
    id = faker.uuid4()
    name = faker.name_male()
    team = teams[randint(0, len(teams)-1)]
    game_year = year
    game_week = week
    country = faker.country()
    na = 'null'
    position = positions[randint(0, len(positions)-1)]
    if position == 'QB':
        pass_att = randint(0, 600)
        pass_yds = randint(0, 40)
        interceptions = randint(0, 40)
        pass_tds = randint(0, 40)
        sacks = randint(0, 10)
        pass_fumbles = randint(0, 10)
        rate = float("{0:.2f}".format(uniform(0, 100)))
        return [id, name, team, country, game_year, game_week, na, na, na, na, na, na, na, na, na, na, pass_att,pass_yds,pass_tds, interceptions, sacks, pass_fumbles, rate, position]

    else:
        rush_att = randint(0, 100)
        rush_yds = randint(0, 100)
        rush_avg = float("{0:.2f}".format(uniform(0, 100)))
        rush_tds = randint(0, 100)
        rush_fumbles = randint(0, 100)
        rec = randint(0, 20)
        rec_yds = randint(0, 20)
        rec_avg = float("{0:.2f}".format(uniform(0, 100)))
        rec_tds = randint(0, 20)
        rec_fumbles = randint(0, 20)

        return [id, name, team,country, game_year, game_week, rush_att, rush_yds, rush_avg, rush_tds, rush_fumbles, rec, rec_yds, rec_avg, rec_tds, rec_fumbles, na, na, na, na, na, na, na, position]


if len(sys.argv) > 2:
    print('Cannot have more than one argument\nUsage: file.py <num_records>')
    sys.exit(1)

num_players_needed = int(sys.argv[1])
faker = Faker()
teams = []
positions = []
header = '"id","name","team", "country", "game_year","game_week","rush_att","rush_yds","rush_avg","rush_tds","rush_fumbles","rec","rec_yds","rec_avg","rec_tds","rec_fumbles","pass_att","pass_yds","pass_tds","int","sck","pass_fumbles","rate","position"'

with open('positions') as fp:
    for line in fp:
        positions.append(line.strip())

with open('teams') as fp:
    for line in fp:
        teams.append(line.strip())

year = 2018
week = 1
players = []
for i in range(num_players_needed):
    players.append(','.join(map(str, create_new_player_record())))


with open('players_out.csv', 'w') as fp:
    fp.write(header + '\n')
    fp.write('\n'.join(players))

