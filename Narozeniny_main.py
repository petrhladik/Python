from Narozeniny import narozeniny

narozeniny()
responce = input("\nChceš zadávat znovu? ano / ne: ")

while responce not in {"ano", "ne"}:
    responce = input("Prosím, zadej 'ano' nebo 'ne': ")

if (responce == "ano"):
    while True:
        while responce not in {"ano", "ne"}:
            responce = input("Prosím, zadej 'ano' nebo 'ne': ")
        narozeniny()
        responce = input("\nChceš zadávat znovu? ano / ne: ")
        if responce != "ano":
            input("Tak se měj. Čau")
            break
else:
    input("Tak se měj. Čau")