#test case for all nodes receiving variable loads at same rate

python2.7 client.py 102:10000 A1 &
R=$((10+$RANDOM%15))
echo "102:10000 A1:  1" &
sleep $R
python2.7 client.py 102:10000 A7 &
R=$((10+$RANDOM%15))
echo "102:10000 A7:  1" &
sleep $R
python2.7 client.py 102:10000 A13 &
R=$((10+$RANDOM%15))
echo "102:10000 A13:  1" &
sleep $R
python2.7 client.py 102:10000 A19 &
R=$((10+$RANDOM%15))
echo "102:10000 A19:  1"

