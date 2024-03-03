from flask import Flask, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

def get_current_time_in_toronto():
    # Get the current UTC time
    utc_time = datetime.utcnow()

    # Toronto timezone offset (Eastern Time Zone)
    toronto_offset = timedelta(hours=-5)  # UTC-5

    # Calculate the current time in Toronto
    toronto_time = utc_time + toronto_offset

    return toronto_time.strftime("%Y-%m-%d %H:%M:%S")

@app.route('/get_current_time')
def get_time():
    toronto_time = get_current_time_in_toronto()
    return jsonify({'TorontoTime': toronto_time})

if __name__ == '__main__':
    app.run(debug=True)

