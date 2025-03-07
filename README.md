# DailyHoroscope

Learning Twilio API, virtual env, and Python

Requirements:

# Need .env with your TWILIO_ACCOUNT_SID & TWILIO_AUTH_TOKEN formatted like this:
TWILIO_ACCOUNT_SID=123ABC
TWILIO_AUTH_TOKEN=123ABC

# Create virtual environment
python3 -m venv venv

# Activate it (Mac/Linux)
source venv/bin/activate

# Or on Windows
venv\Scripts\activate

# Install req
bin/pip3 install -r requirements.txt
pip3 install pyaztro
pip3 install python-dotenv

# Windows
pip install --upgrade certifi requests twilio
