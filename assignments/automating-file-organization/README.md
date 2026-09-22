# 📘 Assignment: Automating File Organization with Python

## 🎯 Objective

Construa um script Python que organize automaticamente arquivos de uma pasta em subpastas por categoria. Você praticará o uso de `pathlib`, funções, manipulação de arquivos e execução segura de operações de automação.

## 📝 Tasks

### 🛠️ Listar e categorizar arquivos

#### Descrição
Explore uma pasta informada pelo usuário e classifique os arquivos encontrados de acordo com suas extensões. Nesta etapa, o programa deve apenas exibir o que seria organizado, sem mover arquivos.

#### Requisitos
O programa concluído deve:

- Usar `pathlib.Path` para trabalhar com caminhos e arquivos
- Ignorar subpastas e considerar somente arquivos diretamente dentro da pasta de origem
- Categorizar extensões comuns em grupos como `Images`, `Documents`, `Audio`, `Videos` e `Other`
- Exibir o nome de cada arquivo e sua categoria
- Tratar uma pasta de origem inexistente com uma mensagem clara


### 🛠️ Organizar arquivos por categoria

#### Descrição
Adicione a movimentação dos arquivos para subpastas dentro de uma pasta de destino. A organização deve ser previsível e não deve substituir arquivos que já existam.

#### Requisitos
O programa concluído deve:

- Criar as subpastas de categorias somente quando forem necessárias
- Mover cada arquivo para a subpasta correspondente usando `Path.rename()` ou `shutil.move()`
- Preservar o nome original do arquivo
- Evitar sobrescrever um arquivo existente, adicionando um sufixo como `_1` ao nome quando necessário
- Exibir um resumo com a quantidade de arquivos organizados em cada categoria


### 🛠️ Adicionar modo de simulação e opções de execução

#### Descrição
Torne o organizador mais seguro e reutilizável. Crie um modo de simulação que mostre as operações sem executá-las e permita escolher a pasta de origem e a pasta de destino pela linha de comando.

#### Requisitos
O programa concluído deve:

- Aceitar a pasta de origem como argumento da linha de comando
- Aceitar uma pasta de destino opcional e usar uma escolha padrão documentada quando ela não for informada
- Aceitar uma opção `--dry-run` que liste as movimentações sem alterar o sistema de arquivos
- Retornar uma mensagem de erro e um código de saída diferente de zero para argumentos inválidos
- Permitir executar o programa com um comando semelhante a:

```bash
python organizer.py ./downloads --destination ./organized --dry-run
```
