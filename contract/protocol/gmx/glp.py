from pydantic import BaseModel

from contract.basic_class.contract_basic_class import ContractBasicClass


class GlpContractAddressModel(BaseModel):
    vault: ContractBasicClass
    reward_reader: str
    reader: str
    staked_gmx_tracker: str
    fee_gmx_tracker: str
    fee_lp_tracker: str
    staked_glp_tracker: str
    glp_manager: str
