#test case for one node receiving all the load requests

python2.7 client_fix_loads.py 102:10000 A1 &
echo "101 - A1" &
sleep 12
python2.7 client_fix_loads.py 102:10000 A2 &
echo "101 -A2" &
sleep 12
python2.7 client_fix_loads.py 102:10000 A3 &
echo "101 - A3" &
sleep 12
python2.7 client_fix_loads.py 102:10000 A4 &
echo "101 - A4" &
sleep 12
python2.7 client_fix_loads.py 102:10000 A5 &
echo "101 - A5" &
sleep 12
python2.7 client_fix_loads.py 102:10000 A6 &
echo "101 - A6" &
sleep 12
python2.7 client_fix_loads.py 102:10000 A7 &
echo "101 - A7" &
sleep 12
python2.7 client_fix_loads.py 102:10000 A8 &
echo "101 - A8" 
sleep 12
python2.7 client_fix_loads.py 102:10000 A7 &
echo "101 - A9" &
sleep 12
python2.7 client_fix_loads.py 102:10000 A8 &
echo "101 - A10" 
