#!/bin/bash

###########################################################
#####################   HELP     ##########################
###########################################################

while getopts ":h" options;
do 
case $options in
h) #help 
    echo "Usage: wiki search_key ";
    exit;;
esac
done

###########################################################
###################   Main Program   ######################
###########################################################

s_key=$1;
search_key="${s_key// /_}";
#search_key="${s_key// /_}";
#echo $search_key;
search_url="https://en.wikipedia.org/wiki/Special:Search?search="$search_key;
curl -L -# -o /dev/null --write-out %{url_effective} $search_url| tee -a log.txt;
echo "" | cat >> log.txt;
echo "";

