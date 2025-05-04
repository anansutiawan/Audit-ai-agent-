from audit.fetch_code import get_source_from_infura
from audit.run_slither import run_slither_audit
from audit.summarize import summarize_with_ai

contract_address = input("Masukkan alamat kontrak: ")
source_code = get_source_from_infura(contract_address)

if source_code:
    with open("Contract.sol", "w") as f:
        f.write(source_code)

    slither_result = run_slither_audit("Contract.sol")
    summary = summarize_with_ai(slither_result, model="openai")

    print("\n=== Ringkasan Audit ===")
    print(summary)
else:
    print("Gagal mengambil source code.")
