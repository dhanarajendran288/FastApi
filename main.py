from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import userDetails

app = FastAPI()


@app.get('/')
def home():
    return {
            'statusCode': 1,
            'response': 'Api Running Successfully'
            }


app.include_router(userDetails.router)


origins = ['*']

app.add_middleware(CORSMiddleware, 
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])