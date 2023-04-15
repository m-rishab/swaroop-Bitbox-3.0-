# Import required libraries
import smartpy as sp

# Define the Avatar NFT smart contract
class AvatarNFT(sp.Contract):
    def __init__(self):
        self.init(
            owner = sp.address('tz2FeTmaEvEUGjTNM5UjZ61Tf4gTC7ZbCQ7H'),  # replace with your Tezos address
            nft_count = 0,
            nft_metadata = {}
        )

    # Define a method to mint a new NFT
    @sp.entry_point
    def mint_avatar(self, metadata):
        sp.verify(self.data.owner == sp.sender, "Only the owner can mint NFTs")
        nft_id = self.data.nft_count
        self.data.nft_count += 1
        self.data.nft_metadata[nft_id] = metadata

        # Create the NFT
        nft = sp.nft_create(
            sp.map({nft_id: sp.to_utf8(metadata)}),
            sp.to_address(sp.sender),
            1
        )

        sp.set_type(nft, sp.TNat)
        sp.set_type(self.data.nft_count, sp.TNat)
        sp.set_type(self.data.nft_metadata, sp.TMap(sp.TNat, sp.TString))

    
    @sp.entry_point
    def transfer(self, params):
        from_token_id = params.tokenId
        to_address = params.toAddress
        sp.verify(sp.sender == self.data.tokenOwners[from_token_id], message="Only the token owner can transfer tokens")
        self.data.tokenOwners[from_token_id] = to_address
        owner_token_count_from = sp.as_int(self.data.ownerTokenCount.get(sp.sender, 0))
        owner_token_count_to = sp.as_int(self.data.ownerTokenCount.get(to_address, 0))
        self.data.ownerTokenCount[sp.sender] = owner_token_count_from - 1
        self.data.ownerTokenCount[to_address] = owner_token_count_to + 1


# Define the main smart contract
class Main(sp.Contract):
    def __init__(self):
        self.init()

    # Define a method to create a new Avatar NFT smart contract
    @sp.entry_point
    def create_avatar_nft(self):
        avatar_nft = AvatarNFT()
        sp.transfer(sp.tez(1), sp.address(avatar_nft))
