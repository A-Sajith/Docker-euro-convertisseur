import requests

url = "https://api.exchangerate-api.com/v4/latest/EUR"

response = requests.get(url)
data = response.json()

# On extrait les taux
usd = data["rates"]["USD"]
inr = data["rates"]["INR"]
jpy = data["rates"]["JPY"]

# L'utilisateur tape un montant
montant = float(input("Entrez un montant en euros : "))

# On calcule
print(f"\n{montant} EUR = {montant * usd:.2f} USD")
print(f"{montant} EUR = {montant * inr:.2f} INR")
print(f"{montant} EUR = {montant * jpy:.2f} JPY")