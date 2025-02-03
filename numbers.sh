date
# This simple echo method take 59 econds.
#for i in $(seq 1 1000000);
#do
    #echo $RANDOM >> file1.txt
#done

# This method of redirecting a buffer or a lerger block takes 9 seconds
#{
#for i in $(seq 1 1000000);
#do
    #echo $RANDOM 
#done
#} >> file1.txt

# This method of using awk and also redirecting a buffer takes 1 second.
awk 'BEGIN{srand(); for(i=1; i<=1000000; i++) print int(rand()*1000000)}' >> file1.txt

date
date -ud "@$SECONDS" "+Time elapsed: %H:%M:%S"
