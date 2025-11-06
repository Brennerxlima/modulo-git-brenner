"""
Desafio Módulo Git

Neste arquivo você encontrará funções **incompletas** que representam
tarefas relacionadas ao aprendizado de Git e GitHub.

Seu objetivo é:
- Criar uma issue para cada função.
- Implementar a função em uma branch específica.
- Fazer commit, criar tag e abrir Pull Request.
- Repetir o processo até concluir todas as funções.

Boa sorte e bons commits! 🚀
"""
import re

def mostrar_mensagem_inicial():
    """
    Exibe uma mensagem de boas-vindas ao desafio.
    Retorno esperado: string com a mensagem "Bem-vindo ao Desafio de Git!"
    """
    return print("\nBem-vindo ao Desafio de Git!\n")

def listar_comandos_git_basicos():
    """
    Retorna e exibe uma lista com os principais comandos básicos do Git.
    Exemplo de saída:
    ["git init", "git add", "git commit", "git status", "git push"]
    """
    comandos = ["git init", "git add", "git commit", "git status", "git push"]
    return print(f"Estes são alguns comandos básicos do git:\n >", comandos)

def criar_mensagens_commit_automaticas():
    """
    Gera mensagens de commit automaticamente
    para todas as funções do desafio (implementadas e pendentes).
    """
    funcoes = [
        "mostrar_mensagem_inicial",
        "listar_comandos_git_basicos",
        "criar_mensagem_commit",
        "verificar_tag_valida",
        "gerar_relatorio_final"
    ]

    tags = [
        "V1.0.1 - Primeira versão estável",
        "V1.0.2 - Segunda versão estável",
        "V1.0.3 - Terceira versão estável",
        "V1.0.4 - Quarta versão estável",
        "V1.0.5 - Quinta versão estável"
    ]
    
    mensagens = [f"Função {f}" for f in funcoes]
    tags_versoes = [f"Tag {t}" for t in tags]

    # Junta as duas listas de forma correspondente
    result = [f"{m} - {t}" for m, t in zip(mensagens, tags_versoes)]

    # Imprime tudo apenas uma vez
    print("\n".join(result))

def verificar_tag_valida(tag):
    """
    Verifica se uma tag está no formato 'vX.Y.Z' (ex: v1.0.0, v2.3.1).
    Retorna True se o formato for válido, caso contrário False.
    """
    padrao = r"^v\d+\.\d+\.\d+$"
    return bool(re.match(padrao, tag))

def gerar_relatorio_final(funcoes_concluidas):
    """
    Recebe uma lista com os nomes das funções implementadas
    e retorna uma mensagem final do desafio.

    Exemplo:
    gerar_relatorio_final(["mostrar_mensagem_inicial", "listar_comandos_git_basicos"])
    ->
    "Desafio concluído! 2 funções implementadas com sucesso."
    """
    quantidade = len(funcoes_concluidas)

    if quantidade == 0:
        print("Nenhuma função foi implementada ainda.")
    elif quantidade == 1:
        print(f"Desafio em progresso! 1 função implementada com sucesso: {funcoes_concluidas[0]}.")
    else:
        nomes = ", ".join(funcoes_concluidas)
        print(f"Desafio concluído! {quantidade} funções implementadas com sucesso: {nomes}.")


# Chamadas das funções
mostrar_mensagem_inicial()
listar_comandos_git_basicos()
criar_mensagens_commit_automaticas()
print(verificar_tag_valida("v1.0.0"))
gerar_relatorio_final([
    "mostrar_mensagem_inicial",
    "listar_comandos_git_basicos",
    "criar_mensagens_commit_automaticas",
    "verificar_tag_valida",
    "gerar_relatorio_final"
])