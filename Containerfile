FROM rockylinux:9.3.20231119-minimal
RUN dnf install python3 -y 
RUN python3 setup.py install 
CMD /bin/bash
