import os, glob

#paths
binpath = './bin_shvc/'
configpath = './cfg/'
encoderpath = './shvc/bin/'
logpath = './log_shvc/'
yuvpath = './yuv_sequence_chunks/'
width  = '1920'
height = '1080'
frames = '60'
fps = '30'
maxlayers = 5
filelist = ['stefan.yuv'] #jsut a placeholder, ignore
#qp = ['21', '24', '27', '30', '33', '36']
qp = ['46', '41', '36', '31', '26', '21']

def pause(chunk):
    programPause = input("Chunk {} done, Press the <ENTER> key to continue...".format(chunk))

def getchunk(name):
    ret = []
    #stefan_chunk_0.yuv
    files = glob.glob(yuvpath + '*.yuv')
    print(files)
    for f in files:
        if '_chunk_' in f:
            name = f.split('/')[-1]
            ret.append(name)
    return ret

def generateConfig(chunk):
    filename = './cfg/' + chunk + '.cfg'
    fp =  open(filename, 'w')
    fp.write('FramesToBeEncoded     : {}    # Number of frames to be coded \n'.format(frames))
    fp.write('Level0          : 4.1         # Level of the whole bitstream \n')
    fp.write('Level1          : 3.1         # Level of the base layer \n')
    fp.write('Level2          : 4.1         # Level of the enhancement layer \n')
    fp.write('\n')
    fp.write('#======== File I/O =============== \n')
    for layers in range(maxlayers):
        #write section for each layers
        fp.write('InputFile{} : {} \n'.format(layers, yuvpath + chunk))
        fp.write('FrameRate{} : {}   # Frame Rate per second \n'.format(layers, fps))
        fp.write('InputBitDepth{} : 8 # Input bitdepth for layer {} \n'.format(layers, layers))
        fp.write('SourceWidth{}  : {} # Input  frame width \n'.format(layers, width))
        fp.write('SourceHeight{} : {} # Input  frame height \n'.format(layers, height))
        fp.write('RepFormatIdx{} : 0 # Index of corresponding rep_format() in the VPS \n'.format(layers))
        fp.write('IntraPeriod{} : 48 # Period of I-Frame ( -1 = only first) \n'.format(layers))
        fp.write('ConformanceMode{} : 1 # conformance mode \n'.format(layers))
        fp.write('QP{}  : {} \n'.format(layers, qp[layers]))
        fp.write('LayerPTLIndex{}   : {} \n'.format(layers, layers + 1))
        fp.write('\n')
    fp.close()


def generateCommand(chunk):
    '''
    TAppEncoderStatic -c cfg/encoder_randomaccess_scalable.cfg -c cfg/per-sequence-svc/BasketballDrive-2x.cfg -c cfg/layers.cfg -q0 22 -q1 22 -b str/BasketballDrive.bin -o0 rec/BasketballDrive_l0_rec.yuv -o1 rec/BasketballDrive_l1_rec.yuv
    '''
    #only need to run for 5 layers
    command = encoderpath + 'TAppEncoderStatic '
    command += ' -c '+ configpath + 'encoder_randomaccess_scalable.cfg'
    command += ' -c ' + './cfg/' + chunk + '.cfg '
    command += ' -c ' + configpath + 'fivelayers.cfg '
    command += ' -q0 ' + qp[0] + ' -q1 ' + qp[1] + ' -q2 ' + qp[2]
    command += ' -q3 ' + qp[3] + ' -q4 ' + qp[4]
    command += ' -b ' + binpath +  chunk + '.bin'
    command += ' | tee ' +  logpath + chunk + '.txt'
    return command


def runSHVC():
    for name in filelist:
        # get all chunk of a file
        #chunks = getchunk(name) YachtRide_1920x1080_chunk_9.yuv_30_hevc.txt
        chunks = ['YachtRide_1920x1080_chunk_8.yuv']
        print(chunks)
        for chunk in chunks:
            # generate a config file per sequence before running SHVC
            generateConfig(chunk)
            # run SHVC encode on this chunk
            command = generateCommand(chunk)
            print(command)
            os.system(command)


if __name__ == '__main__':
    # col1               Layer1             layer2        ...
    # chunk1          (PSNR/Size)          (PSNR/Size)    ...
    # chunk2          (PSNR/Size)          (PSNR/Size)    ...
    # chunk3          (PSNR/Size)          (PSNR/Size)    ...
    #  ...                ...                ...          ...
    runSHVC()
