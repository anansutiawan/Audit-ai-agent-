import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_with_ai(audit_text, model="openai"):
    prompt = f"Analisis keamanan dari smart contract ini:\n{audit_text}\n\nBerikan ringkasan dan rekomendasi."

    if model == "openai":
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Kamu adalah auditor smart contract."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    else:
        return "Model belum didukung."
