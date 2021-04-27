import os, sys

logpath = './log_hevc/'
yuvseq = ['HoneyBee_1920x1080','Beauty_1920x1080','Bosphorus_1920x1080', 'HoneyBee_1920x1080', 'Jockey_1920x1080', 'ReadySteadyGo_1920x1080','YachtRide_1920x1080', 'ShakeNDry_1920x1080', ]
chunks = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
qplist = ['50', '46', '43', '39', '36', '33', '30', '27', '24']
#get all data - bitrate + PSNR for each chunk of a file
bitrate_all = []
quality_all = []
def getChunkData(fname, bitrate, quality):
    with open(fname) as fp:
        line = fp.readlines() [-22:-21]
        tokens = line[0].split()
        bitrate.append(float(tokens[3]))
        quality.append(float(tokens[4]))
        #print(tokens[3], tokens[4])

def getFileData(yuvseq):
    for yuvfile in yuvseq: #HoneyBee_1920x1080
        bitrate_all = []
        quality_all = []
        print("\n *************************************** \n")
        print(yuvfile)
        print("\n *************************************** \n")
        for chunk in chunks:
            suffix = '_chunk_' + chunk + '.yuv_' 
            prefix = yuvfile + suffix #HoneyBee_1920x1080_chunk_9.yuv_
            bitrate = []
            quality = []
            print(prefix)
            for q in qplist:
                suffix   = q + '_hevc.txt'
                filename = prefix + suffix #HoneyBee_1920x1080_chunk_9.yuv_50_hevc.tct
                chunk    = logpath + filename
                getChunkData(chunk, bitrate, quality)
            print("bitrate(kbps) -", bitrate, "\n", "PSNR(dB) -", quality, "\n")
            bitrate_all.append(bitrate)
            quality_all.append(quality)
        print(bitrate_all, "\n", quality_all)

if __name__ == '__main__':
    getFileData(yuvseq)
    print("\n ------------------------------------------------------- \n")
