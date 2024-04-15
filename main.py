import uvicorn
from fastapi import FastAPI


from APIComponents.blog import Blog


app = FastAPI()

@app.get("/")
def index():
    return {'data': 'Data As API'}


@app.get("/blog/{id}")
def show_blog(id: int):
    return {'data': id}


@app.get("/blog/{id}/comments")
def comments(id: int):
    return {
            'data': {
                    'comments': ['comment']
                    }
            }


@app.post("/create-blog")
def create_blog(blog: Blog):
    return {'blog': blog}



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)