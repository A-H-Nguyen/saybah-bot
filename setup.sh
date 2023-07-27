# Create venv
python -m venv bot-env

# Create empty .env file -- need to manually put in bot token
touch .env

source activate

# Install requirements
pip install -r requirements.txt