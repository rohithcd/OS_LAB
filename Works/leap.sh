#!/bin/bash

echo "Enter the year"
read year

#if [ `expr $year % 400` == 0  -a `expr $year % 100` == 0 ]
if ((  $year % 400 == 0 & $year % 100 == 0 ))
then
echo "$year is leap year"
elif [ `expr $year % 4` == 0  -a `expr $year % 100` != 0 ]
then
echo "$year is leap year"
else
echo "$year is not a leap year"
fi
