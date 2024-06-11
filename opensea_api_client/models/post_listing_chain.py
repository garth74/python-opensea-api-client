from enum import Enum


class PostListingChain(str, Enum):
    ARBITRUM = "arbitrum"
    ARBITRUM_GOERLI = "arbitrum_goerli"
    ARBITRUM_NOVA = "arbitrum_nova"
    AVALANCHE = "avalanche"
    AVALANCHE_FUJI = "avalanche_fuji"
    BAOBAB = "baobab"
    BASE = "base"
    BASE_GOERLI = "base_goerli"
    BSC = "bsc"
    BSCTESTNET = "bsctestnet"
    ETHEREUM = "ethereum"
    GOERLI = "goerli"
    KLAYTN = "klaytn"
    MATIC = "matic"
    MUMBAI = "mumbai"
    OPTIMISM = "optimism"
    OPTIMISM_GOERLI = "optimism_goerli"
    SEPOLIA = "sepolia"
    SOLANA = "solana"
    SOLDEV = "soldev"
    ZORA = "zora"
    ZORA_TESTNET = "zora_testnet"

    def __str__(self) -> str:
        return str(self.value)
