# Use the LinuxServer.io Firefox image which provides a web-based GUI
FROM ghcr.io/linuxserver/firefox:latest

# Render uses port 10000 by default for external traffic
# We map the internal KasmVNC port (3000) to Render's required port
ENV PORT=10000
EXPOSE 10000

# Set the timezone to Singapore as requested
ENV TZ=Asia/Singapore

# PUID and PGID 1000 are standard for non-root users in these containers
ENV PUID=1000
ENV PGID=1000

# Configure the internal service to run on Render's expected port
# This ensures the web interface is what you see when you visit the URL
ENV CUSTOM_PORT=10000
