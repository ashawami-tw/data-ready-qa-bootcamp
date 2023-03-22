import sys
if len(sys.argv) > 2:
    print('Cannot have more than one argument\nUsage: remove_players_with_no_team.py <file_name>')
    sys.exit(1)

filename = sys.argv[1]

team_col = 2
num_invalid = 0
valid_lines = []

for line in open(filename):
    info = line.split(',')
    if info[2] == '""':
        num_invalid += 1
    else:
        valid_lines.append(line)
fileout = filename + '_teams.csv'

print(str(num_invalid) + ' records found. Removing...')

with open(fileout, 'w') as fp:
    fp.write(''.join(valid_lines))
