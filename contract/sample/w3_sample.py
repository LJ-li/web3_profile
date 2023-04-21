import os

from dotenv import load_dotenv
from web3 import Web3

load_dotenv()
infura_api_key = os.getenv('INFURA_API_KEY')
# w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{infura_api_key}'))
# w3 = Web3(Web3.HTTPProvider(f'https://arbitrum-mainnet.infura.io/v3/{infura_api_key}'))
w3 = Web3(Web3.HTTPProvider(f'https://avalanche-mainnet.infura.io/v3/{infura_api_key}'))
print(w3.is_connected())
