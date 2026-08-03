Information about this repository

=================================

This is the docker container that is able to use the picamera to read barcode.

To re-build the docker image, use command:

docker compose build



The name of the docker image is specified in the docker-compose.yml file, by
the line:
image: raspberrypi-barcode:v1



To run the docker container, use the two commands:

xhost +SI:localuser:root


docker compose up



The first command is to grant access permission of the display to the root user.
When the container runs, it runs as the root user. However, the Rasp Pi setting is
limiting access right to the X11 only to pi user. The first command adds root
user to the account list that has permission to access the x11. The first
command is only needed to be run one time only after the Rasp Pi boots up.



The second command is the one that actually launch the container.



S

