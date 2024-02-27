from fastapi.responses import StreamingResponse, FileResponse
from fastapi.templating import Jinja2Templates

from Backend.app import api

from util import read_file, write_file

app = FastAPI()
templates = Jinja2Templates(directory="Frontend/templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})