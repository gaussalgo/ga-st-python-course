
localhost
---------

.. code-block:: shell

    docker compose up
    xdg-open 'http://localhost:9000/'

    System / Inputs / Select input (GELF TCP)
    echo -n -e '{ "version": "1.1", "host": "example.org", "short_message": "A short message 2", "level": 5, "_some_info": "foo" }'"\0" | nc -w0 localhost 12201

    System / Inputs / Select input (GELF HTTP)
    curl -X POST -H 'Content-Type: application/json' -d '{ "version": "1.1", "host": "example.org", "short_message": "A short message", "level": 5, "_some_info": "foo" }' 'http://localhost:12201/gelf'


AWS EC2 virtual
---------------


Setup DNS CNAME graylog.gaussalgo.com

    ec2-52-17-3-161.eu-west-1.compute.amazonaws.com

.. code-block:: shell

    ssh -i secrets/python-training.pem -l rocky graylog.gaussalgo.com

        sudo yum install -y bash less vim curl wget nmap traceroute net-tools openssh-clients telnet strace bind-utils mc && yum clean all

        sudo yum install -y yum-utils
        sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
        sudo yum install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
        sudo systemctl enable docker
        sudo systemctl start docker
        sudo docker run hello-world

        sudo yum -y install docker wget
        curl -s https://api.github.com/repos/docker/compose/releases/latest | grep browser_download_url | grep docker-compose-linux-x86_64 | cut -d '"' -f 4 | wget -qi -
        chmod +x docker-compose-linux-x86_64
        sudo mv docker-compose-linux-x86_64 /usr/local/bin/docker-compose
        docker-compose --version
            Docker Compose version v2.16.0

        mkdir -p /home/rocky/graylog

.. code-block:: shell

    scp -i secrets/python-training.pem docker-compose.yml .env rocky@graylog.gaussalgo.com:/home/rocky/graylog/

    ssh -i secrets/python-training.pem -l rocky graylog.gaussalgo.com
        cd /home/rocky/graylog
        sudo /usr/local/bin/docker-compose -f docker-compose.yml up -d

.. code-block:: shell

    xdg-open 'http://graylog.gaussalgo.com:9000/'
    # admin / thisisasecret



Setup tunning

1) Start input stream

    System / Inputs / Select input (GELF TCP)

.. code-block:: shell

    curl -i -X POST -H 'Content-Type: application/json' -d '{ "version": "1.1", "host": "example.org", "short_message": "A short message", "level": 5, "_some_info": "foo" }' 'http://graylog.gaussalgo.com:12201/gelf'

2) Add read-only reader

    System / Users and Teams
        Rocky
        Readonly
        rocky
        polcar+graylog-plebz@gaussalgo.com
        ✔️ Session do not time out
        Time Zone: Prague
        Assign Roles: vsechno krome "Admin"
        <see `secrets/access.txt`>

3) Share default stream to read-only user

    Streams

        Default Stream
            +Share -> Everyone -> Viewer


Perfrom restart

.. code-block:: shell

    ssh -i secrets/python-training.pem -l rocky graylog.gaussalgo.com sudo reboot
