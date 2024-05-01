import pyaudio
import audioop
import time
import wave

repeat_times = 10
threshold = 100
end_latency_times = []
start_latency_times = []

print("* recording")

for i in range(repeat_times):
    time.sleep(1)
    wf = wave.open("./kick.wav", 'rb')

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 5

    p = pyaudio.PyAudio()

    # Define callback for playing audio in another thread
    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    record = p.open(format=FORMAT, 
                    channels=CHANNELS, 
                    rate=RATE, 
                    input=True, 
                    output=False, 
                    frames_per_buffer=CHUNK)

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    input=False,
                    output=True,
                    start=False,
                    stream_callback=callback)

    record.start_stream()
    over_threshold = False

    stream.start_stream()
    start_latency_times.append(time.time())
    # Listen for audio on callback and log time
    while not over_threshold:
        data = record.read(CHUNK)
        rms = audioop.rms(data, 2)
        if(rms > threshold):
            end_latency_times.append(time.time())
            record.close()
            over_threshold = True
        time.sleep(0.0001)

print("* done")
stream.close()
record.close()
p.terminate()

total = 0
for i in range(repeat_times):
    end_latency = end_latency_times[i]
    start_latency = start_latency_times[i]
    total_latency = end_latency - start_latency
    total += total_latency
    # print(f'Latency = {"%.2f" % end_latency}ms - {"%.2f" % start_latency}ms = {"%.5f" % total_latency}ms')
    print(f'Latency = {"%.5f" % total_latency}ms')

print(f'Average: {"%.5f" % (total/repeat_times)}ms')