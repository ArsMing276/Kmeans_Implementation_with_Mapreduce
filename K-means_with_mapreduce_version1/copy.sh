#!/usr/bin/env bash
set -x
trap read debug

python MRKMeans.py data.txt --c centroids.txt >centroids1.txt
python MRKMeans.py data.txt --c centroids1.txt >centroids2.txt
python MRKMeans.py data.txt --c centroids2.txt >centroids3.txt
python MRKMeans.py data.txt --c centroids3.txt >centroids4.txt
python MRKMeans.py data.txt --c centroids4.txt >centroids5.txt
python MRKMeans.py data.txt --c centroids5.txt >centroids6.txt
python MRKMeans.py data.txt --c centroids6.txt >centroids7.txt
python MRKMeans.py data.txt --c centroids7.txt >centroids8.txt
python MRKMeans.py data.txt --c centroids8.txt >centroids9.txt
python MRKMeans.py data.txt --c centroids9.txt >centroids10.txt
python MRKMeans.py data.txt --c centroids10.txt >centroids11.txt
