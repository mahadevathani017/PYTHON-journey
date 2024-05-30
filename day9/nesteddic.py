#nesting

capitals={
    "france":'Paris',
    "germany":"Berlin",
}

travel_log={
    "France":{"cities_visit":["Paris","Lille","Dijon"]},
    "Germany":["Berlin","Hamburg","Stutgart"]
}
# print(travel_log)
# print(type(travel_log["France"]))

travel_log=[
    {
        "Country":"France",
        "Cities_visited":["Paris","Lille","Dijion"],
        "total_visits":12
    },
    {
        "Country":"Germany",
        "cities_visited":["Berlin","Hamburg","Stuttgart"],
        "total_visits":5
    }
]

print(travel_log)
print(type(travel_log))
