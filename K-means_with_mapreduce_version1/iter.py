##Run MRKmeans until Centroids converge. 
##There is an small encoding problem in our real data test thus we decided to use 
##shell script to finish the iteration job. 

from mrjob.job import MRJob
from kmeans import MRKMeans
import sys
import os.path
import shutil
from math import sqrt

input_c = "centroids.txt"

CENTROIDS_FILE="tmp_centroids.txt"

def get_c(job, runner):
	c = []
	for line in runner.stream_output():
	    key, value = job.parse_output_line(line)
	    c.append(key)
	return c

def get_first_c(fname):
	f = open(fname,'r')
	centroids=[]
	for line in f.read().split('\n'):
		if line:
			x,y = line.split(',')
			centroids.append([float(x),float(y)])
	f.close()
	return centroids

def write_c(centroids):
	f = open(CENTROIDS_FILE, "w")
	centroids.sort()
	for c in centroids:
	    k,cx,cy = c.split(',')
	    #print c
	    f.write("%s,%s"%(cx,cy))
	f.close()

def dist_vec(v1,v2):
	return sqrt((v2[0]-v1[0])*(v2[0]-v1[0])+(v2[1]-v1[1])*(v2[1]-v1[1]))

def diff(cs1,cs2):
	max_dist = 0.0
	for i in range(3):
	    dist = dist_vec(cs1[i],cs2[i])
	    if dist > max_dist:
	        max_dist = dist
	
	return max_dist
 
if __name__ == '__main__':

	args = sys.argv[1:]
	if not os.path.isfile(CENTROIDS_FILE):
	    shutil.copy(input_c,CENTROIDS_FILE)

	old_c = get_first_c(input_c)
	
	i=1 
	while True:
	    print "Iteration #%i" % i
	mr_job=MRKMeans(args=args + ['--c='+CENTROIDS_FILE])
	
	with mr_job.make_runner() as runner:
		runner.run()
		centroids = get_c(mr_job,runner)

		write_c(centroids)
		n_c = get_first_c(CENTROIDS_FILE)
		max_d = diff(n_c,old_c)
		#print "dist max = "+str(max_d)
		if max_d < 0.01:
			break
		else:
			old_c = n_c
	i=i+1