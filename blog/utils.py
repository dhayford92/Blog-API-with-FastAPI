import os
import secrets
from fastapi import File, HTTPException




async def upload_file(filedir, filename: File(...)):
    filepath = f'media/{filedir}/'
    
    extension = filename.filename.split('.')[1]
    if not extension in ['jpg', 'jpeg', 'png']:
        raise HTTPException(status_code=400, detail='File extension not supported')
    
    generate_filename = secrets.token_hex(10)
    
    new_file = generate_filename+'.'+ extension
    new_file_path = filepath + new_file
    
    file_content = await filename.read()
    with open(new_file_path, 'wb') as f:
        f.write(file_content)
        
    return new_file_path



def remove_file(file_path: str):
    if os.path.exists(file_path):
        os.remove(file_path)     