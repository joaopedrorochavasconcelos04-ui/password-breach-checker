import hashlib, json, os, urllib.error, urllib.request, time

def checar_senha_api(senha):
    h = hashlib.sha1(senha.encode()).hexdigest().upper()
    url = f"https://api.pwnedpasswords.com/range/{h[:5]}"
    try:
        with urllib.request.urlopen(url) as r:
            texto = r.read().decode("utf-8")
    except urllib.error.HTTPError as erro:
        return {"status": "erro", "erro_codigo": erro.code}

    for linha in texto.split():
        fim, qtd = linha.split(":")
        if fim == h[5:]:
            return {"status": "sucesso", "vazamentos": int(qtd)}
            
    return {"status": "sucesso", "vazamentos": 0}

# --- MENU PRINCIPAL ---
print("=========================================")
print("Verificador de vazamentos de senha:")
print("1 - Verificação por lotes (Arquivos .txt)")
print("2 - Verificação única (Input)")
print("=========================================")

opcao = input("Escolha uma opção (1 ou 2): ").strip()

# Guard Clause: Opção inválida
if opcao not in ("1", "2"):
    print(json.dumps({"erro": "Opção inválida do menu"}, indent=4, ensure_ascii=False))
    exit()

# --- FLUXO 1: VERIFICAÇÃO EM LOTE ---
if opcao == "1":
    nome_arquivo = input("Digite o nome do arquivo (ex: senhas.txt): ").strip()
    
    # Guard Clauses
    if not nome_arquivo:
        print(json.dumps({"erro": "O nome do arquivo não pode ser vazio"}, indent=4, ensure_ascii=False))
        exit()
        
    if not os.path.exists(nome_arquivo):
        print(json.dumps({"erro": f"O arquivo '{nome_arquivo}' não foi encontrado"}, indent=4, ensure_ascii=False))
        exit()

    # Dicionário que vai guardar a estrutura final do JSON
    resultado_final = {
        "tipo_verificacao": "lote",
        "arquivo_origem": nome_arquivo,
        "resultados": {}
    }

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            senha = linha.strip()
            if not senha: 
                continue
            
            resposta = checar_senha_api(senha)
            
            # Alimenta o dicionário usando a senha como chave
            if resposta["status"] == "sucesso":
                resultado_final["resultados"][senha] = {
                    "vazada": resposta["vazamentos"] > 0,
                    "quantidade": resposta["vazamentos"]
                }
            else:
                resultado_final["resultados"][senha] = {
                    "erro": f"Falha na API (Status {resposta['erro_codigo']})"
                }
            
            time.sleep(0.5)

    # Converte o dicionário final para uma string formatada em JSON e exibe
    json_output = json.dumps(resultado_final, indent=4, ensure_ascii=False)
    print("\n--- OUTPUT JSON ---")
    print(json_output)

# --- FLUXO 2: VERIFICAÇÃO ÚNICA ---
elif opcao == "2":
    senha_unica = input("Digite a senha que deseja consultar: ")
    
    # Guard Clause
    if not senha_unica:
        print(json.dumps({"erro": "Nenhuma senha foi digitada"}, indent=4, ensure_ascii=False))
        exit()

    resposta = checar_senha_api(senha_unica)
    
    resultado_unico = {
        "tipo_verificacao": "unica",
        "senha_analisada": senha_unica,
        "vazada": resposta.get("vazamentos", 0) > 0 if resposta["status"] == "sucesso" else "erro",
        "quantidade": resposta.get("vazamentos", 0) if resposta["status"] == "sucesso" else 0
    }
    
    print("\n--- OUTPUT JSON ---")
    print(json.dumps(resultado_unico, indent=4, ensure_ascii=False))
