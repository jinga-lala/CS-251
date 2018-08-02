#! /bin/bash

randchar1=`head /dev/urandom | tr -dc A-Z | head -c 1`
randchar2=`head /dev/urandom | tr -dc A-Z | head -c 1`
randnum=`head /dev/urandom | tr -dc 0-9 | head -c 1`
string="$randchar1$randchar2$randnum"
echo $string

sed -i "s#[A-Z][A-Z][0-9]#$string#g" $1
