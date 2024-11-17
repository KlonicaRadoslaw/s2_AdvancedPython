from collections import namedtuple, defaultdict, deque, Counter
from additionalFunctions import *
from Patient import Patient
from ProductDataClass import ProductDataClass
from datetime import time
import random

def exercise1():
    Product = namedtuple('Product',['name','price','weight'])

    products = [
        Product(name="product 1", price=1.5, weight=0.1),
        Product(name="product 2", price=2.2, weight=0.25),
        Product(name="product 3", price=3.3, weight=1.0),
        Product(name="product 4", price=4.4, weight=0.2)
    ]

    print("All products printed: ")
    for prod in products:
        print(prod)

    print("All products names printed: ")
    for prod in products:
        print(prod.name)

def exercise2():
    products = [
        ProductDataClass(name="product 1", price=1.5, weight=0.1),
        ProductDataClass(name="product 2", price=2.2, weight=0.25),
        ProductDataClass(name="product 3", price=3.3, weight=1.0),
        ProductDataClass(name="product 4", price=4.4, weight=0.2)
    ]

    print("All products printed from data class: ")
    for prod in products:
        print(prod)

    print("All products names printed from data class: ")
    for prod in products:
        print(prod.name)

def exercise3():
    Product = namedtuple('Product', ['name', 'price', 'weight'])

    products = [
        Product(name="product 1", price=1.5, weight=0.1),
        Product(name="product 2", price=2.2, weight=0.25),
        Product(name="product 3", price=3.3, weight=1.0),
        Product(name="product 1", price=4.4, weight=0.2),
        Product(name="product 2", price=1.5, weight=0.1),
        Product(name="product 3", price=2.2, weight=0.25),
        Product(name="product 1", price=3.3, weight=1.0),
        Product(name="product 2", price=1.5, weight=0.1),
        Product(name="product 3", price=2.2, weight=0.25),
        Product(name="product 1", price=3.3, weight=1.0)
    ]

    groupedProds = groupProducts(products)
    for name, group in groupedProds.items():
        print(f"{name}: {group}")

def exercise4():
    patients = [
        Patient(name="John", surname="Doe", age=30, disease="Flu", visit_time=time(9, 20)),
        Patient(name="Jane", surname="Amith", age=25, disease="Cold", visit_time=time(19, 00)),
        Patient(name="Bob", surname="Brown", age=40, disease="Headache", visit_time=time(9, 40)),
        Patient(name="Alice", surname="Johnson", age=35, disease="Fever", visit_time=time(10, 0)),
        Patient(name="Tom", surname="Williams", age=45, disease="Back pain", visit_time=time(10, 20)),
    ]

    sortedPatients = sorted(patients)
    pQueue = deque(sortedPatients)

    while pQueue:
        currPatient = pQueue.popleft()
        print(f"Now patient: {currPatient.surname} at {currPatient.visit_time}")

    if not pQueue:
        print("Queue is empty")


def exercise5():
    grades = []
    for _ in range(15):
        grades.append(random.randint(2,5))

    countedGrades = Counter(grades)

    twoMostCommonGrades = countedGrades.most_common(2)
    for grade, howMany in twoMostCommonGrades:
        print("Most common grade: ",grade)

    positiveGrades = countGoodGrades(grades)
    print("Count of positive grades: ", positiveGrades)

#exercise1()
#exercise2()
#exercise3()
#exercise4()
exercise5()