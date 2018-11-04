#!/usr/bin/env python3
# Copyright (c) 2008-9 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

numbers = []
total = 0
lowest = None
highest = None
median = None

while True:
    try:
        line = input("zadejte číslo nebo Enter pro ukončení: ")
        if not line:
            break
        number = int(line)
        numbers.append(number)
        total += number
        if lowest is None or lowest > number:
            lowest = number
        if highest is None or highest < number:
            highest = number
    except ValueError as err:
        print(err)

for y in range(len(numbers)):
    for x in range(len(numbers)):
        if x == (len(numbers)-1):
            pass#ToDo
        elif numbers[x] > numbers[x+1]:
            tmp = numbers[x+1]
            numbers[x+1] = numbers[x]
            numbers[x]=tmp
if(len(numbers)%2 != 0):
    index = (len(numbers)//2)
    median= numbers[index]
    
else:
    prvek1i = (len(numbers)//2)-1
    prvek2i = prvek1i+1
    median = (numbers[prvek1i]+numbers[prvek2i])/2
        
  

print("čísla:", numbers)
print("počet =", len(numbers), "součet =", total,
      "nejmenší =", lowest, "největší =", highest,
      "průměr =", total / len(numbers), "medián =", median)
