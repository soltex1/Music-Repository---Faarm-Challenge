# Music-Repository---Faarm-Challenge


**Database Engine:** MySQL

**Models:** Album, Genre, Lending, Track, Artist

**Actions:** CRUD for models Album, Genre and Lending

**Rest API's:** Album and Genre

## Album Rest API EndPoints [GET, PUT and POST]:

Get all albums:
```
http://127.0.0.1:8000/api/v1/albums
eg: curl -X GET http://127.0.0.1:8000/api/v1/albums -H "Content-Type: application/json"
```
Get all favorite albums:
```
http://127.0.0.1:8000/api/v1/albums/favorites
eg: curl -X GET http://127.0.0.1:8000/api/v1/albums/favorites -H "Content-Type: application/json"
```
Get all albums lent:
```
http://127.0.0.1:8000/api/v1/albums/lent
eg: curl -X GET http://127.0.0.1:8000/api/v1/albums/lent -H "Content-Type: application/json"
```
Get all available albums (that aren't lent):
```
http://127.0.0.1:8000/api/v1/albums/available
eg: curl -X GET http://127.0.0.1:8000/api/v1/albums/available -H "Content-Type: application/json"
```
Get album by id:
```
http://127.0.0.1:8000/api/v1/album/:id/
eg: curl -X GET http://127.0.0.1:8000/api/v1/album/16/ -H "Content-Type: application/json"
```
Post new album:
```
http://127.0.0.1:8000/api/v1/albums
eg: curl -X POST http://127.0.0.1:8000/api/v1/albums -d '{"lending":"16","title":"new album 001","a_date":"1931-04-16T00:00:00Z","c_date":"2017-04-18T16:02:29.406452Z","favorite":false,"n_songs":10,"description":"C","genres":[11],"types":"ps"}' -H "Content-Type: application/json"
```
Update album via id:
```
http://127.0.0.1:8000/api/v1/album/:id/
eg: curl -X PUT http://127.0.0.1:8000/api/v1/album/27/ -d '{"title": "new album 005"}' -H "Content-Type: application/json"
```
Change album lending value (key must be lending and value equal to album id to be true and false to be false):
```
http://127.0.0.1:8000/api/v1/album/:id/
eg: curl -X PUT http://127.0.0.1:8000/api/v1/album/27/ -d  '{"lending": "17"}' -H "Content-Type: application/json"
eg: curl -X PUT http://127.0.0.1:8000/api/v1/album/27/ -d  '{"lending": "false"}' -H "Content-Type: application/json"
```
Change album favorite value (key favorite must have the value true or false)
```
http://127.0.0.1:8000/api/v1/album/:id/
eg: curl -X PUT http://127.0.0.1:8000/api/v1/album/27/ -d '{"favorite": "false"}' -H "Content-Type: application/json"
eg: curl -X PUT http://127.0.0.1:8000/api/v1/album/27/ -d '{"favorite": "true"}' -H "Content-Type: application/json"
```