#test case for all nodes receiving variable loads at same rate

python2.7 client.py 102:10000 A25 &
R=$((10+$RANDOM%15))
echo "102:10000 A25:  1" &
sleep $R
python2.7 client.py 102:10000 A31 &
R=$((10+$RANDOM%15))
echo "102:10000 A31:  1" &
sleep $R
python2.7 client.py 102:10000 A37 &
R=$((10+$RANDOM%15))
echo "102:10000 A37:  1" &
sleep $R
python2.7 client.py 102:10000 A43 &
R=$((10+$RANDOM%15))
echo "102:10000 A43:  1"

