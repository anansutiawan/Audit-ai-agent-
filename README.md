# Audit AI Agent

Audit AI Agent adalah agen otomatis berbasis AI yang dirancang untuk membantu proses audit smart contract berbasis Ethereum. Sistem ini menggabungkan alat analisis statis seperti **Slither** dengan model bahasa besar (**LLM**) untuk menghasilkan ringkasan dan deteksi potensi kerentanan secara otomatis.

## Fitur

- Fetch source code dari smart contract di blockchain (melalui Infura atau Etherscan).
- Analisis kerentanan dengan Slither.
- Ringkasan hasil audit dengan prompt AI.
- Bisa dikembangkan lebih lanjut untuk multi-chain, auto-patch, atau laporan PDF.

## Teknologi yang Digunakan

- Python
- Slither (Trail of Bits)
- OpenAI API (LLM)
- Infura API
- Git & GitHub

## Instalasi

```bash
git clone https://github.com/anansutiawan/Audit-ai-agent-.git
cd Audit-ai-agent-
pip install -r requirements.txt
