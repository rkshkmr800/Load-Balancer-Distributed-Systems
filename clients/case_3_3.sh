#test case for all nodes receiving variable loads at same rate

python2.7 client.py 102:9000 A3 &
R=$((10+$RANDOM%15))
echo "102:9000 A3:   3" &
sleep $R
python2.7 client.py 102:9000 A9 &
R=$((10+$RANDOM%15))
echo "102:9000 A9:   3" &
sleep $R
python2.7 client.py 102:9000 A15 &
R=$((10+$RANDOM%15))
echo "102:9000 A15:   3" &
sleep $R
python2.7 client.py 102:9000 A21 &
R=$((10+$RANDOM%15))
echo "102:9000 A21:   3"

