#distionary
mydisc ={
   "mona":"beautiful",
   "shakshi":"pretty",
   "MyList":[12,13,24,45],
   "MonaLisa":{ "Fruit":"Mango",
   "colour":"pink"}   
}
# print(mydisc['mona'])
# print(mydisc['shakshi'])
# print(mydisc['MonaLisa']['Fruit'])
print(list(mydisc.keys()))
print(list(mydisc.values()))
print(list(mydisc.items()))
monagupta={
    "misba":"friend",
    "mona":"slim"
}
mydisc.update(monagupta)
print(mydisc)

#consept
print(mydisc.get("mona"))
print(mydisc['mona'])

#differnce
print(mydisc.get("mona1"))
print(mydisc['mona1'])

