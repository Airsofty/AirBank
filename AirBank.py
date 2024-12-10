import re
import random
import time

def encrypt_data(data):
    return f"ENCRYPTED({data})"

def decrypt_data(data):
    return data.replace("ENCRYPTED(", "").replace(")", "")

def validate_iban(iban):
    iban_pattern = r"^[A-Z]{2}\d{2}[A-Z0-9]{1,30}$"
    if not re.match(iban_pattern, iban):
        return False

    country_prefix = iban[:2]
    iban_lengths = {
        "RO": 24,
        "DE": 22,
        "FR": 27,
        "IT": 27,
        "NL": 18,
    }
    if country_prefix in iban_lengths and len(iban) != iban_lengths[country_prefix]:
        return False
    
    return True

def communicate_with_bank(payload):
    print("Trimitere date către serverul băncii...")
    time.sleep(2)
    encrypted_payload = encrypt_data(payload)
    print(f"Date criptate trimise: {encrypted_payload}")
    server_responses = [
        "SUCCESS: Transfer aprobat.",
        "ERROR: Fonduri insuficiente.",
        "ERROR: IBAN destinatar invalid.",
        "ERROR: Sistem indisponibil temporar.",
    ]
    response = random.choice(server_responses)
    time.sleep(2)
    print(f"Răspuns de la server: {response}")

    return response

def process_transfer(sender_iban, receiver_iban, amount):
    print("\n--- Procesare Transfer ---")
    print(f"Verificare IBAN expeditor: {sender_iban}")
    time.sleep(1)
    if not validate_iban(sender_iban):
        print("Eroare: IBAN-ul expeditorului este invalid.")
        return

    print(f"Verificare IBAN destinatar: {receiver_iban}")
    time.sleep(1)
    if not validate_iban(receiver_iban):
        print("Eroare: IBAN-ul destinatarului este invalid.")
        return

    print("Verificare sumă transfer...")
    time.sleep(1)
    if amount <= 0:
        print("Eroare: Suma trebuie să fie mai mare decât zero.")
        return

    payload = f"IBAN_SENDER={sender_iban}&IBAN_RECEIVER={receiver_iban}&AMOUNT={amount}"
    response = communicate_with_bank(payload)

    if "SUCCESS" in response:
        print("\nTransferul a fost procesat cu succes!")
        print("Suma a fost debitată din contul expeditorului și creditată în contul destinatarului.")
    else:
        print("\nTransferul nu a fost efectuat.")
        print(f"Motiv: {response.split(': ')[1]}")

def airsofty_interface():
    print("\n--- Airsofty Bank Transfer Simulator ---")
    print("Bine ați venit! Acesta este un simulator bancar complet nefuncțional.\n")
    
    while True:
        print("\nMeniu principal:")
        print("1. Efectuează un transfer")
        print("2. Ieșire")
        
        choice = input("Alegeți o opțiune: ")
        
        if choice == '1':
            sender_iban = input("Introduceți IBAN-ul expeditorului (ex: RO49AAAA1B31007593840000): ")
            receiver_iban = input("Introduceți IBAN-ul destinatarului (ex: RO49BBBB1B31007593840001): ")
            try:
                amount = float(input("Introduceți suma de transfer (RON): "))
            except ValueError:
                print("Eroare: Suma introdusă nu este validă.")
                continue

            process_transfer(sender_iban, receiver_iban, amount)

        elif choice == '2':
            print("Vă mulțumim că ați utilizat Airsofty! La revedere!")
            break
        else:
            print("Opțiune invalidă. Încercați din nou.")

if __name__ == "__main__":
    airsofty_interface()
