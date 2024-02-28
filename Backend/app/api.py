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

        ciphertext = cipher.vigenereEncrypt(text,key)
        ciphertext = ciphertext if not base64 else cipher.base64Encrypt(ciphertext)

        return {"ciphertext" : ciphertext}
    
    else:

        plaintext = cipher.vigenereDecrypt((text if not base64 else cipher.base64Decrypt(text)),key)
    
        return {"plaintext" : plaintext}

@app.post("/vigenere/file")
async def vigenere(textfile: UploadFile = File(...), key: str = Form(...), encrypt: bool = Form(...), base64: bool = Form(...)) -> dict:
    
    text = textfile.file.read().decode()

    if encrypt:

        ciphertext = cipher.vigenereEncrypt(text,key)
        ciphertext = ciphertext if not base64 else cipher.base64Encrypt(ciphertext)

        return {"ciphertext" : ciphertext}
    
    else:

        plaintext = cipher.vigenereDecrypt((text if not base64 else cipher.base64Decrypt(text)),key)
    
        return {"plaintext" : plaintext}

@app.post("/playfair")
async def playfair(text: str = Form(...), key: str = Form(...), encrypt: bool = Form(...), base64: bool = Form(...)) -> dict:
    
    if encrypt:

        ciphertext = cipher.playfairEncrypt(text,key)
        ciphertext = ciphertext if not base64 else cipher.base64Encrypt(ciphertext)

        return {"ciphertext" : ciphertext}
    
    else:

        plaintext = cipher.playfairDecrypt((text if not base64 else cipher.base64Decrypt(text)),key)
    
        return {"plaintext" : plaintext}
    
@app.post("/playfair/file")
async def playfair(textfile: UploadFile = File(...), key: str = Form(...), encrypt: bool = Form(...), base64: bool = Form(...)) -> dict:
    
    text = textfile.file.read().decode()

    if encrypt:

        ciphertext = cipher.playfairEncrypt(text,key)
        ciphertext = ciphertext if not base64 else cipher.base64Encrypt(ciphertext)

        return {"ciphertext" : ciphertext}
    
    else:

        plaintext = cipher.playfairDecrypt((text if not base64 else cipher.base64Decrypt(text)),key)
    
        return {"plaintext" : plaintext}
    
@app.post("/vigenereautokey")
async def vigereautokey(text: str = Form(...), key: str = Form(...), encrypt: bool = Form(...), base64: bool = Form(...)) -> dict:
    
    if encrypt:

        ciphertext = cipher.vigenereAutokeyEncrypt(text,key)
        ciphertext = ciphertext if not base64 else cipher.base64Encrypt(ciphertext)

        return {"ciphertext" : ciphertext}
    
    else:

        plaintext = cipher.vigenereAutokeyDecrypt((text if not base64 else cipher.base64Decrypt(text)),key)
    
        return {"plaintext" : plaintext}

@app.post("/vigenereautokey/file")
async def vigereautokey(textfile: UploadFile = File(...), key: str = Form(...), encrypt: bool = Form(...), base64: bool = Form(...)) -> dict:
    
    text = textfile.file.read().decode()

    if encrypt:

        ciphertext = cipher.vigenereAutokeyEncrypt(text,key)
        ciphertext = ciphertext if not base64 else cipher.base64Encrypt(ciphertext)

        return {"ciphertext" : ciphertext}
    
    else:

        plaintext = cipher.vigenereAutokeyDecrypt((text if not base64 else cipher.base64Decrypt(text)),key)
    
        return {"plaintext" : plaintext}

@app.post("/product")
async def product(text: str = Form(...), vigenere_key: str = Form(...), transposition_key: int = Form(...), encrypt: bool = Form(...), base64: bool = Form(...)) -> dict:
    
    if encrypt:

        ciphertext = cipher.productEncrypt(text,vigenere_key,transposition_key)
        ciphertext = ciphertext if not base64 else cipher.base64Encrypt(ciphertext)

        return {"ciphertext" : ciphertext}
    
    else:

        plaintext = cipher.productDecrypt((text if not base64 else cipher.base64Decrypt(text)),vigenere_key,transposition_key)
    
        return {"plaintext" : plaintext}

@app.post("/product/file")
async def product(textfile: UploadFile = File(...), vigenere_key: str = Form(...), transposition_key: int = Form(...), encrypt: bool = Form(...), base64: bool = Form(...)) -> dict:
    
    text = textfile.file.read().decode()

    if encrypt:

        ciphertext = cipher.productEncrypt(text,vigenere_key,transposition_key)
        ciphertext = ciphertext if not base64 else cipher.base64Encrypt(ciphertext)

        return {"ciphertext" : ciphertext}
    
    else:

        plaintext = cipher.productDecrypt((text if not base64 else cipher.base64Decrypt(text)),vigenere_key,transposition_key)
    
        return {"plaintext" : plaintext}
    
@app.post("/affine")
async def affine(text: str = Form(...), m: int = Form(...), b: int = Form(...), encrypt: bool = Form(...), base64: bool = Form(...)) -> dict:
    
    if encrypt:

        ciphertext = cipher.affineEncrypt(text,m,b)
        ciphertext = ciphertext if not base64 else cipher.base64Encrypt(ciphertext)

        return {"ciphertext" : ciphertext}
    
    else:

        plaintext = cipher.affineDecrypt((text if not base64 else cipher.base64Decrypt(text)),m,b)
    
        return {"plaintext" : plaintext}

@app.post("/affine/file")
async def affine(textfile: UploadFile = File(...), m: int = Form(...), b: int = Form(...), encrypt: bool = Form(...), base64: bool = Form(...)) -> dict:
    
    text = textfile.file.read().decode()

    if encrypt:

        ciphertext = cipher.affineEncrypt(text,m,b)
        ciphertext = ciphertext if not base64 else cipher.base64Encrypt(ciphertext)

        return {"ciphertext" : ciphertext}
    
    else:

        plaintext = cipher.affineDecrypt((text if not base64 else cipher.base64Decrypt(text)),m,b)
    
        return {"plaintext" : plaintext}
    