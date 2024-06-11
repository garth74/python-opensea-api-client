from enum import Enum


class ChainIdentifier(str, Enum):
    AMOY = "amoy"
    ARBITRUM = "arbitrum"
    ARBITRUM_NOVA = "arbitrum_nova"
    ARBITRUM_SEPOLIA = "arbitrum_sepolia"
    AVALANCHE = "avalanche"
    AVALANCHE_FUJI = "avalanche_fuji"
    BAOBAB = "baobab"
    BASE = "base"
    BASE_SEPOLIA = "base_sepolia"
    BLAST = "blast"
    BLAST_SEPOLIA = "blast_sepolia"
    BSC = "bsc"
    BSCTESTNET = "bsctestnet"
    ETHEREUM = "ethereum"
    KLAYTN = "klaytn"
    MATIC = "matic"
    MUMBAI = "mumbai"
    OPTIMISM = "optimism"
    OPTIMISM_SEPOLIA = "optimism_sepolia"
    SEPOLIA = "sepolia"
    SOLANA = "solana"
    SOLDEV = "soldev"
    ZORA = "zora"
    ZORA_SEPOLIA = "zora_sepolia"

    def __str__(self) -> str:
        return str(self.value)
