# Use existing Node Red container
FROM cunlifs/ubuntu:v0.5
LABEL maintainer="Andrew Laidlaw [andrew.laidlaw@uk.ibm.com]"

# Create the user for Node Red
RUN useradd -m -l -d /usr/src/node-red -u 1000730033 -g 0 nodered -p abc1234

# Copy source files into the container
COPY bond-films-flow.json /usr/src/node-red/bond-films-flow.json
COPY package.json /usr/src/node-red/package.json

# Expose default Node Red port
EXPOSE 1880/tcp

# Set permissions
RUN chmod 750 /usr/src/node-red/bond-films-flow.json
RUN chmod 777 /usr/src/node-red

# Proxy settings only needed for our local environment, could be passed at build
ENV http_proxy http://9.196.156.29:3128
ENV https_proxy http://9.196.156.29:3128

# Create Python environment for scripts
RUN python3 -m venv /usr/src/node-red/venv --system-site-packages

# Set user and required environmetn variables
USER nodered
ENV HOME /usr/src/node-red
WORKDIR /usr/src/node-red

# Run Node Red including our predefined flows
CMD node-red /usr/src/node-red/bond-films-flow.json
