#test case for all nodes receiving variable loads at same rate

python2.7 client.py 102:8000 A26 &
R=$((10+$RANDOM%15))
echo "102:8000 A26:   2" &
sleep $R
python2.7 client.py 102:8000 A32 &
R=$((10+$RANDOM%15))
echo "102:8000 A32:   2" &
sleep $R
python2.7 client.py 102:8000 A38 &
R=$((10+$RANDOM%15))
echo "102:8000 A38:   2" &
sleep $R
python2.7 client.py 102:8000 A44 &
R=$((10+$RANDOM%15))
echo "102:8000 A44:   2"


