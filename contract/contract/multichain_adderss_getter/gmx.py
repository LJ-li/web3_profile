from contract.dto.protocol_address.gmx import GmxProtocolAddresses
from contract.enum.chain_id_enum import ChainIdEnum


class GMXMultichainAddressGetter:

    @staticmethod
    def get_chain(chain: ChainIdEnum.ARBITRUM | ChainIdEnum.AVALANCHE) -> str:
        arbitrum_gmx_protocol_addresses = GmxProtocolAddresses(
            gmx="0xfc5A1A6EB076a2C7aD06eD22C90d7E710E35ad0a",
            vault="0x489ee077994B6658eAfA855C308275EAd8097C4A",
            router="0xaBBc5F99639c9B6bCb58544ddf04EFA6802F4064",
            position_router="0xb87a436B93fFE9D75c5cFA7bAcFff96430b09868",
            order_book="0x09f77e8a13de9a35a7231028187e9fd5db8a2acb",
            reader="0x22199a49A999c351eF7927602CFB187ec3cae489",
            reward_reader="0x8BFb8e82Ee4569aee78D03235ff465Bd436D40E0",
            order_book_reader="0xa27C20A7CF0e1C68C0460706bB674f98F362Bc21",
            staked_gmx="0xd2D1162512F927a7e282Ef43a362659E4F2a728F",
            staked_glp="0x5402B5F40310bDED796c7D0F3FF6683f5C0cFfdf",
            glp_manager="0x3963FfC9dff443c2A94f21b129D429891E32ec18",
            reward_router="0xA906F338CB21815cBc4Bc87ace9e68c87eF8d8F1",
            glp_reward_router="0xB95DB5B167D75e6d04227CfFFA61069348d271F5",
            referral_storage="0xe6fab3F0c7199b0d34d7FbE83394fc0e0D06e99d",
            dex_pool="0x80A9ae39310abf666A87C743d6ebBD0E8C42158E",  # uniswap_pool
        )
        avalanche_gmx_protocol_addresses = GmxProtocolAddresses(
            gmx="0x62edc0692BD897D2295872a9FFCac5425011c661",
            vault="0x9ab2De34A33fB459b538c43f251eB825645e8595",
            router="0x5F719c2F1095F7B9fc68a68e35B51194f4b6abe8",
            position_router="0xffF6D276Bc37c61A23f06410Dce4A400f66420f8",
            order_book="0x4296e307f108B2f583FF2F7B7270ee7831574Ae5",
            reader="0x67b789D48c926006F5132BFCe4e976F0A7A63d5D",
            reward_reader="0x04Fc11Bd28763872d143637a7c768bD96E44c1b6",
            order_book_reader="0xccFE3E576f8145403d3ce8f3c2f6519Dae40683B",
            staked_gmx="0x4d268a7d4C16ceB5a606c173Bd974984343fea13",
            staked_glp="0xaE64d55a6f09E4263421737397D1fdFA71896a69",
            glp_manager="0xD152c7F25db7F4B95b7658323c5F33d176818EE4",
            reward_router="0x82147C5A7E850eA4E28155DF107F2590fD4ba327",
            glp_reward_router="0xB70B91CE0771d3f4c81D87660f71Da31d48eB3B3",
            referral_storage="0x827ED045002eCdAbEb6e2b0d1604cf5fC3d322F8",
            dex_pool="0x0c91a070f862666bBcce281346BE45766d874D98",  # trader_joe pool
        )

        if chain == ChainIdEnum.ARBITRUM:
            return arbitrum_gmx_protocol_addresses
        elif chain == ChainIdEnum.AVALANCHE:
            return avalanche_gmx_protocol_addresses
        else:
            raise ValueError("Chain not supported")


print(GMXMultichainAddressGetter.get_chain(ChainIdEnum.ARBITRUM).glp_manager)
print(GMXMultichainAddressGetter.get_chain(ChainIdEnum.AVALANCHE).glp_manager)
