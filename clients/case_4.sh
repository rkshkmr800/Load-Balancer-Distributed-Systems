#test case for one node receiving all the variable load requests

python2.7 client.py 103:10000 A1 &
echo "6 - A1" &
sleep 7
python2.7 client.py 103:10000 A2 &
echo "6 -A2" &
sleep 7
python2.7 client.py 103:10000 A3 &
echo "6 - A3" &
sleep 7
python2.7 client.py 103:10000 A4 &
echo "6 - A4" &
sleep 7
python2.7 client.py 103:10000 A5 &
echo "6 - A5" &
sleep 7
python2.7 client.py 103:10000 A6 &
echo "6 - A6" &
sleep 7
python2.7 client.py 103:10000 A7 &
echo "6 - A7" &
sleep 7
python2.7 client.py 103:10000 A8 &
echo "6 - A8" &
sleep 7
python2.7 client.py 103:10000 A9 &
echo "6 - A9" &
sleep 7
python2.7 client.py 103:10000 A10 &
echo "6 - A10"

