#!/bin/bash

while true; do

Principal() {
clear
#
echo " Script para 'DES'inverter url " 
echo " ============================= " 
echo "" 
echo " 1 - base64 " 
echo " 2 - invertida " 
echo " 3 - Sair " 
echo -n " Selecione a opcao desejada: " 
read opcao
case $opcao in
        1) base64
           echo "";;
        2) invertida
           echo "";;
        3) clear
           exit
           echo "";;
        *) Principal
           echo "";;
esac
}


pause(){
   read -p "$*"
}


base64() {
echo " Decode base64"
read url 
bs=$(echo $url | /usr/bin/base64 -d)
echo ""
echo "A url solicita e: " $bs
echo ""
pause 'Aperte enter para continuar.'
Principal
}

invertida() {
echo " Inverter url"
read url
echo ""
bs=$(echo $url | rev)
echo ""
echo "A url solicita e: " $bs
echo ""
pause 'Aperte enter para continuar.'
Principal
}
Principal
done
