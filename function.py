def percent(marks):
    p=(sum(marks)/500)*100
    return p
s1=int(input(" Enter The Marsks In Sub1 :"))
s2=int(input(" Enter The Marsks In Sub2 :"))
s3=int(input(" Enter The Marsks In Sub3 :"))
s4=int(input(" Enter The Marsks In Sub4 :"))
s5=int(input(" Enter The Marsks In Sub5 :"))
marks=[s1,s2,s3,s4,s5]
per1=percent(marks)
print("\n\n Percentage of A Student is : ",per1)

