#!/bin/sh
conda create -n rates python=3.10
conda activate rates
pip install -r requirements.txt
python main.py