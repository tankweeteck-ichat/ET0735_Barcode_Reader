<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Raspberry Pi Barcode Reader</title>
<style>
body{font-family:Arial,Helvetica,sans-serif;line-height:1.65;color:#1f2937;background:#f5f7fa;margin:0}
.container{max-width:950px;margin:35px auto;padding:45px 55px;background:#fff;border-radius:14px;box-shadow:0 4px 18px rgba(0,0,0,.1)}
h1{text-align:center;color:#2E86C1} h2{border-bottom:2px solid #d9e0e7;padding-bottom:7px;margin-top:38px}
.overview,.build{color:#28B463}.run{color:#E67E22}.stop{color:#C0392B}.rebuild{color:#8E44AD}.summary{color:#16A085}.image{color:#2E86C1}
.subtitle{text-align:center;font-size:1.08rem}
code{font-family:Consolas,"Courier New",monospace;background:#eef2f6;padding:2px 5px;border-radius:4px}
pre{background:#20252b;color:#f4f7fa;padding:18px 20px;border-radius:8px;overflow-x:auto;border-left:5px solid #2E86C1}
pre code{background:transparent;padding:0;color:inherit}
.note,.important{padding:15px 18px;border-radius:7px;margin:18px 0}
.note{background:#fff8df;border-left:5px solid #e0a800}.important{background:#fdecea;border-left:5px solid #C0392B}
table{width:100%;border-collapse:collapse}th,td{border:1px solid #d9e0e7;padding:11px 13px;text-align:left}th{background:#16A085;color:white}tr:nth-child(even){background:#f7f9fb}
footer{text-align:center;margin-top:42px;padding-top:20px;border-top:1px solid #d9e0e7;font-weight:bold;color:#52606d}
</style>
</head>
<body><div class="container">
<h1>📷 Raspberry Pi Barcode Reader</h1>
<p class="subtitle"><strong>A Docker-based barcode reader using the Raspberry Pi Camera</strong></p>

<h2 class="overview">📋 Overview</h2>
<p>This repository contains a <strong>Docker-based barcode reader application</strong> designed for the <strong>Raspberry Pi</strong>.</p>
<p>The application uses the Raspberry Pi Camera (<code>Picamera</code>) to capture images and detect barcodes. The barcode reader application is packaged and executed inside a Docker container.</p>

<h2 class="build">🔧 Build the Docker Image</h2>
<p>To rebuild the Docker image, open a terminal in the project directory and run:</p>
<pre><code>docker compose build</code></pre>
<p>The Docker image name is specified in the <code>docker-compose.yml</code> file:</p>
<pre><code>image: raspberrypi-barcode:v1</code></pre>
<p>Therefore, the Docker image created by the build process is:</p>
<pre><code>raspberrypi-barcode:v1</code></pre>

<h2 class="run">🚀 Run the Docker Container</h2>
<p>Before starting the container, run:</p>
<pre><code>xhost +SI:localuser:root</code></pre>
<p>Then start the Docker container:</p>
<pre><code>docker compose up</code></pre>

<h3>🖥️ Step 1: Grant X11 Display Access</h3>
<p>The following command grants the <code>root</code> user permission to access the Raspberry Pi's X11 display:</p>
<pre><code>xhost +SI:localuser:root</code></pre>
<p>The Docker container runs as the <code>root</code> user by default. However, the Raspberry Pi desktop's X11 display is normally accessible only to the logged-in desktop user, such as <code>pi</code>.</p>
<p>Therefore, the <code>xhost</code> command allows GUI applications running as <code>root</code> inside the Docker container to display windows on the Raspberry Pi desktop.</p>
<div class="note"><strong>Note</strong><ul><li>This command normally needs to be run only once after the Raspberry Pi boots.</li><li>It may need to be run again after restarting or rebooting the Raspberry Pi.</li><li>It may also need to be run again after logging out or starting a new X11 desktop session.</li></ul></div>

<h3>▶️ Step 2: Start the Container</h3>
<p>Run:</p><pre><code>docker compose up</code></pre>
<p>This command creates and starts the Docker container using the configuration defined in <code>docker-compose.yml</code>. The container then starts the barcode reader application.</p>

<h2 class="stop">🛑 Stop the Container</h2>
<p>When <code>docker compose up</code> is running in the foreground, press:</p><pre><code>Ctrl+C</code></pre>
<p>to stop the container. Alternatively, open another terminal and run:</p><pre><code>docker compose down</code></pre>
<p>This command stops and removes the container created by Docker Compose.</p>
<div class="important"><strong>Important:</strong> The Docker image is <strong>not removed</strong> by <code>docker compose down</code>.</div>

<h2 class="rebuild">🔄 Rebuild and Run</h2>
<p>After modifying the application source code or the <code>Dockerfile</code>, rebuild the image and start the container using:</p>
<pre><code>docker compose up --build</code></pre>
<p>This command:</p><ol><li>Rebuilds the Docker image</li><li>Creates the container if it does not already exist</li><li>Starts the barcode reader application</li></ol>

<h2 class="summary">📌 Command Summary</h2>
<table><thead><tr><th>Purpose</th><th>Command</th></tr></thead><tbody>
<tr><td>Build the Docker image</td><td><code>docker compose build</code></td></tr>
<tr><td>Grant X11 access to the container's <code>root</code> user</td><td><code>xhost +SI:localuser:root</code></td></tr>
<tr><td>Start the container</td><td><code>docker compose up</code></td></tr>
<tr><td>Rebuild the image and start the container</td><td><code>docker compose up --build</code></td></tr>
<tr><td>Stop the foreground container</td><td><code>Ctrl+C</code></td></tr>
<tr><td>Stop and remove the Compose container</td><td><code>docker compose down</code></td></tr>
</tbody></table>

<h2 class="image">🐳 Docker Image</h2>
<p>The Docker image name is:</p><pre><code>raspberrypi-barcode:v1</code></pre>
<p>The image name is configured in the <code>docker-compose.yml</code> file.</p>
<footer>Raspberry Pi • Docker • Picamera • Barcode Reader</footer>
</div></body></html>