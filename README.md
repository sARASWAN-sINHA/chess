# Steps


To get the project up and running, follow these steps.

1. Create a docker image using the docker build command.<br>
   ```$ docker build -t name_of_your_image . ```

3. Once your docker image is ready, create a container using that docker image. Use the docker run command.<br>
   ```$ docker run -p 8000:8000 name_of_your_image```

4. Once your container is running, you can now test the APIs, on any API platform, like Postman, Insomnia or  


# Endpoints.

  a. __localhost:8080/chess/queen__ [GET]
         <br>
         &nbsp;&nbsp; Returns the valid positions of the queen.
         <br >
   ```
   {
    "positions": {
        "Queen": "H1",
        "Bishop": "B7",
        "Rook": "H8",
        "Knight": "F2"
    }
}
```
  b. __localhost:8000/chess/rook__ [GET]
  <br>
  &nbsp;&nbsp;returns the valid positions of the rook.
  <br>
  ```
{
    "positions": {
        "Queen": "A5",
        "Bishop": "G8",
        "Rook": "H5",
        "Knight": "G4"
    }
}
```
  c. __localhost:8000/chess/knight__ [GET]
  <br>
  &nbsp; &nbsp;Returns the valid positions of the knight. 
  <br>
  ```
{
    "positions": {
        "Queen": "E7",
        "Bishop": "B7",
        "Rook": "G5",
        "Knight": "C3"
    }
}
```


