import uvicorn
from app.main import sio_app

from requests import get

ipv6_address = get('https://ip6.seeip.org/').text

if __name__ == "__main__":
    uvicorn.run(
        'app.main:sio_app', 
        host=ipv6_address, 
        port=8049, 
        # reload=True,
        log_level='info')
