# Kmeans_Implementation_with_Mapreduce

In a 'big data' environment with millions of records, direcly apply kmeans would be time consuming no matter in what language. In this project, we want to parallize the kmeans algorithm with mapreduce. This approach may also be applicable to other clustering or Expectation-Maximization optimized algorithms.

1. Deployed Hadoop ecosystem with Cloudera Manager and Hortonworks Sandbox on multiple nodes.
2. Randomly generated three data clusters. Each cluster has a huge amount of data and is multivariate normal distributed.
3. Wrote Parallel K-means MapReduce code with mrjob in Python. Mapper calculates distances between points and
centroids and update class labels, Reducer aggregate data points from each updated class and calculate mean as new
centroid. Used mrjob steps function to iterate this process until centroids converge.
4. Executed the MapReduce code on both single node and multiple nodes and compared their performances.
