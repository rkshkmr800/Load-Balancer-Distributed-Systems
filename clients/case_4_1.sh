#test case for one node receiving all the variable load requests

python2.7 client.py 103:10000 A11 &
echo "6 - A11" &
sleep 7
python2.7 client.py 103:10000 A12 &
echo "6 -A12" &
sleep 7
python2.7 client.py 103:10000 A13 &
echo "6 - A13" &
sleep 7
python2.7 client.py 103:10000 A14 &
echo "6 - A14" &
sleep 7
python2.7 client.py 103:10000 A15 &
echo "6 - A15" &
sleep 7
python2.7 client.py 103:10000 A16 &
echo "6 - A16" &
sleep 7
python2.7 client.py 103:10000 A17 &
echo "6 - A17" &
sleep 7
python2.7 client.py 103:10000 A18 &
echo "6 - A18" &
sleep 7
python2.7 client.py 103:10000 A19 &
echo "6 - A19" &
sleep 7
python2.7 client.py 103:10000 A20 &
echo "6 - A20"

