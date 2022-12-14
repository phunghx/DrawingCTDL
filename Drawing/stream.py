import logging, sys, time, cv2, ffmpeg, numpy

logger = logging.getLogger("Writer")
logger.setLevel("INFO")
formatter = logging.Formatter("%(asctime)s %(levelname)-8s %(module)s %(message)s")
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
logger.addHandler(handler)

video_path='rtmp://live-10-hcm.fcam.vn:1956/63eef9bd282e0ab5mye8?t=1670316702&tk=a7386178df986c5f82d6b0164109ec196fc92023f525f1f98cb85295d3b5984f/KeYm2RCH-AhrStRPD-9g5Kioe1-PbAvhlmw-v2'

command = [ 'ffmpeg',
            #'-rtsp_transport', 'tcp',
            '-i', video_path,
            '-pix_fmt', 'rgb24',  # brg24 for matching OpenCV
            '-f', 'rawvideo',
            '-loglevel', 'error',
            'pipe:' ]
process = sp.Popen(command, stdout=sp.PIPE, bufsize=32)
H = 1080
W = 1920
#videoCapture = cv2.VideoCapture()
process = (                                                                                                                                                                                                                                                                   
    ffmpeg                                                                                                                                                                                                                                                                    
    .input('pipe:', framerate='{}'.format(videoCapture.get(cv2.CAP_PROP_FPS)), format='rawvideo', pix_fmt='bgr24', s='{}x{}'.format(1920, 1080))                                                                                                                              
    .output('rtsp://localhost:8554/mystream', vcodec='h264', format='rtsp',  pix_fmt='nv21', **{'b:v': 2000000}, loglevel='error')                                                                                                                                            
    .overwrite_output()                                                                                                                                                                                                                                                       
    .run_async(pipe_stdin=True)                                                                                                                                                                                                                                               
)

lastFrame = False
frames = 0
start = time.time()
while not lastFrame:
    buffer = process.stdout.read(W*H*3)
    if len(buffer) != W*H*3:
        break

    img = numpy.frombuffer(buffer, np.uint8).reshape(H, W, 3)
    
    process.stdin.write(
            img
            .astype(numpy.uint8)
            .tobytes()
        )        
    
    
elapsed = time.time() - start
logger.info("%d frames" % frames)
logger.info("%4.1f FPS, elapsed time: %4.2f seconds" % (frames / elapsed, elapsed))
del videoCapture
