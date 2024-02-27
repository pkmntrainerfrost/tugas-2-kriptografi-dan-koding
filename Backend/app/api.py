from fastapi import FastAPI, Form, File, UploadFile, Request
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

import app.cipher as cipher

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
)

@app.post("/vigenere")
async def vigenere(text: str = Form(...), key: str = Form(...), encrypt: bool = Form(...), base64: bool = Form(...)) -> dict:
    
    if encrypt:
        return {"ciphertext" : cipher.vigenereEncrypt(text,key)}
    else:
        return {"plaintext" : cipher.vigenereDecrypt(text,key)}

@app.post("/vigenere/file")
async def vigenere(textfile: UploadFile = File(...), key: str = Form(...), encrypt: bool = Form(...), base64: bool = Form(...)) -> dict:
    
    text = textfile.file.read().decode()

    if encrypt:
        return {"ciphertext" : cipher.vigenereEncrypt(text,key)}
    else:
        return {"plaintext" : cipher.vigenereDecrypt(text,key)}

@app.post("/playfair")
async def playfair(text: str = Form(...), key: str = Form(...), encrypt: bool = Form(...), base64: bool = Form(...)) -> dict:
    
    if encrypt:
        return {"ciphertext" : cipher.playfairEncrypt(text,key)}
    else:
        return {"plaintext" : cipher.playfairDecrypt(text,key)}
    
@app.post("/playfair/file")
async def playfair(textfile: UploadFile = File(...), key: str = Form(...), encrypt: bool = Form(...), base64: bool = Form(...)) -> dict:
    
    text = textfile.file.read().decode()

    if encrypt:
        return {"ciphertext" : cipher.playfairEncrypt(text,key)}
    else:
        return {"plaintext" : cipher.playfairDecrypt(text,key)}
    
@app.post("/vigenereautokey")
async def vigereautokey(text: str = Form(...), key: str = Form(...), encrypt: bool = Form(...), base64: bool = Form(...)) -> dict:
    
    if encrypt:
        return {"ciphertext" : cipher.vigenereAutokeyEncrypt(text,key)}
    else:
        return {"plaintext" : cipher.vigenereAutokeyDecrypt(text,key)}

@app.post("/vigenereautokey/file")
async def vigereautokey(textfile: UploadFile = File(...), key: str = Form(...), encrypt: bool = Form(...), base64: bool = Form(...)) -> dict:
    
    text = textfile.file.read().decode()

    if encrypt:
        return {"ciphertext" : cipher.vigenereAutokeyEncrypt(text,key)}
    else:
        return {"plaintext" : cipher.vigenereAutokeyDecrypt(text,key)}

@app.post("/product")
async def product(text: str = Form(...), vigenere_key: str = Form(...), transposition_key: int = Form(...), encrypt: bool = Form(...), base64: bool = Form(...)) -> dict:
    
    if encrypt:
        return {"ciphertext" : cipher.productEncrypt(text,vigenere_key,transposition_key)}
    else:
        return {"plaintext" : cipher.productDecrypt(text,vigenere_key,transposition_key)}

@app.post("/product/file")
async def product(textfile: UploadFile = File(...), vigenere_key: str = Form(...), transposition_key: int = Form(...), encrypt: bool = Form(...), base64: bool = Form(...)) -> dict:
    
    text = textfile.file.read().decode()

    if encrypt:
        return {"ciphertext" : cipher.productEncrypt(text,vigenere_key,transposition_key)}
    else:
        return {"plaintext" : cipher.productDecrypt(text,vigenere_key,transposition_key)}
    
@app.post("/affine")
async def affine(text: str = Form(...), vigenere_key: str = Form(...), m: int = Form(...), b: int = Form(...), encrypt: bool = Form(...), base64: bool = Form(...)) -> dict:
    
    if encrypt:
        return {"ciphertext" : cipher.affineEncrypt(text,vigenere_key,m,b)}
    else:
        return {"plaintext" : cipher.affineDecrypt(text,vigenere_key,m,b)}

@app.post("/product/file")
async def affine(textfile: UploadFile = File(...), vigenere_key: str = Form(...), m: int = Form(...), b: int = Form(...), encrypt: bool = Form(...), base64: bool = Form(...)) -> dict:
    
    text = textfile.file.read().decode()

    if encrypt:
        return {"ciphertext" : cipher.affineEncrypt(text,vigenere_key,m,b)}
    else:
        return {"plaintext" : cipher.affineDecrypt(text,vigenere_key,m,b)}
    