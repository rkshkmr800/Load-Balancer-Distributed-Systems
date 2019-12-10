#test case for all nodes receiving variable loads at same rate

python2.7 client.py 103:9000 A5 &
R=$((10+$RANDOM%15))
echo "103:9000 A5:   5" &
sleep $R
python2.7 client.py 103:9000 A11 &
R=$((10+$RANDOM%15))
echo "103:9000 A11:   5" &
sleep $R
python2.7 client.py 103:9000 A17 &
R=$((10+$RANDOM%15))
echo "103:9000 A17:   5" &
sleep $R
python2.7 client.py 103:9000 A23 &
R=$((10+$RANDOM%15))
echo "103:9000 A23:   5"


