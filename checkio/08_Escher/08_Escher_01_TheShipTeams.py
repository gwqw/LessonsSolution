"""
    Split saylors on two teams: one: age > 40 and age < 20, two: 20 <= age <= 40
    and sort them alphabetically
    input: {name1:age1, ...}
    output: [[names], [names]]
    1 <= sailors <= 100
"""

def two_teams(sailors):
    team1 = []
    team2 = []
    for name, age in sailors.items():
        if age > 40 or age < 20:
            team1.append(name)
        else:
            team2.append(name)
    team1.sort()
    team2.sort()        
    return [team1, team2]

if __name__ == '__main__':
    print("Example:")
    print(two_teams({'Smith': 34, 'Wesson': 22, 'Coleman': 45, 'Abrahams': 19}))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert two_teams({
        'Smith': 34, 
        'Wesson': 22, 
        'Coleman': 45, 
        'Abrahams': 19}) == [
            ['Abrahams', 'Coleman'], 
            ['Smith', 'Wesson']
            ]

    assert two_teams({
        'Fernandes': 18,
        'Johnson': 22,
        'Kale': 41,
        'McCortney': 54}) == [
            ['Fernandes', 'Kale', 'McCortney'], 
            ['Johnson']
            ]
    print("Coding complete? Click 'Check' to earn cool rewards!")
