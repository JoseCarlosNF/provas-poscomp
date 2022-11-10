from fastapi import APIRouter
from fastapi.datastructures import UploadFile
from fastapi.responses import FileResponse
from models.file import FileType
from repository.aws_s3 import S3

router = APIRouter(prefix='/file')
s3 = S3()


@router.post('', tags=['file'], status_code=201)
def enviar_arquivo(ano: str, tipo: FileType, upload_file: UploadFile):
    s3.upload(upload_file, ano, tipo.value)
    return {'message': 'Arquivo enviado com sucesso.'}


@router.get('', tags=['file'], status_code=200)
def baixar_arquivo(ano: str, tipo: FileType):
    temp_file_path = s3.download(ano, tipo.value)
    return FileResponse(path=temp_file_path, media_type='application/pdf')


@router.get('/ls', tags=['file'], status_code=200)
def listar_arquivos_disponiveis():
    return s3.list()
