import os

from dotenv import load_dotenv
from multicall import Call, Multicall
from web3 import Web3

# assuming you are on kovan
MKR_TOKEN = '0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2'
MKR_WHALE = '0x9a3f63F053512597d486cA679Ce5A0D13b98C8db'


def from_wei(value):
    return value


load_dotenv()
infura_api_key = os.getenv('INFURA_API_KEY')

w3 = Web3(
    provider=Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{infura_api_key}')
)
print(w3.eth.chain_id)
multi = Multicall(
    calls=[
        Call(target=MKR_TOKEN, function=['balanceOf(address)(uint256)', MKR_WHALE], returns=[('whale', from_wei)]),
        Call(target=MKR_TOKEN, function=['balanceOf(address)(uint256)', MKR_WHALE], returns=[('fish', from_wei)]),
    ],
    _w3=w3,
)

print(multi())  # {'whale': 566437.0921992733, 'fish': 7005.0, 'supply': 1000003.1220798912}
