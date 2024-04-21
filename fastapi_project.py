from fastapi import FastAPI, Query, Request
from pydantic import BaseModel
from typing import Optional
from starlette.templating import Jinja2Templates
from starlette.responses import HTMLResponse

app = FastAPI() #inizializziamo l'applicazione fastAPI

templates = Jinja2Templates(directory="templates")

class Item(BaseModel):  #creiamo il nostro modello di base
    name: str
    price: float
    tax: Optional[float] = None

@app.post("/items/")    #creazione del primo endpoint
async def create_item(item: Item):
    item_with_tax = item.price * (1 + (item.tax or 0.0))
    return {"name": item.name, "price_with_tax": item_with_tax}

@app.get("/initialize_item/") #se non effettuiamo una richiesta con i valori settati possiamo usare questo endpoint per creare oggetti di default
async def initialize_item(name: str = Query("Default Item"), price: float = Query(100.0), tax: Optional[float] = Query(0.1)):
    new_item = Item(name=name, price=price, tax=tax)
    return new_item.dict()

@app.get('/',response_class=HTMLResponse)
async def ironic_page(request:Request):
    return templates.TemplateResponse("pagina_ironizzante.html", {"request": request})

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)