# 5.2 Sports Team Analyzer (Sets)

football = {"Amit", "Sagar", "Pooja", "Rahul"}
cricket = {"Rahul", "Anjali", "Sagar", "Kiran"}

print("Football Team:", football)
print("Cricket Team:", cricket)

both = football.intersection(cricket)
print("\nPlaying both sports:", both)

only_one = football.symmetric_difference(cricket)
print("Playing only one sport:", only_one)

total_unique = football.union(cricket)
print("Total unique players:", len(total_unique))
