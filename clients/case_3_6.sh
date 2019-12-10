#test case for all nodes receiving variable loads at same rate

python2.7 client.py 103:10000 A6 &
R=$((10+$RANDOM%15))
echo "103:10000 A6:   6" &
sleep $R
python2.7 client.py 103:10000 A12 &
R=$((10+$RANDOM%15))
echo "103:10000 A12:   6" &
sleep $R
python2.7 client.py 103:10000 A18 &
R=$((10+$RANDOM%15))
echo "103:10000 A18:   6" &
sleep $R
python2.7 client.py 103:10000 A24 &
R=$((10+$RANDOM%15))
echo "103:10000 A24:   6"


