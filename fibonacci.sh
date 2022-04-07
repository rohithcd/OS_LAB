#!/bin/bash
echo "Enter the number of elements"
read n

first=0
second=1
i=2
echo "Fibonacci Series"
echo $first
echo $second

while [ $i -lt $n ]
do
sum=`expr $first + $second`
echo $sum
first=$second
second=$sum
i=`expr $i + 1`
done


