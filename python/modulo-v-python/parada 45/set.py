tarefas = []
concluidas = set()

#add tarefas
tarefas.append("Estudar Java")
tarefas.append("fazer exers")
tarefas.append("ler livro")

#marcar uma tarefa como concluida
concluidas.add(tarefas[0])

#exibir todas as tarefas e quais foram concluidas
for tarefa in tarefas:
  status = "concluida" if tarefa in concluidas else "pendente"
  print(f"tarefa: {tarefa}, status {status}")