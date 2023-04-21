import os

from dotenv import load_dotenv
from multicall import Call, Multicall
from web3 import Web3

from contract.contract.gmx_reader import GMXReader

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

arb = Web3(
    provider=Web3.HTTPProvider(f'https://arbitrum-mainnet.infura.io/v3/{infura_api_key}')
)
eth = Web3(
    provider=Web3.HTTPProvider(f'https://arbitrum-mainnet.infura.io/v3/{infura_api_key}')
)
print(arb.eth.chain_id)
multi = Multicall(
    calls=[
        Call(target=MKR_TOKEN, function=GMXReader.getTotalBalance(
            token='0xfc5A1A6EB076a2C7aD06eD22C90d7E710E35ad0a',
            accounts=[
                '0xfcb2a5CbF9EC079CD3f7C32F43C385F3A6d8FF04']
        ),
             returns=[('ray', from_wei)]),

    ],
    _w3=arb,
)
result = multi()
print(result)
