#test case for all nodes receiving variable loads at same rate

python2.7 client.py 102:8000 A2 &
R=$((10+$RANDOM%15))
echo "102:8000 A2:   2" &
sleep $R
python2.7 client.py 102:8000 A8 &
R=$((10+$RANDOM%15))
echo "102:8000 A8:   2" &
sleep $R
python2.7 client.py 102:8000 A14 &
R=$((10+$RANDOM%15))
echo "102:8000 A14:   2" &
sleep $R
python2.7 client.py 102:8000 A20 &
R=$((10+$RANDOM%15))
echo "102:8000 A20:   2"


