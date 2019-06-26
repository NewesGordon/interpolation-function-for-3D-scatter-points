from scipy.interpolate import griddata
#import matplotlib.pyplot as plt
import pandas
import np

def interPolateFunc(data):#data:n*3
    try:
        points = pandas.DataFrame(np.array(data))#构造DataFame
        points.set_axis(['lon', 'lat', 'depth'], axis='columns', inplace=True)#重新设置列索引名称
        grid_x, grid_y = np.mgrid[min(points.iloc[:,0]):max(points.iloc[:,0]):500j, min(points.iloc[:,1]):max(points.iloc[:,1]):500j]
        values = points.iloc[:,2]
        points2 = points.drop('depth',1)#去掉最后一列
        grid_z = griddata(points2, values, (grid_x, grid_y), method='cubic')#插值nearest,linear,cubic
        len_lon = len(grid_x)#经度数据点数
        len_lat = len(grid_x[0])#纬度数据点数
        depth = grid_z.tolist()#深度数据
        lon_start = min(points.iloc[:,0])#经度起点
        lon_end = max(points.iloc[:,0])#经度终点
        lat_start = min(points.iloc[:,1])#纬度起点
        lat_end = max(points.iloc[:,1])#纬度终点
    except BaseException:
        len_lon = -1
        len_lat = -1
        return len_lon, len_lat
    else:
        return len_lon, len_lat, depth, lon_start, lon_end, lat_start, lat_end

#points = [[119.125,37.625,10],[119.125,37.750,10],[119.125,38.500,15],[119.250,25.375,5],[129.875,37.750,1400]]
#len_lon, len_lat, grid_z,lon0, lon1, lat0, lat1 = interPolateFunc(points)
#绘图
#plt.imshow(grid_z, extent=(lon0, lon1, lat0, lat1), origin='lower')
#plt.title('Cubic')
#plt.gcf().set_size_inches(5, 5)
#plt.show()
