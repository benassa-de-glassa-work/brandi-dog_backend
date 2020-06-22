import uvicorn
from app.main import sio_app


if __name__ == "__main__":
    uvicorn.run(
        'app.main:sio_app', 
        host="2a04:ee41:3:b127:f7a3:1ea5:2c09:ef42", 
        port=8049, 
        # reload=True,
        log_level='info')
