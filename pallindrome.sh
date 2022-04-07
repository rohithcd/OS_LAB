#!/bin/bash
echo "----Pallindrome Checking Program----"
echo "Enter the String"
read string
len=${#string}

for((i=$len-1;i>=0;i--))
do
rev=$rev${string:$i:1}
done

if [ $string == $rev ]
then
echo "$rev is pallindrome"
else
echo "$string is not a pallindrome"
fi
