# asdecaldas_validar_manilla

for i in {1..2000}
openssl rand -hex 10 >> asistentes.txt
awk {'print NR";"$1'} asistentes.txt > asistentes2.txt
awk -F";" {'print "/usr/local/bin/qrencode -s 6 -l H -o "$1".png https://juanse.com/"$2'} asistentes2.txt | sh
awk -F";" {'print "insert into punto1_caballista values("$1",'\''"$2"'\'',0,0);"'} asistentes2.txt > caballistas.sql

