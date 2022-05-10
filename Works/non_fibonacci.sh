#!/bin/bash


echo "Enter the value of n:"
read n

first=3
sec=5
count=0
total=0

echo "The nonfibunocci series is:"
while [ $count -lt $n ]
do


for ((i=`expr $first + 1`;$i<$sec;i++))
do

if [ $count -lt $n ]
then

echo $i
fi

count=`expr $count + 1`

done


total=`expr $first + $sec`
first=$sec
sec=$total


done


