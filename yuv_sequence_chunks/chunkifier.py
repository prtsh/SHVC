import os, glob

'''
Convert a raw video sequence (yuv 4:2:0) into chunks of fixed frame counts
'''

width = '1920' #'352'
height = '1080' #'288'
fps = '30'
time = '2'
#frames = framerate * time

inputpath = './'
outputpath = './'

def readfilename(path):
    ret = []
    files = glob.glob(path + '/*.yuv')
    for f in files:
        if "_chunk_" in f:
            continue
        name = f.split('/')[-1]
        ret.append(name)
    return ret


def chunkify():
    #read input files
    files = readfilename(inputpath)
    for filename in files:
        if "_chunk_" in filename:
            continue
        print(filename)
        infile = inputpath + filename
        outfile = outputpath + filename.split('.')[0] + '_chunk_'
        '''
        ffmpeg -i input.y4m -f segment -segment_time 1 -pix_fmt yuv444p output%4d.y4m
        ffmpeg -f rawvideo -framerate 30  -s 1280x720 -pixel_format yuv420p -i input.yuv -f -segment_time 5  -pix_fmt yuv420p output%4d.y4m
        '''
        command =  'ffmpeg -f rawvideo -framerate ' + fps + ' -s ' + width + 'x' + height
        command += ' -pix_fmt yuv420p -i ' + infile + ' -f segment -segment_time ' + time
        command += ' -pix_fmt yuv420p ' + outfile + '%d.yuv'
        print(command)
        os.system(command)


if __name__ == '__main__':
    chunkify()
