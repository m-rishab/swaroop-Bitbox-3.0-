import pytezos

# Initialize the Tezos client
tezos = pytezos.using(key='your_private_key', shell='your_tezos_shell_url')

# Load the smart contract instance
contract = tezos.contract('your_contract_address')

# Define the metadata for the avatar
avatar_metadata = {
    'name': 'My Avatar',
    'description': 'This is my custom avatar',
    'image': 'https://oaidalleapiprodscus.blob.core.windows.net/private/org-xLuJ4yNn8usOyGNFrwjiKCGJ/user-QFuMugZsArJdLoDWqd3u0frq/img-vsfmz9RO82y6y7SysLLXVYA0.png?st=2023-04-15T09%3A08%3A39Z&se=2023-04-15T11%3A08%3A39Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-04-15T08%3A32%3A59Z&ske=2023-04-16T08%3A32%3A59Z&sks=b&skv=2021-08-06&sig=KdBlynd3cXvAJXgFThvWkjQiZ%2BtY8h%2BVXEMGpHYOQM8%3D'
}

# Call the mint entry point to create the NFT
operation = contract.mint(token_metadata=avatar_metadata).autofill().sign().inject()

# Wait for the transaction to be included in a block
tezos.wait_for_inclusion(operation['hash'])

# Get the ID of the newly minted token
token_id = operation['contents'][0]['metadata']['operation_result']['big_map_diff'][0]['key'][0]

print(f"Avatar NFT minted with ID {token_id}")