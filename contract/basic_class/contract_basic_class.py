from contract.dto.contract_basic import ContractBasicParams


class ContractBasicClass(object):
    """contract basic class"""

    def __init__(self, contract: ContractBasicParams):
        self.contract = contract

    def get_contract(self):
        return self.contract

    def get_contract_address(self):
        return self.contract.address

    def get_contract_abi(self):
        return self.contract.abi

    def get_contract_bytecode(self):
        return self.contract.bytecode

    def get_contract_bytecode_runtime(self):
        return self.contract.bytecode_runtime
