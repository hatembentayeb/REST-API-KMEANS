# REST-API-KMEANS
A simple demo of kmeans clustering on text input via REST API based on flask µ-server. -( ISITCOM-DATA-SCIENCE-CLUB )-

#### Building the Docker image 

To build the docker image use this command:

   * `git clone https://github.com/hatemBT/REST-API-KMEANS`
   * `cd REST-API-KMEANS`
   * `docker build -t kmeans-rest .`

After buiding the image check it by typing ` docker images `

#### Running the Image 

Inside the docker container flask work at port `3000`, so we have to expose it outside the container buy doing this :

`docker run -p 3000:3000 -t  kmeans-rest `

note that `run` will execute the container
          `-p` will map the 3000 port ouside the container to port 3000 inside the container
          `-t` just a pretty output

#### Testing the image

We will use `curl` to test the `/predict` route, let's type the command :

`curl -X POST -H "Content-Type: application/json" "http://localhost:3000/predict" -d @data.json | jq "."`

note that `-X POST` is the request method
          `-H ...` the Header that specify the data type (json in our case)
          `http://...` is our target url to point to the container (flask server)
          `-d @..` is the data to be sent to the flask server via a post method
          
`jq "." ` is json query to get a pretty output


this a sample output :

```bash 

Ξ datascience-opening/REST-API-KMEANS git:(master) ▶ curl -X POST -H "Content-Type: application/json" "http://localhost:4000/predict" -d @data.json | jq "."
zsh: correct '@data.json' to 'data.json' [nyae]? n
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   842  100   237  100   605  11850  30250 --:--:-- --:--:-- --:--:-- 42100
{
  "cluster_0": [
    "works",
    "set",
    "best",
    "conditions",
    "given",
    "learning",
    "machine",
    "algorithm",
    "try",
    "decision"
  ],
  "cluster_1": [
    "use",
    "algorithm",
    "condition",
    "regression",
    "categorical",
    "variable",
    "dependent",
    "linear",
    "superior",
    "requirements"
  ]


```