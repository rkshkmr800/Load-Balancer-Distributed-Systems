#test case for all nodes receiving variable loads at same rate

python2.7 client.py 103:8000 A4 &
R=$((10+$RANDOM%15))
echo "103:8000 A4:   4" &
sleep $R
python2.7 client.py 103:8000 A10 &
R=$((10+$RANDOM%15))
echo "103:8000 A10:   4" &
sleep $R
python2.7 client.py 103:8000 A16 &
R=$((10+$RANDOM%15))
echo "103:8000 A16:   4" &
sleep $R
python2.7 client.py 103:8000 A22 &
R=$((10+$RANDOM%15))
echo "103:8000 A22:   4"


