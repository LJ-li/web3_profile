from pydantic import BaseModel


class GmxProtocolAddresses(BaseModel):
    gmx: str
    vault: str
    router: str
    position_router: str
    order_book: str
    reader: str
    reward_reader: str
    order_book_reader: str
    staked_gmx: str
    staked_glp: str
    glp_manager: str
    reward_router: str
    glp_reward_router: str
    referral_storage: str
    dex_pool: str  # biggest dex pool
