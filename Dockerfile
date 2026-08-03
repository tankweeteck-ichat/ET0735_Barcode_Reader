###############################################################################
# Raspberry Pi 4
# Raspberry Pi OS Bullseye (32-bit)
###############################################################################

FROM arm32v7/debian:bullseye

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

###############################################################################
# Install Python
###############################################################################

RUN apt-get update && \
    apt-get install -y \
        python3 \
        python3-pip \
        python3-dev \
        python3-setuptools \
        python3-wheel \
        && rm -rf /var/lib/apt/lists/*

###############################################################################
# Add Raspberry Pi Repository
###############################################################################

RUN apt-get update && \
    apt-get install -y wget gnupg ca-certificates

RUN wget https://archive.raspberrypi.org/debian/raspberrypi.gpg.key -O /tmp/rpi.gpg && \
    apt-key add /tmp/rpi.gpg

RUN echo "deb http://archive.raspberrypi.org/debian bullseye main" > /etc/apt/sources.list.d/raspi.list

###############################################################################
# Install Raspberry Pi Camera Packages
###############################################################################


RUN apt-get update && \
    apt-get install -y \
        python3-picamera2 \
        python3-libcamera \
        python3-opencv \
        python3-pyzbar \
        libcamera0 \
        libcamera-apps \
        libcamera-tools \
        libzbar0 \
        libgtk-3-0 \
        libcanberra-gtk3-module \
        x11-apps \
        && rm -rf /var/lib/apt/lists/*



###############################################################################
# Copy source
###############################################################################

COPY . .

CMD ["python3","barcode_reader.py"]
