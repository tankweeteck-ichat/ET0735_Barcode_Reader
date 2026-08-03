# 📷 Raspberry Pi Barcode Reader

> **A Docker-based barcode reader using the Raspberry Pi Camera**

---

## 📋 Overview

This repository contains a **Docker-based barcode reader application** designed for the **Raspberry Pi**.

The application uses the Raspberry Pi Camera (`Picamera`) to capture images and detect barcodes. The barcode reader application is packaged and executed inside a Docker container.

---

## 🔧 Build the Docker Image

To rebuild the Docker image, open a terminal in the project directory and run:

```bash
docker compose build
```

The Docker image name is specified in the `docker-compose.yml` file:

```yaml
image: raspberrypi-barcode:v1
```

Therefore, the Docker image created by the build process is:

```text
raspberrypi-barcode:v1
```

---

## 🚀 Run the Docker Container

Before starting the container, run:

```bash
xhost +SI:localuser:root
```

Then start the Docker container:

```bash
docker compose up
```

### 🖥️ Step 1: Grant X11 Display Access

The following command grants the `root` user permission to access the Raspberry Pi's X11 display:

```bash
xhost +SI:localuser:root
```

The Docker container runs as the `root` user by default. However, the Raspberry Pi desktop's X11 display is normally accessible only to the logged-in desktop user, such as `pi`.

Therefore, the `xhost` command allows GUI applications running as `root` inside the Docker container to display windows on the Raspberry Pi desktop.

> **Note**
>
> This command normally needs to be run only once after the Raspberry Pi boots. It may need to be run again after:
>
> - Restarting or rebooting the Raspberry Pi
> - Logging out of the Raspberry Pi desktop session
> - Starting a new X11 desktop session

### ▶️ Step 2: Start the Container

Run:

```bash
docker compose up
```

This command creates and starts the Docker container using the configuration defined in `docker-compose.yml`.

The container then starts the barcode reader application.

---

## 🛑 Stop the Container

When `docker compose up` is running in the foreground, press:

```text
Ctrl+C
```

to stop the container.

Alternatively, open another terminal and run:

```bash
docker compose down
```

This command stops and removes the container created by Docker Compose.

> **Important**
>
> The Docker image is **not removed** by `docker compose down`.

---

## 🔄 Rebuild and Run

After modifying the application source code or the `Dockerfile`, rebuild the image and start the container using:

```bash
docker compose up --build
```

This command:

1. Rebuilds the Docker image
2. Creates the container if it does not already exist
3. Starts the barcode reader application

---

## 📌 Command Summary

| Purpose | Command |
|---|---|
| Build the Docker image | `docker compose build` |
| Grant X11 access to the container's `root` user | `xhost +SI:localuser:root` |
| Start the container | `docker compose up` |
| Rebuild the image and start the container | `docker compose up --build` |
| Stop the foreground container | `Ctrl+C` |
| Stop and remove the Compose container | `docker compose down` |

---

## 🐳 Docker Image

The Docker image name is:

```text
raspberrypi-barcode:v1
```

The image name is configured in the `docker-compose.yml` file.

---

<p align="center">

**Raspberry Pi • Docker • Picamera • Barcode Reader**

</p>
