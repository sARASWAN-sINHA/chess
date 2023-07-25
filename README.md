# Steps


To get the project up and running, follow the steps.

1. Create a docker image using the docker build command.
   ```$ docker build -t name_of_your_image . ```

3. Once your docker image is ready, create a container using that docker image. Use the docker run command.
   ```$ docker run -p 8000:8000 name_of_your_image```

4. Once your container is running, you can now test the APIs. 


# Endpoints.

  a. localhost:8080/chess/queen -> returns the valid positions of the queen.
  b. localhost:8000/chess/rook -> returns the valid positions of the rook.
  c. localhost:8000/chess/knight -> returns the valid positions of the knight.


