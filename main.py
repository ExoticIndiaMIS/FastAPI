from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from db import get_connection

app = FastAPI()

# ✅ Request model
class ProductRequest(BaseModel):
    itemcode: str

# ✅ POST: Fetch product by itemcode
@app.post("/product")
def get_product(request: ProductRequest):
    conn = get_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="DB connection failed")

    cursor = conn.cursor(dictionary=True)
    sql = "SELECT * FROM products WHERE itemcode = %s"
    cursor.execute(sql, (request.itemcode,))
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    if not result:
        raise HTTPException(status_code=404, detail="Item not found")

    return result
