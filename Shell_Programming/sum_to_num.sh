#!/bin/sh

echo "Enter the number"
read n
sum=0
i=0
while [ $i -le $n ]
do
sum=`expr $sum + $i`
i=`expr $i + 1` 
done
echo "Sum of $n numbers is $sum"
