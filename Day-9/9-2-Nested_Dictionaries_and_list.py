# Nesting List and Dict in Dict
travel_log = {
    "France": {
        "Cities_Visited": ['Paris', 'Lille', 'Dijon'],
    },

    "Germany": ["Berlin", "Hamburg", "Stuttgart"],

    "India": {
        "Cities_Visited": ['Ghaziabad', 'Noida', 'Delhi'],
        "Total_Visits": "uncountable",
    },
}

# Nesting Dict and list in List

travel_log1 = [
    {
        "Countries": "France",
        "Cities_Visited": ['Paris', 'Lille', 'Dijon'],
    },

    {
        "Countries": "India",
        "Cities_Visited": ['Ghaziabad', 'Noida', 'Delhi'],
        "Total_Visits": "uncountable",
    },
]
