from pydantic import BaseModel

from contract.dto.chain import Chain


class ContractBasicParams(BaseModel):
    """contract basic params"""
    address: str
    abi: dict
    bytecode: str
    bytecode_runtime: str
    protocol_name: str
    chain: Chain
