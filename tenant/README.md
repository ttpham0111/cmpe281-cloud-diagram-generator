docker build -t backend .

docker rm -f backend;
docker run --name backend
           -d
           -p 5001:5000
           -e SECRET_KEY=\xf7\xa4\x91n}\x14\n\xf1\x9cN\xb7\xfdO\xc2\xc5aY\xe7\x14\xfd\xb4f\x90\xdf 
           -e TEMP_DIR=/tmp
           -e CREATE_DIAGRAM_COMMAND="java -cp /app/app/resources/* -Dzanthan.prefs=/app/app/resources/diagram.preferences -jar /app/app/resources/sequence.jar --headless {}"
           -e OUTPUT_EXT=".png"
           -e INPUT_EXT=".seq"
           backend &&
docker logs -f backend

docker rm -f backend;
docker run --name backend
           -d
           -p 5001:5000
           -e SECRET_KEY=\xf7\xa4\x91n}\x14\n\xf1\x9cN\xb7\xfdO\xc2\xc5aY\xe7\x14\xfd\xb4f\x90\xdf 
           -e TEMP_DIR=/tmp
           -e CREATE_DIAGRAM_COMMAND="java -cp /app/app/resources/UmlGraph.jar:/app/app/resources/commons-logging-1.0.
3.jar org.umlgraph.doclet.UmlGraph {} png"
           -e OUTPUT_EXT=".png"
           -e INPUT_EXT=".java"
           backend &&
docker logs -f backend


docker rm -f backend;
docker run --name backend
           -d
           -p 5001:5000
           -e SECRET_KEY=\xf7\xa4\x91n}\x14\n\xf1\x9cN\xb7\xfdO\xc2\xc5aY\xe7\x14\xfd\xb4f\x90\xdf 
           -e MODE=file
           -e TEMP_DIR=/tmp
           -e CREATE_DIAGRAM_COMMAND="java -jar /app/app/resources/ProjectUml.jar {} pic"
           -e OUTPUT_EXT=.jpeg
           backend &&
docker logs -f backend