FROM python:3

# https://stackoverflow.com/questions/154443/how-to-avoid-pyc-files
ENV PYTHONDONTWRITEBYTECODE=1

# ARG TIMEZONE
# ENV TIMEZONE=${TIMEZONE}
# RUN ln -snf /usr/share/zoneinfo/$TIMEZONE /etc/loPPDIR=/appcaltime \
#   && echo $TZ > /etc/timezone

ENV APPDIR=/app
ENV TGTDIR=${APPDIR}/src

# RUN apt update \
#   && apt install -y cifs-utils \
#   && rm -rf /var/lib/apt/lists/*

# target directories are created automatically if they don't already exist
COPY *.py *.txt *.sh ${TGTDIR}/
RUN pip install --no-cache-dir -r ${TGTDIR}/requirements.txt

WORKDIR ${APPDIR}
CMD [ "/bin/bash" ]
