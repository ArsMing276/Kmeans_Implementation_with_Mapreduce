import numpy as np
with open('e.txt', 'r') as f:
    list = []
    nclass = 0
    Points_arr = []

    for line in f:
        data_ID, Cluster_ID, Coord, Centroid = line.split('|')
        Coord_arr = np.array(Coord.split(','), dtype = float)
        
        Centroid = Centroid.strip('\t\n')
        Centroid_arr = np.array(Centroid.split(','), dtype = float)
        Centroid_arr = np.reshape(Centroid_arr, (-1, len(Coord_arr)))

        #print Centroid_arr.shape
        #print Coord_arr.shape
        nclass = Centroid_arr.shape[0]          
        ndim = Centroid_arr.shape[1]
        #print Centroid_arr
        #print Coord_arr
        Distance = ((Centroid_arr - Coord_arr)**2).sum(axis = 1)
        Cluster_ID = str(Distance.argmin() + 1)
        #print Cluster_ID
        Points_arr = np.append(Points_arr, Coord_arr)
        Points_arr = np.reshape(Points_arr,(-1,len(Coord_arr)))
        
        list.append((Cluster_ID, (data_ID, Coord_arr)))
    #print list
    Centroid_arr = []
    #print Points_arr
    print
    for cluster in range(1,nclass+1):
        temp_centroid = np.zeros(nclass)
        point_num = 0
        for point in list:
            '''
            print cluster
            print int(point[0])
            print point[1][1]
            '''
            if int(point[0]) == cluster:
                temp_centroid += point[1][1]
                point_num = point_num+1;
        if(point_num != 0):
            temp_centroid = temp_centroid /point_num 
        Centroid_arr = np.append(Centroid_arr, temp_centroid)
    Centroid_arr = np.reshape(Centroid_arr,(-1,len(Coord_arr)))

    print Centroid_arr
    print
    list = []
    for i in Points_arr:
        Distance = ((i-Centroid_arr)**2).sum(axis =1)
        Cluster_ID = str(Distance.argmin() + 1)
        list.append((Cluster_ID,i))
    
    iteration =1;
    while(iteration <= 10):
        Centroid_arr = []
        for cluster in range(1,nclass+1):
            temp_centroid = np.zeros(nclass)
            point_num = 0
            for point in list:
                if int(point[0]) == cluster:
                    temp_centroid += point[1]
                    point_num = point_num+1;
            if(point_num != 0):
                temp_centroid = temp_centroid /point_num 
            Centroid_arr = np.append(Centroid_arr, temp_centroid)
        Centroid_arr = np.reshape(Centroid_arr,(-1,len(Coord_arr)))
        print Centroid_arr
        print
        list = []
        for i in Points_arr:
            Distance = ((i-Centroid_arr)**2).sum(axis =1)
            Cluster_ID = str(Distance.argmin() + 1)
            list.append((Cluster_ID,i))
        iteration = iteration+1


