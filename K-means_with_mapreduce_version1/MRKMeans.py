#MRKmeans is an one step mapreduce job

from mrjob.job import MRJob
import mrjob
# MRJob is a python class which will be overloaded
from math import sqrt
from mr3px.csvprotocol import CsvProtocol

def write_c(centroids):
    f = open(CENTROIDS_FILE, "w")
    centroids.sort()
    for c in centroids:
        k,cx,cy = c.split(',')
        #print c
        f.write("%s,%s"%(cx,cy))
    f.close()

def get_c(job, runner):
    c = []
    for line in runner.stream_output():
        key, value = job.parse_output_line(line)
        c.append(key)
    return c


class MRKMeans(MRJob):

    SORT_VALUES = True
    #OUTPUT_PROTOCOL = mrjob.protocol.RawProtocol
    OUTPUT_PROTOCOL = mrjob.protocol.RawProtocol
    def dist_vec(self,v1,v2):
        #calculate the ditance between two vectors (in two dimensions)
        return sqrt((v2[0]-v1[0])*(v2[0]-v1[0])+(v2[1]-v1[1])*(v2[1]-v1[1]))
    
    def configure_options(self):
        super(MRKMeans, self).configure_options()
        #the line below define that the file folowing the --c option is the centroid and is loadable
        self.add_file_option('--c')

    def get_centroids(self):
        """
        Definition : extracts centroids from the centroids file define afetr --c flag
        Out : Return the list of centroids
        """
        # self.options.c is the name of the file following --c option
        f = open(self.options.c,'r')
        centroids=[]
        for line in f.read().split('\n'):
            #print line
            line = line.strip()
            if line:
                x,y = line.split(',')
                centroids.append([float(x),float(y)])

        f.close()
        #print centroids
        return centroids
    
    def mapper(self, _, lines):
        """
        Definition : Mapper take centroids extract form get_centroids() and the point cloud and for each point, calculate the distance to the centroids, find the mininum of it
        Out : yield the point with it's class
        """
        centroids = self.get_centroids()
        for l in lines.split('\n'):
            #print lines
            x,y = l.split(',')
            point = [float(x),float(y)]
        min_dist=100000000.0
        classe = 0
        #print centroids
        #iterate over the centroids (Here we know that we are doing a 3means)
        for i in range(3):
            dist = self.dist_vec(point,centroids[i])
            if dist < min_dist:
                min_dist = dist
                classe = i
        yield classe, point
        #print classe, point
    
    def combiner(self,k,v):
        """
        Definition : Calculate for each class, at the end of the mapper, before reducer, the medium point of each class
        Out: return for each class, the centroids for each mapper
        """
        count = 0
        moy_x=moy_y=0.0
        for t in v:
            count += 1
            moy_x+=t[0]
            moy_y+=t[1]
        yield k, (moy_x/count,moy_y/count)

    def reducer(self, k, v):
        """
        Definition : for each class, get all the tmp centroids from each combiner and calculate the new centroids.
        """
        # k is class and v are medium points linked to the class
        count = 0
        moy_x=moy_y=0.0
        #f = open('new_centroids' , 'w')
        for t in v:
            count += 1
            moy_x+=t[0]
            moy_y+=t[1]
        print str(moy_x/count)+","+str(moy_y/count)
        #.write(str(moy_x/count)+","+str(moy_y/count)
if __name__ == '__main__':
    MRKMeans.run()