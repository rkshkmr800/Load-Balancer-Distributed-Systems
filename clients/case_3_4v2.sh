#test case for all nodes receiving variable loads at same rate

python2.7 client.py 103:8000 A28 &
R=$((10+$RANDOM%15))
echo "103:8000 28:   4" &
sleep $R
python2.7 client.py 103:8000 A34 &
R=$((10+$RANDOM%15))
echo "103:8000 A34:   4" &
sleep $R
python2.7 client.py 103:8000 A40 &
R=$((10+$RANDOM%15))
echo "103:8000 A40:   4" &
sleep $R
python2.7 client.py 103:8000 A46 &
R=$((10+$RANDOM%15))
echo "103:8000 A46:   4"


