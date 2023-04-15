from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
# Creación de variable
movies = [
     {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    },
    {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    }
]

app = FastAPI() # Creación de intancia. Nombre de la aplicación.
app.title = "Mi aplicación con FastAPI" # Título
app.version = "0.0.1" 

class Movie(BaseModel):
    id: Optional[int] = None # Se asigna que sea un parámetro opcional con valor por defecto None
    title:str = Field( min_lengrh = 5, max_length=15) 
    overview:str = Field( min_lengrh = 15, max_length=50) 
    year: int = Field(le=2022) # Menor al 2022
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=5, max_length=15)

    class Config: # Se pone de manera más compacta el default. Los defaults sirven para dar guías de como dar los parámetros
        schema_extra = {
            "example": {
                "id":1,
                "title":"Mi película",
                "overview":"Descripción película",
                "year": "2022",
                "rating": 9.8,
                "category":"Acción"


            }                              
        }

# Creacón de rutas para inicio.Esto se usa para agrupar determinadas rutas en la aplicación
@app.get('/',tags = ['Home'])                               
def message():
    return HTMLResponse('<h1> Primer proyecto con FastAPI </h1>') # Retorna en formato HTML

# Creacón de rutas para películas
@app.get('/movies', tags = ['movies'], response_model=List[Movie])
def get_movies() -> List[Movie]: # Creación de función que me devuelve el listado

    return JSONResponse(content=movies)

# Para indicarle a una ruta que va a requerir de parámetros, se debe añadir la siguiente ruta de la siguiente manera:
# donde en llaves va el parámetro que se quiera consultar {parámetro}
@app.get('/movies/{id}',tags = ['movies'], response_model= Movie) 
# Luego se realiza el filtrado de la película mediante la función get_movie
def get_movie(id:int = Path(ge=1, le=2000) ) -> Movie:
    for item in movies:
        if item['id'] == id: 
            return JSONResponse(content=item)
    return JSONResponse(content=[])

# Uso de parámetros Query. Sirve para realizar búsqueda a partir de categorías
@app.get('/movies/',tags = ['movies'], response_model=List[Movie]) # Nota: cuando no se especifica en la url, se entiende automáticamente que se está usando un parámetro Query.
def get_movies_by_category(category:str = Query(min_length=5, max_length=15)) -> List[Movie]:
    data = [item for item in movies if item['category'] == category] # La función da listado de datos que coincidan con la categoría solicitada
    return JSONResponse(content=data)

@app.post('/movies',tags = ['movies'], response_model=dict) # Con Body() se indica que pertenecen al contenido de la petición
#Hace que permita modificar los datos, en este caso se van a añadir
#def create_movie(id:int = Body(), title:str= Body(), overview:str= Body(), year:int= Body(), rating:float= Body(), category:str= Body() ):
#
#    movies.append({
#        "id": id,
#        "title": title,
#        "overview": overview,
#        "year": year,
#        "rating": rating,
#        "category": category
#    })
#    return movies 

# Para no poner todos los parámetros de la función del método, se usa la clase Movies con el Método Basemodel.
# por tanto las líneas 64-74 pueden resumirse a:
def create_movie(movie: Movie) -> dict:
     movies.append(movie)
     return JSONResponse(content={"message": "Se ha reistrado la película"})


# Método que permite realizar modificaciones en la API.
@app.put('/movies/{id}', tags=['movies'],response_model=dict)
#def update_movie(id:int, title:str= Body(), overview:str= Body(), year:int= Body(), rating:float= Body(), category:str= Body() ):
#    for item in movies:
#        if item["id"] == id: # Por cada item de la lista de películas realiza un filtrado
#            item['title '] = title,
#            item['overview'] = overview,
#            item['year'] = year,
#            item['rating'] = rating,
#            item['category'] = category, 
#            return movies

#De igual manera, podemos sustituir las líneas 100-110 mediante:
def update_movie(id:int, movie: Movie) -> dict:
    for item in movies:
        if item["id"] == id: # Por cada item de la lista de películas realiza un filtrado
            item['title '] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category 
            return JSONResponse(content={"message": "Se ha modificado la película"})




# Método para eliminar datos
@app.delete('/movies/{id}', tags=['movies'], response_model=dict)
def delete_movie(id:int) -> dict:
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return JSONResponse(content={"message": "Se ha eliminado la película"})





