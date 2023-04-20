from pydantic import BaseModel


class Chain(BaseModel):
    chain_id: int
    chain_name: str
    chain_type: str
    rpc_url: str  # 也可以用 list 或是 dict 來確保一條 chain 有多個 rpc_url
