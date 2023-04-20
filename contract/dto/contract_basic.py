from pydantic import BaseModel
from web3.contract import Contract

from contract.dto.chain import Chain


class ContractBasicParams(BaseModel):
    """contract basic params"""
    protocol_name: str  # 用於區分不同的 protocol 的 contract
    chain: Chain  # web3.py 好像沒有 chain 的 class
    contract: Contract
