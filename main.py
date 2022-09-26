import fastapi
import uvicorn

print("Hello FastAPI")

api = fastapi.FastAPI()
# Use ALT+Enter for context help
# api = FastAPI()

@api.get("/")
def index():
    return {"msg" : "Hello from FastAPI",
            "another msg": ["Hello" , "World"]}

uvicorn.run(api, port=5496)