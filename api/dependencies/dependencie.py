"""
    Injeção de Dependência (Dependency Injection – DI) é um padrão de projeto usado para desacoplar componentes de um sistema, delegando a criação e o fornecimento das dependências a um mecanismo externo, em vez de o próprio objeto criá-las diretamente.

    * um objeto recebe aquilo de que precisa para funcionar, em vez de criar essas coisas por conta própria.

    Conceito básico:

    * Uma dependência é qualquer objeto ou serviço que outro objeto utiliza para executar sua lógica.

    Exemplo:

    * Uma classe que acessa o banco de dados depende de um repositório

    * Um serviço que envia e-mails depende de um cliente SMTP

    * Um controller depende de um service

    * Sem DI, a classe cria suas próprias dependências.
    * Com DI, alguém “injeta” essas dependências nela.
"""

from fastapi import FastAPI, Depends
from typing import Annotated

app = FastAPI()


async def commom_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {
        "q": q,
        "skip": skip,
        "limit": limit
    }

CommonDep = Annotated[dict, Depends(commom_parameters)]

@app.get("/items/")
async def read_items(commons: CommonDep):
    return commons


@app.get('/users/')
async def read_users(commons: CommonDep):
    return commons