date
#for i in $(seq 1 1000000);
#do
    #echo $RANDOM >> file1.txt
#done
# Use buferring by redirecting output of  larger block to reduce the execution time.
{
for i in $(seq 1 1000000);
do
    echo $RANDOM 
done
} >> file1.txt
date
date -ud "@$SECONDS" "+Time elapsed: %H:%M:%S"
