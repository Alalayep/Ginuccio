import json
from datetime import datetime

class Cliente:
    def __init__(self, nome, cognome, email):
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.storico_appuntamenti = []

    def __str__(self):
        return f"{self.nome} {self.cognome}"

class Appuntamento:
    def __init__(self, data, ora, tipo_di_servizio, cliente):
        self.data = data
        self.ora = ora
        self.tipo_di_servizio = tipo_di_servizio
        self.cliente = cliente

    def __str__(self):
        return f"{self.data} {self.ora}, {self.tipo_di_servizio}, Cliente: {self.cliente}"

class Salone:
    def __init__(self):
        self.agenda = []

    def aggiungi_appuntamento(self, appuntamento):
        self.agenda.append(appuntamento)

    def cancella_appuntamento(self, appuntamento):
        self.agenda.remove(appuntamento)

    def modifica_appuntamento(self, appuntamento, nuovo_ora):
        appuntamento.ora = nuovo_ora

    def ricerca_per_cliente(self, cliente):
        return [appuntamento for appuntamento in self.agenda if appuntamento.cliente == cliente]

    def ricerca_per_data(self, data):
        return [appuntamento for appuntamento in self.agenda if appuntamento.data == data]

    def salva_json(self):
        with open("agenda.json", 'w+') as file:
            json.dump([vars(appuntamento) for appuntamento in self.agenda], file)

    def carica_json(self):
        with open("agenda.json") as file:
            data = json.load(file)
            for item in data:
                cliente_data = item['cliente']
                cliente = Cliente(cliente_data['nome'], cliente_data['cognome'], cliente_data['email'])
                appuntamento = Appuntamento(item['data'], item['ora'], item['tipo_di_servizio'], cliente)
                self.agenda.append(appuntamento)

def main():
    salone = Salone()
    salone.carica_json("agenda.json")

    while True:
        print("\n1. Aggiungi Appuntamento")
        print("2. Cancella Appuntamento")
        print("3. Modifica Appuntamento")
        print("4. Ricerca per Cliente")
        print("5. Ricerca per Data")
        print("6. Esci")

        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":
            nome = input("Nome del cliente: ")
            cognome = input("Cognome del cliente: ")
            email = input("Email del cliente: ")
            cliente = Cliente(nome, cognome, email)
            data = input("Data dell'appuntamento (YYYY-MM-DD): ")
            ora = input("Ora dell'appuntamento (HH:MM): ")
            tipo_di_servizio = input("Tipo di servizio: ")
            appuntamento = Appuntamento(data, ora, tipo_di_servizio, cliente)
            salone.aggiungi_appuntamento(appuntamento)
        
        elif scelta == "2":
            cliente = input("Nome del cliente: ")
            appuntamenti_cliente = salone.ricerca_per_cliente(cliente)
            if not appuntamenti_cliente:
                print("Nessun appuntamento trovato per questo cliente.")
            else:
                print("Appuntamenti trovati per il cliente:")
                for i, appuntamento in enumerate(appuntamenti_cliente, 1):
                    print(f"{i}. {appuntamento}")
                index = int(input("Seleziona l'appuntamento da cancellare: ")) - 1
                salone.cancella_appuntamento(appuntamenti_cliente[index])

        elif scelta == "3":
            cliente = input("Nome del cliente: ")
            appuntamenti_cliente = salone.ricerca_per_cliente(cliente)
            if not appuntamenti_cliente:
                print("Nessun appuntamento trovato per questo cliente.")
            else:
                print("Appuntamenti trovati per il cliente:")
                for i, appuntamento in enumerate(appuntamenti_cliente, 1):
                    print(f"{i}. {appuntamento}")
                index = int(input("Seleziona l'appuntamento da modificare: ")) - 1
                nuovo_ora = input("Nuova ora dell'appuntamento (HH:MM): ")
                salone.modifica_appuntamento(appuntamenti_cliente[index], nuovo_ora)

        elif scelta == "4":
            cliente = input("Nome del cliente: ")
            appuntamenti_cliente = salone.ricerca_per_cliente(cliente)
            if not appuntamenti_cliente:
                print("Nessun appuntamento trovato per questo cliente.")
            else:
                print("Appuntamenti trovati per il cliente:")
                for appuntamento in appuntamenti_cliente:
                    print(appuntamento)

        elif scelta == "5":
            data = input("Data da cercare (YYYY-MM-DD): ")
            appuntamenti_data = salone.ricerca_per_data(data)
            if not appuntamenti_data:
                print("Nessun appuntamento trovato per questa data.")
            else:
                print("Appuntamenti trovati per la data:")
                for appuntamento in appuntamenti_data:
                    print(appuntamento)

        elif scelta == "6":
            salone.salva_su_file_json('agenda.json')
            break

        else:
            print("Scelta non valida. Riprova.")

    if __name__ == "__main__":
            main()
    else:main()==True