#test case for equal load at equal rate to all the nodes

python2.7 client_light_static.py 101:8000 A1 &
python2.7 client_light_static.py 102:8000 A2 &
python2.7 client_light_static.py 102:9000 A3 &
python2.7 client_light_static.py 103:8000 A4 &
python2.7 client_light_static.py 103:9000 A5 &
python2.7 client_light_static.py 103:10000 A6 &
echo "101:8000 - A1, 102:8000 - A2, 102:9000 - A3, 103:8000 - A4, 103:9000 - A5, 103:10000 - A6" &
sleep 5
python2.7 client_light_static.py 101:8000 A7 &
python2.7 client_light_static.py 102:8000 A8 &
python2.7 client_light_static.py 102:9000 A9 &
python2.7 client_light_static.py 103:8000 A10 &
python2.7 client_light_static.py 103:9000 A11 &
python2.7 client_light_static.py 103:10000 A12 &
echo "101:8000 - A7, 102:8000 - A8, 102:9000 - A9, 103:8000 - A10, 103:9000 - A11, 103:10000 - A12" &
sleep 5
python2.7 client_light_static.py 101:8000 A13 &
python2.7 client_light_static.py 102:8000 A14 &
python2.7 client_light_static.py 102:9000 A15 &
python2.7 client_light_static.py 103:8000 A16 &
python2.7 client_light_static.py 103:9000 A17 &
python2.7 client_light_static.py 103:10000 A18 &
echo "101:8000 - A13, 102:8000 - A14, 102:9000 - A15, 103:8000 - A16, 103:9000 - A17, 103:10000 - A18" &
sleep 5
python2.7 client_light_static.py 101:8000 A19 &
python2.7 client_light_static.py 102:8000 A20 &
python2.7 client_light_static.py 102:9000 A21 &
python2.7 client_light_static.py 103:8000 A22 &
python2.7 client_light_static.py 103:9000 A23 &
python2.7 client_light_static.py 103:10000 A24 &
echo "101:8000 - A19, 102:8000 - A20, 102:9000 - A21, 103:8000 - A22, 103:9000 - A23, 103:10000 - A24"

