from fastapi import FastAPI
from mangum import Mangum
from routes import file

app = FastAPI(title='Provas POSCOMP', version='0.1.0')
app.include_router(file.router)

handler = Mangum(app)
