#!/bin/bash
echo "Enter "
read n
c=0
for((i=1;i<=n;i++))
do
if [ `expr $n % $i` -eq 0 ]
then
c=`expr $c + 1`
fi
done
if [ $c -eq 2 ]
then
echo "Prime"
else 
echo "No prime"
fi
