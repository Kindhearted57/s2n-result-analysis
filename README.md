This repo contains the scripts for analyzing the results from mutation testing on Amazon S2N-TLS

To setup seaborn:

```
apt-get install libjpeg-dev zlib1g-dev python3-pip

pip3 install seaborn
```
## seed_distribution.py

This has to be used inside the server as it takes file creation time as input.

(Remember to change the survival path dir)

x-axis -> the time gap between the first seed and the current seed

y-axis -> the number of seed (cumulative)


