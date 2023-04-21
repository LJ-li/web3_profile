class GMXReader:

    @staticmethod
    def getVestingInfoV2(account: str, vesters: list[str]) -> list:
        """get balance of token"""
        return ['getVestingInfoV2(address,address[])(uint256[])', address]

    @staticmethod
    def getTokenSupply():
        pass

    @staticmethod
    def getTotalBalance(token: str, accounts: list[str]) -> list:
        """get balance of token"""
        return ['getTotalBalance(address,address[])(uint256)', token, accounts]
