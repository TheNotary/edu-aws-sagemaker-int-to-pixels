from fastapi import FastAPI, Query
from starlette.responses import FileResponse 

from int_to_pixels.int_to_pixels import predict_pixels

app = FastAPI()

@app.get("/")
async def read_index():
    return FileResponse('index.html')

@app.get("/script.js")
async def read_index():
    return FileResponse('script.js')

@app.get("/styles.css")
async def read_index():
    return FileResponse('styles.css')

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse("favicon.ico")

@app.get("/pixels")
async def hello_world(number: int = Query(..., gt=-1, lt=10, description="The number you'd like an array of pixels for")):
    pixel_grid = predict_pixels(number)
    
    print("finished predicting pixels")
    return {"pixels": pixel_grid}
