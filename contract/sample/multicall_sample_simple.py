import os

from dotenv import load_dotenv
from multicall import Call, Multicall
from web3 import Web3

# 這邊可以用成 enum
MKR_TOKEN = '0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2'
MKR_WHALE = '0x40f2ec751f922db371b2404049a40d1d5de57ab0'
MKR_FISH = '0x96294a10222d69d29ca047c0e9e5e707d1d5a2d6'


def from_wei(value: int) -> float | None:
    if value is None:
        return None
    return value / 1e18


load_dotenv()
infura_api_key = os.getenv('INFURA_API_KEY')

w3 = Web3(
    provider=Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{infura_api_key}')
)
print(w3.eth.chain_id)
multi = Multicall(
    calls=[
        Call(target=MKR_TOKEN, function=['balanceOf(address)(uint256)', MKR_WHALE], returns=[('whale', from_wei)]),
        Call(target=MKR_TOKEN, function=['balanceOf(address)(uint256)', MKR_FISH], returns=[('fish', from_wei)]),
    ],
    _w3=w3,
)
result = multi()
print()  # {'whale': 566437.0921992733, 'fish': 7005.0, 'supply': 1000003.1220798912}
