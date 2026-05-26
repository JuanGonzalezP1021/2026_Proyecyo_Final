from modelo.agente_chat import AgenteChat
from repositorio.chat_dao import ChatDAO


dao = ChatDAO()

while True:

    print("\nCALL CENTER CHAT ")
    print("1. Crear agente")
    print("2. Buscar agente")
    print("3. Actualizar agente")
    print("4. Eliminar agente")
    print("5. Listar agentes")
    print("6. Calcular AHT")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    # CREAR
    if opcion == "1":

        agent_id = input("ID del agente: ")
        manager = input("Team manager: ")
        aht = float(input("Chat AHT: "))
        chats = int(input("Chats concurrentes: "))

        agente = AgenteChat(
            agent_id,
            manager,
            aht,
            chats
        )

        if dao.crear(agente):
            print("Agente creado correctamente.")
        else:
            print("El agente ya existe.")

    # BUSCAR
    elif opcion == "2":

        agent_id = input("Ingrese ID: ")

        agente = dao.obtener(agent_id)

        if agente:
            print(agente.to_dict())
        else:
            print("Agente no encontrado.")

    # ACTUALIZAR
    elif opcion == "3":

        agent_id = input("ID del agente: ")

        agente = dao.obtener(agent_id)

        if agente:

            nuevo_aht = float(input("Nuevo AHT: "))
            nuevos_chats = int(input("Nuevos chats concurrentes: "))

            agente.set_chat_aht(nuevo_aht)
            agente.set_concurrent_chats(nuevos_chats)

            dao.actualizar(agente)

            print("Agente actualizado.")

        else:
            print("Agente no encontrado.")

    # ELIMINAR
    elif opcion == "4":

        agent_id = input("ID del agente: ")

        if dao.eliminar(agent_id):
            print("Agente eliminado.")
        else:
            print("No existe ese agente.")

    # LISTAR
    elif opcion == "5":

        agentes = dao.obtener_todos()

        if len(agentes) == 0:
            print("No hay agentes registrados.")

        for agente in agentes:
            print(agente.to_dict())

    # CALCULAR AHT
    elif opcion == "6":

        agent_id = input("ID del agente: ")

        agente = dao.obtener(agent_id)

        if agente:
            print("AHT:", agente.calcular_aht())
        else:
            print("Agente no encontrado.")

    # SALIR
    elif opcion == "7":

        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")