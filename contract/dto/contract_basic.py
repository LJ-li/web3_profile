from pydantic import BaseModel
from web3.contract import Contract

from contract.dto.chain import Chain


class ContractBasicParams(BaseModel):
    """contract basic params"""
    protocol_name: str  # 用於區分不同的 protocol 的 contract
    chain: Chain  # web3.py 好像沒有 chain 的 class
    contract: Contract
    metadata: dict  # 用於存放 contract 的 metadata，例如 pool_name 等等


c_1 = ContractBasicParams(
    protocol_name='xrex',
    chain=Chain(
        chain_id=1,
        chain_name='mainnet',
        chain_type='EVM',
        rpc_url='https://mainnet.infura.io/v3/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    ),
    contract=Contract,
    metadata={
        'pool_name': 'xrex',
    },
)
