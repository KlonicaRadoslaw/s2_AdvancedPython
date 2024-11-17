from collections import defaultdict

def groupProducts(products):
    groupedProds = defaultdict(list)
    for prod in products:
        groupedProds[prod.name].append(prod)

    return groupedProds

def countGoodGrades(grades):
    goodGrades = 0
    for i in grades:
        if i >=3:
            goodGrades+=1

    return goodGrades