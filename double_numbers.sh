date
#for i in $(seq 1 1000000);
#do
    #echo $RANDOM >> file1.txt
#done
{
while read -r number
do
    let "number *= 2"
    echo $number
done < file1.txt
} >> newfile1.txt
date
date -ud "@$SECONDS" "+Time elapsed: %H:%M:%S"
