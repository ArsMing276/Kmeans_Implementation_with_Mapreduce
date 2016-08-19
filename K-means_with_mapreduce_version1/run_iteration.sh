#!/bin/bash

$iteration = 1
python MRKMeans.py data.txt --c centroids.txt >centroids1.txt


for iteration in $(seq 5)
do
   python MRKMeans.py data.txt --c centroids.txt >centroids$iteration.txt
done


