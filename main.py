from fastapi import FastAPI

app = FastAPI() 

vendas = {
    1: {"item": "video-game", "preco_unitario": 5000, "quantidade": 5  },
    2: {"item": "Alexa", "preco_unitario": 2560, "quantidade": 180},
    3: {"item": "Notebook", "preco_unitario": 1750, "quantidade": 3000},
    4: {"item": "smartphone", "preco_unitario": 1800, "quantidade": 8000}, 
}


@app.get("/")
def home():
    return {"Vendas": len(vendas)}

@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda: int):
    if id_venda in vendas:
        return vendas[id_venda]
    else:
        return {"Erro": "ID venda inexistente!" }
        
    
    
    