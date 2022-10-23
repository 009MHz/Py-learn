"""Concept: printing out the domino card"""
for left in range(7):  #karena domino cuman nyampe 6
    for right in range(left, 7):
        print(f"[{left}|{right}]", end=" ")
        # fungsi end= " "
        # Once print has taken the content we passed and written to the screen then
        # it writes a special characters that creates new line called "newline character"
    print()

"""example 1: Membuat bagan kompetisi sistim setengah kompetisi"""
print("\nexample 1: Membuat bagan kompetisi sistim setengah kompetisi")
teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(f"{home_team} vs {away_team}")