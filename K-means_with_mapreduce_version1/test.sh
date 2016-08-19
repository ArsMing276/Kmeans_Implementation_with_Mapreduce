#!/usr/bin/env bash

$iteration = 1
python MRKMeans.py data.txt --c centroids.txt >centroids1.txt

$nextiteration = 1
for iteration in $(seq 5)
do
   $nextiteration = $iteration +1
   python MRKMeans.py data.txt --c centroids$iteration.txt >centroids$nextiteration.txt
done