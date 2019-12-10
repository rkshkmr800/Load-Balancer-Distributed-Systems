#test case for all nodes receiving variable loads at same rate

python2.7 client.py 102:9000 A27 &
R=$((10+$RANDOM%15))
echo "102:9000 A27:   3" &
sleep $R
python2.7 client.py 102:9000 A33 &
R=$((10+$RANDOM%15))
echo "102:9000 A33:   3" &
sleep $R
python2.7 client.py 102:9000 A39 &
R=$((10+$RANDOM%15))
echo "102:9000 A39:   3" &
sleep $R
python2.7 client.py 102:9000 A45 &
R=$((10+$RANDOM%15))
echo "102:9000 A45:   3"

