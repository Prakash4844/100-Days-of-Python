from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon",["Pikachu","Charmander","Squirtle"])
table.add_column("Types",["Electric","Fire","Water"])
table.align = "l"

print(table)
