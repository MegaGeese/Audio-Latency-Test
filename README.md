# Audio Latency Test
## Audio latency tester used to test latency over different protocols i.e. bluetooth, 2.4GHz, physical cable

## Setup: 
Start by plugging in your computers audio output (line-out, audio interface, DAC, ect.) into your computer's audio input (line-in, mic-in, interface, ect.)

Ensure that both the audio source and recording source are your primary audio devices

Run python '.\pyaudioTest audio.py' and wait

# Findings

## Short Direct Connection (Line-Out to Line-In) 82cm cable 10 tests 
### Average: 0.299544ms
```
Latency = 0.29785ms
Latency = 0.29702ms
Latency = 0.29984ms
Latency = 0.30855ms
Latency = 0.29951ms
Latency = 0.29907ms
Latency = 0.29905ms
Latency = 0.29763ms
Latency = 0.29851ms
Latency = 0.29841ms
```
## Long Direct Connection (Line-Out to Line-In) 609 cm cable 10 tests
### Average: 0.296539
```
Latency = 0.29913ms
Latency = 0.29747ms
Latency = 0.29597ms
Latency = 0.29629ms
Latency = 0.29646ms
Latency = 0.29572ms
Latency = 0.29437ms
Latency = 0.29628ms
Latency = 0.29654ms
Latency = 0.29716ms
```
## Long Direct Connection (Scarlet Focusrite Solo to Line-In) 609 cm cable 10 tests
### Average: 0.386003
```
Latency = 0.38418ms
Latency = 0.38627ms
Latency = 0.38559ms
Latency = 0.38546ms
Latency = 0.38510ms
Latency = 0.38624ms
Latency = 0.38834ms
Latency = 0.38666ms
Latency = 0.38559ms
Latency = 0.38660ms
```
## 2.4GHz transeiver (Line-Out to Line-In) 10 tests
### Average: 0.317595
```
Latency = 0.31504ms
Latency = 0.32019ms
Latency = 0.31887ms
Latency = 0.31990ms
Latency = 0.31993ms
Latency = 0.31837ms
Latency = 0.31856ms
Latency = 0.30901ms
Latency = 0.31645ms
Latency = 0.31963ms
```
## Bluetooth transiever (Line-Out to Line-In) 10 tests
### Average: 0.453861
```
Latency = 0.45834ms
Latency = 0.45427ms
Latency = 0.45464ms
Latency = 0.45313ms
Latency = 0.45330ms
Latency = 0.45330ms
Latency = 0.45264ms
Latency = 0.45381ms
Latency = 0.45214ms
Latency = 0.45304ms
```
