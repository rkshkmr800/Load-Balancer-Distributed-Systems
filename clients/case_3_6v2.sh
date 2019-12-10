#test case for all nodes receiving variable loads at same rate

python2.7 client.py 103:10000 A30 &
R=$((10+$RANDOM%15))
echo "103:10000 30:   6" &
sleep $R
python2.7 client.py 103:10000 A36 &
R=$((10+$RANDOM%15))
echo "103:10000 A36:   6" &
sleep $R
python2.7 client.py 103:10000 A42 &
R=$((10+$RANDOM%15))
echo "103:10000 A42:   6" &
sleep $R
python2.7 client.py 103:10000 A48 &
R=$((10+$RANDOM%15))
echo "103:10000 A48:   6"


