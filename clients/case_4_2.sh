#test case for one node receiving all the variable load requests

python2.7 client.py 103:10000 A21 &
echo "6 - A21" &
sleep 7
python2.7 client.py 103:10000 A22 &
echo "6 -A22" &
sleep 7
python2.7 client.py 103:10000 A23 &
echo "6 - A23" &
sleep 7
python2.7 client.py 103:10000 A24 &
echo "6 - A24" &
sleep 7
python2.7 client.py 103:10000 A25 &
echo "6 - A25" &
sleep 7
python2.7 client.py 103:10000 A26 &
echo "6 - A26" &
sleep 7
python2.7 client.py 103:10000 A27 &
echo "6 - A27" &
sleep 7
python2.7 client.py 103:10000 A28 &
echo "6 - A28" &
sleep 7
python2.7 client.py 103:10000 A29 &
echo "6 - A29" &
sleep 7
python2.7 client.py 103:10000 A30 &
echo "6 - A30"

