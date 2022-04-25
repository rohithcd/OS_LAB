#!/bin/bash

echo "Enter the number: "
read n
len=${#n}

cube=0
for ((i=0;$i<$len;i++))
do 

digit=${n:$i:1}

cube=`expr $cube + $digit \* $digit \* $digit`
done


if [ $n == $cube ]
then
echo "$n is armstrong no"
else
echo "$n is not armstrong no"
fi

