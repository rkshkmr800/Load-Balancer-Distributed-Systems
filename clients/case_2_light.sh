#test case for one node receiving all the load requests

python2.7 client_light_static.py 101:8000 A1 &
echo "101 - A1" &
sleep 5
python2.7 client_light_static.py 101:8000 A2 &
echo "101 -A2" &
sleep 5
python2.7 client_light_static.py 101:8000 A3 &
echo "101 - A3" &
sleep 5
python2.7 client_light_static.py 101:8000 A4 &
echo "101 - A4" &
sleep 5
python2.7 client_light_static.py 101:8000 A5 &
echo "101 - A5" &
sleep 5
python2.7 client_light_static.py 101:8000 A6 &
echo "101 - A6" &
sleep 5
python2.7 client_light_static.py 101:8000 A7 &
echo "101 - A7" &
sleep 5
python2.7 client_light_static.py 101:8000 A8 &
echo "101 - A8" &
sleep 5
python2.7 client_light_static.py 101:8000 A9 &
echo "101 - A9" &
sleep 5
python2.7 client_light_static.py 101:8000 A10 &
echo "101 - A10"

