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


Cara Penggunaan

1. Salin .env.example menjadi .env, lalu isi API key yang dibutuhkan.


2. Jalankan script:



python main.py

3. Ikuti instruksi di terminal untuk memasukkan alamat kontrak yang ingin diaudit.



Contoh Output

Laporan deteksi kerentanan oleh Slither

Ringkasan audit oleh AI: potensi bug, pattern mencurigakan, rekomendasi perbaikan


Rencana Pengembangan

Integrasi laporan dalam format PDF

Audit otomatis untuk seluruh project di GitHub

Penambahan plugin untuk Solidity 0.8+ dan Vyper


Kontribusi

Pull request dan masukan sangat diterima. Silakan fork repo ini atau buat issue jika ada saran.
