class ERC20:

    @staticmethod
    def balance_of(address: str) -> list:
        """get balance of token"""
        return ['balanceOf(address)(uint256)', address]
