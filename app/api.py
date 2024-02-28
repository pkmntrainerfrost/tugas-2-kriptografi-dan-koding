from fastapi import FastAPI, Form, File, UploadFile, Request
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates


from pydantic import BaseModel

import app.cipher as cipher

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
)

app = FastAPI()
templates = Jinja2Templates(directory="templates/")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

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
async def vigenere(filepath: str = Form(...), key: str = Form(...), encrypt: bool = Form(...), base64: bool = Form(...)) -> dict:
    
    text = ""

    try:
        with open(filepath,"r") as textfile:
            text = textfile.read()
    except:
        return {"error" : "Invalid file or filepath!"}

    if encrypt:

        ciphertext = ciphertext if not base64 else cipher.base64Encrypt(ciphertext)

        return {"ciphertext" : ciphertext}
    
    else:

        plaintext = cipher.vigenereDecrypt((text if not base64 else cipher.base64Decrypt(text)),key)
    
        return {"plaintext" : plaintext}

@app.post("/vigenereextended")
async def vigenereextended(text: str = Form(...), key: str = Form(...), encrypt: bool = Form(...), base64: bool = Form(...)) -> dict:
    
    if encrypt:

        ciphertext = cipher.vigenereExtendedEncrypt(text,key)

        return {"ciphertext" : ciphertext}
    
    else:

        plaintext = cipher.vigenereExtendedDecrypt(text,key)
    
        return {"plaintext" : plaintext}

@app.post("/vigenereextended/file")
async def vigenereextended(filepath: str = Form(...), destinationfilepath: str = Form(...), key: str = Form(...), encrypt: bool = Form(...), base64: bool = Form(...)) -> dict:
    
    text = ""

    try:
        bytefile = open(filepath,"rb")
    except:
        return {"error" : "Invalid file or filepath!"}

    if encrypt:

        ciphertext = cipher.vigenereExtendedEncryptBytes(bytefile,key)

        with open(destinationfilepath, "wb") as binary_file:
        
            binary_file.write(ciphertext) 
        
        bytefile.close()

        return {"saved" : destinationfilepath}
    
    else:

        plaintext = cipher.vigenereExtendedDecryptBytes(bytefile,key)

        with open(destinationfilepath, "wb") as binary_file:
        
            binary_file.write(plaintext) 

        bytefile.close()
    
        return {"saved" : destinationfilepath}

@app.post("/playfair")
async def playfair(txt: str = Form(...), key: str = Form(...), encrypt: bool = Form(...), base64: bool = Form(...)) -> dict:
    
    if encrypt:

        ciphertext = cipher.playfairEncrypt(text,key)
        ciphertext = ciphertext if not base64 else cipher.base64Encrypt(ciphertext)

        return {"ciphertext" : ciphertext}
    
    else:

        plaintext = cipher.playfairDecrypt((text if not base64 else cipher.base64Decrypt(text)),key)
    
        return {"plaintext" : plaintext}
    
@app.post("/playfair/file")
async def playfair(filepath: str = Form(...), key: str = Form(...), encrypt: bool = Form(...), base64: bool = Form(...)) -> dict:
    
    text = ""

    try:
        with open(filepath,"r") as textfile:
            text = textfile.read()
    except:
        return {"error" : "Invalid file or filepath!"}

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
async def vigereautokey(filepath: str = Form(...), key: str = Form(...), encrypt: bool = Form(...), base64: bool = Form(...)) -> dict:
    
    text = ""

    try:
        with open(filepath,"r") as textfile:
            text = textfile.read()
    except:
        return {"error" : "Invalid file or filepath!"}

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
async def product(filepath: str = Form(...), vigenere_key: str = Form(...), transposition_key: int = Form(...), encrypt: bool = Form(...), base64: bool = Form(...)) -> dict:
    
    text = ""

    try:
        with open(filepath,"r") as textfile:
            text = textfile.read()
    except:
        return {"error" : "Invalid file or filepath!"}

    if encrypt:

        ciphertext = cipher.productEncrypt(text,vigenere_key,transposition_key)
        ciphertext = ciphertext if not base64 else cipher.base64Encrypt(ciphertext)

        return {"ciphertext" : ciphertext}
    
    else:

        plaintext = cipher.productDecrypt((text if not base64 else cipher.base64Decrypt(text)),vigenere_key,transposition_key)
    
        return {"plaintext" : plaintext}
    
@app.post("/affine")
async def affine(text: str = Form(...), m: int = Form(...), b: int = Form(...), encrypt: bool = Form(...), base64: bool = Form(...)) -> dict:
    
    # validasi hardcode soalnya kepepet waktu
    relprimes = [1,3,5,7,9,11,15,17,19,21,23,25]
    if (m <= 0 or m >= 26 or (m not in relprimes)):
        return {"error" : "M is not relatively prime with 26!"}

    if encrypt:

        ciphertext = cipher.affineEncrypt(text,m,b)
        ciphertext = ciphertext if not base64 else cipher.base64Encrypt(ciphertext)

        return {"ciphertext" : ciphertext}
    
    else:

        plaintext = cipher.affineDecrypt((text if not base64 else cipher.base64Decrypt(text)),m,b)
    
        return {"plaintext" : plaintext}

@app.post("/affine/file")
async def affine(filepath: str = Form(...) , m: int = Form(...), b: int = Form(...), encrypt: bool = Form(...), base64: bool = Form(...)) -> dict:
    
    text = ""

    try:
        with open(filepath,"r") as textfile:
            text = textfile.read()
    except:
        return {"error" : "Invalid file or filepath!"}

    if encrypt:

        ciphertext = cipher.affineEncrypt(text,m,b)
        ciphertext = ciphertext if not base64 else cipher.base64Encrypt(ciphertext)

        return {"ciphertext" : ciphertext}
    
    else:

        plaintext = cipher.affineDecrypt((text if not base64 else cipher.base64Decrypt(text)),m,b)
    
        return {"plaintext" : plaintext}
    