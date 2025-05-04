import requests
import os

INFURA_URL = "https://mainnet.infura.io/v3/" + os.getenv("INFURA_API_KEY")

def get_source_from_infura(contract_address):
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getCode",
        "params": [contract_address, "latest"],
        "id": 1
    }
    res = requests.post(INFURA_URL, json=payload)
    bytecode = res.json().get("result")
    if bytecode and bytecode != "0x":
        return f"// Bytecode detected\n{bytecode}"
    return None
