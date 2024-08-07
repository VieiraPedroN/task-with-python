from database import Database

def main():
    db = Database("tasks.db")
    
    while True:
        print("\nGerenciador de Tarefas")
        print("1. Adicionar Tarefa")
        print("2. Ver Tarefas")
        print("3. Remover Tarefa")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome_tarefa = input("Digite o nome da tarefa: ")
            db.add_task(nome_tarefa)
            print("Tarefa adicionada!")
        elif escolha == '2':
            tarefas = db.get_tasks()
            print("\nTarefas:")
            for tarefa in tarefas:
                print(f"- ID {tarefa[0]}: {tarefa[1]}")
        elif escolha == '3':
            id_tarefa = input("Digite o ID da tarefa para remover: ")
            db.remove_task(id_tarefa)
            print("Tarefa removida!")
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
