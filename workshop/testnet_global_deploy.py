from global_contract import SaveInfo
from pyteal import *
from beaker import *
import os
from dotenv import load_dotenv

from algosdk import mnemonic
from algosdk import account

from algosdk.atomic_transaction_composer import AccountTransactionSigner
from beaker.client import ApplicationClient, Network
from beaker.client.api_providers import AlgoNode

load_dotenv()

passphrase = os.environ.get("PASSPHRASE")

SaveInfo().dump("artifacts")

pk_signer = AccountTransactionSigner(mnemonic.to_private_key(passphrase))
user_address = account.address_from_private_key(pk_signer.private_key)
print (f"Cuenta: {user_address}")

app_client = ApplicationClient(
    client = AlgoNode(Network.TestNet).algod(),
    app = SaveInfo(),
    signer = pk_signer
)

app_id, app_addr, txid = app_client.create()

open ("./artifacts/app_id", "w").write(str(app_id))

print (
    f"""
        Aplicación desplegada txid {txid}
        App ID: {app_id}
        Address: {app_addr}
   """
)