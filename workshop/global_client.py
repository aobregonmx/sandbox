from global_contract import SaveInfo
from pyteal import *
from beaker import *

text_file = open("./artifacts/app_id", "r")
app_id = int (text_file.read())
text_file.close()

account = sandbox.get_accounts()[0]

app_client = client.ApplicationClient(
    client = sandbox.get_algod_client(),
    app = SaveInfo(),
    app_id = app_id,
    signer = account.signer)

result = app_client.call(SaveInfo.get_name)

print(result.return_value)
