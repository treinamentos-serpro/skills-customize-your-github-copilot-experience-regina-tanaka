# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Aprenda a criar uma API REST com FastAPI, organizando endpoints, validando dados com modelos Pydantic e retornando respostas HTTP apropriadas. Ao final, você terá uma API de tarefas que pode ser explorada pela documentação interativa do framework.

## 📝 Tasks

### 🛠️ Criar os primeiros endpoints

#### Descrição
Complete a estrutura inicial para criar uma API de tarefas. Execute o servidor localmente e implemente endpoints de leitura que permitam consultar a lista completa e uma tarefa específica.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI no arquivo `starter-code.py`
- Implementar `GET /` retornando uma mensagem que confirme que a API está funcionando
- Implementar `GET /tasks` retornando todas as tarefas armazenadas
- Implementar `GET /tasks/{task_id}` retornando uma tarefa pelo ID
- Retornar status HTTP `404` quando o ID solicitado não existir


### 🛠️ Validar e criar tarefas

#### Descrição
Use modelos Pydantic para definir o formato de uma tarefa e validar os dados recebidos em requisições. Depois, adicione a criação de novas tarefas à API.

#### Requisitos
O programa concluído deve:

- Definir um modelo para representar uma tarefa com título, descrição e indicação de conclusão
- Definir um modelo de entrada que exija um título não vazio
- Implementar `POST /tasks` para criar uma tarefa com um novo ID
- Retornar a tarefa criada com status HTTP `201`
- Permitir que o FastAPI gere mensagens de erro de validação para dados inválidos


### 🛠️ Atualizar e remover tarefas

#### Descrição
Complete o CRUD da API implementando atualização parcial e remoção de tarefas. Use os códigos de status adequados para comunicar o resultado de cada operação.

#### Requisitos
O programa concluído deve:

- Implementar `PATCH /tasks/{task_id}` para atualizar apenas os campos enviados
- Implementar `DELETE /tasks/{task_id}` para remover uma tarefa
- Retornar status HTTP `404` ao atualizar ou remover um ID inexistente
- Retornar uma resposta clara após uma remoção bem-sucedida
- Permitir testar todos os endpoints em `/docs`, a documentação interativa gerada pelo FastAPI

Para executar a API, instale as dependências e use:

```bash
pip install fastapi uvicorn
uvicorn starter-code:app --reload
```
