# Sleep 10 seconds while mongodb server spins up
echo "Waiting for mongo..."
sleep 10
echo "Starting app now"
python app.py
