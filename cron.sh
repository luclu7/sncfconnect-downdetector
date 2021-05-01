#!/usr/bin/env bash
cd /root/moncompte-downdetector
export PATH=$PATH:$PWD/lib
./sncf-connect-downdetector.py >> debug.log
