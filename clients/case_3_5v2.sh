#test case for all nodes receiving variable loads at same rate

python2.7 client.py 103:9000 A29 &
R=$((10+$RANDOM%15))
echo "103:9000 A29:   5" &
sleep $R
python2.7 client.py 103:9000 A35 &
R=$((10+$RANDOM%15))
echo "103:9000 A35:   5" &
sleep $R
python2.7 client.py 103:9000 A41 &
R=$((10+$RANDOM%15))
echo "103:9000 A41:   5" &
sleep $R
python2.7 client.py 103:9000 A47 &
R=$((10+$RANDOM%15))
echo "103:9000 A47:   5"


