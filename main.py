import unittest
import os

from modelo.agente_phone import AgentePhone
from modelo.agente_chat import AgenteChat
from modelo.agente_email import AgenteEmail
from repositorio.phone_dao import PhoneDAO
from repositorio.chat_dao import ChatDAO
from repositorio.email_dao import EmailDAO

phone_dao = PhoneDAO()
chat_dao  = ChatDAO()
email_dao = EmailDAO()

# ──────────────────────────────────────────────
# FUNCIONES AUXILIARES DE VALIDACIÓN 
# ──────────────────────────────────────────────

def leer_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("❌ Error: Ingrese un número decimal válido.")

def leer_int(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("❌ Error: Ingrese un número entero válido.")

# ──────────────────────────────────────────────
# MENÚS POR CANAL
# ──────────────────────────────────────────────

def menu_phone():
    while True:
        print("\n CALL CENTER — PHONE")
        print("1. Crear agente")
        print("2. Buscar agente")
        print("3. Actualizar handle_time")
        print("4. Eliminar agente")
        print("5. Listar agentes")
        print("6. Calcular AHT")
        print("7. Volver")
        op = input("Seleccione: ")

        if op == "1":
            aid = input("ID: ")
            tm  = input("Team Manager: ")
            ht  = leer_float("Handle Time (seg): ")
            tx  = leer_int("Inbound Transactions: ")
            a   = AgentePhone(aid, tm, ht, tx)
            print("Creado ✓" if phone_dao.crear(a) else "Ya existe ese ID.")

        elif op == "2":
            a = phone_dao.obtener(input("ID: "))
            print(a if a else "No encontrado.")

        elif op == "3":
            aid = input("ID: ")
            a   = phone_dao.obtener(aid)
            if a:
                a.set_handle_time(leer_float("Nuevo handle_time: "))
                print("Actualizado ✓" if phone_dao.actualizar(a) else "Error.")
            else:
                print("No encontrado.")

        elif op == "4":
            print("Eliminado ✓" if phone_dao.eliminar(input("ID: ")) else "No encontrado.")

        elif op == "5":
            agentes = phone_dao.obtener_todos()
            print(f"\n{len(agentes)} agente(s):")
            for a in agentes: print(" ", a.to_dict())

        elif op == "6":
            a = phone_dao.obtener(input("ID: "))
            print(f"AHT: {a.calcular_aht()} seg" if a else "No encontrado.")

        elif op == "7":
            break


def menu_chat():
    while True:
        print("\n CALL CENTER — CHAT")
        print("1. Crear agente")
        print("2. Buscar agente")
        print("3. Actualizar chat_aht")
        print("4. Eliminar agente")
        print("5. Listar agentes")
        print("6. Calcular AHT")
        print("7. Volver")
        op = input("Seleccione: ")

        if op == "1":
            aid = input("ID: ")
            tm  = input("Team Manager: ")
            ca  = leer_float("Chat AHT: ")
            cc  = leer_int("Concurrent Chats: ")
            a   = AgenteChat(aid, tm, ca, cc)
            print("Creado ✓" if chat_dao.crear(a) else "Ya existe ese ID.")

        elif op == "2":
            a = chat_dao.obtener(input("ID: "))
            print(a if a else "No encontrado.")

        elif op == "3":
            aid = input("ID: ")
            a   = chat_dao.obtener(aid)
            if a:
                a.set_chat_aht(leer_float("Nuevo chat_aht: "))
                print("Actualizado ✓" if chat_dao.actualizar(a) else "Error.")
            else:
                print("No encontrado.")

        elif op == "4":
            print("Eliminado ✓" if chat_dao.eliminar(input("ID: ")) else "No encontrado.")

        elif op == "5":
            agentes = chat_dao.obtener_todos()
            print(f"\n{len(agentes)} agente(s):")
            for a in agentes: print(" ", a.to_dict())

        elif op == "6":
            a = chat_dao.obtener(input("ID: "))
            print(f"AHT: {a.calcular_aht()} seg" if a else "No encontrado.")

        elif op == "7":
            break


def menu_email():
    while True:
        print("\n CALL CENTER — EMAIL")
        print("1. Crear agente")
        print("2. Buscar agente")
        print("3. Actualizar handle_time")
        print("4. Eliminar agente")
        print("5. Listar agentes")
        print("6. Calcular AHT y ACW")
        print("7. Volver")
        op = input("Seleccione: ")

        if op == "1":
            aid = input("ID: ")
            tm  = input("Team Manager: ")
            ht  = leer_float("Handle Time (seg): ")
            tx  = leer_int("Inbound Transactions: ")
            acw = leer_float("ACW (seg): ")
            a   = AgenteEmail(aid, tm, ht, tx, acw)
            print("Creado ✓" if email_dao.crear(a) else "Ya existe ese ID.")

        elif op == "2":
            a = email_dao.obtener(input("ID: "))
            print(a if a else "No encontrado.")

        elif op == "3":
            aid = input("ID: ")
            a   = email_dao.obtener(aid)
            if a:
                a.set_handle_time(leer_float("Nuevo handle_time: "))
                print("Actualizado ✓" if email_dao.actualizar(a) else "Error.")
            else:
                print("No encontrado.")

        elif op == "4":
            print("Eliminado ✓" if email_dao.eliminar(input("ID: ")) else "No encontrado.")

        elif op == "5":
            agentes = email_dao.obtener_todos()
            print(f"\n{len(agentes)} agente(s):")
            for a in agentes: print(" ", a.to_dict())

        elif op == "6":
            a = email_dao.obtener(input("ID: "))
            if a:
                print(f"AHT: {a.calcular_aht()} seg")
                print(f"ACW promedio: {a.calcular_acw_promedio()} seg")
            else:
                print("No encontrado.")

        elif op == "7":
            break


# ──────────────────────────────────────────────
# RUNNER DE PRUEBAS
# ──────────────────────────────────────────────

def correr_pruebas():
    print("\n Ejecutando pruebas unitarias...\n")
    loader = unittest.TestLoader()
    suite  = unittest.TestSuite()

    for modulo in ["tests.test_phone_crud", "tests.test_chat_crud", "tests.test_email_crud"]:
        try:
            suite.addTests(loader.loadTestsFromName(modulo))
        except Exception as e:
            print(f"  ⚠ No se pudo cargar {modulo}. Detalle: {e}")

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


# ──────────────────────────────────────────────
# MENÚ PRINCIPAL
# ──────────────────────────────────────────────

def main():
    while True:
        print("\n══════════════════════════════")
        print("   CALL CENTER KPI — CRUD")
        print("══════════════════════════════")
        print("1. Gestionar agentes Phone")
        print("2. Gestionar agentes Chat")
        print("3. Gestionar agentes Email")
        print("4. Ejecutar pruebas unitarias")
        print("5. Salir")
        op = input("Seleccione una opción: ")

        if   op == "1": menu_phone()
        elif op == "2": menu_chat()
        elif op == "3": menu_email()
        elif op == "4": correr_pruebas()
        elif op == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
