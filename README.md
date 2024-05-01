# Audio Latency Test
## Audio latency tester used to test latency over different protocols i.e. bluetooth, 2.4GHz, physical cable

## Setup: 
Start by plugging in your computers audio output (line-out, audio interface, DAC, ect.) into your computer's audio input (line-in, mic-in, interface, ect.)

Ensure that both the audio source and recording source are your primary audio devices

Run python '.\pyaudioTest audio.py' and wait

# Findings
Note: Beacn is an audio processing software that I use
### Beacn
Beacn adds about a 0.15ms delay to the audio audio latency
### Cable Length
Cable length has no appreciable affect on audio audio latency
### Atom Amp/Schiit DAC
Neither the Atom Amp nor the Shiit DAC has no appreciable affect on audio latency
### Scarlett Focusrite
Surprisingly the Scarlett interface adds about a 0.1ms delay to the audio chain
### 2.4GHz
The transievers that I have seem to add about 0.03ms of delay to the audio chain
### Bluetooth
The bluetooth TX/RX pucks that I have added about 0.18ms of delay

# Without Beacn
## Short Direct Connection (Line-Out to Line-In) 82cm cable 10 tests 
### Average: 0.15654ms
```
Latency = 0.14934ms
Latency = 0.15826ms
Latency = 0.15465ms
Latency = 0.15826ms
Latency = 0.15797ms
Latency = 0.15789ms
Latency = 0.15511ms
Latency = 0.15702ms
Latency = 0.15871ms
Latency = 0.15825ms
```
## Long Direct Connection (Scarlet Focusrite Solo to Line-In) 609 cm cable 10 tests
### Average: 0.25939ms
```
Latency = 0.25274ms
Latency = 0.25994ms
Latency = 0.26112ms
Latency = 0.25980ms
Latency = 0.25985ms
Latency = 0.26102ms
Latency = 0.26027ms
Latency = 0.25819ms
Latency = 0.26131ms
Latency = 0.25968ms
```
## Long Direct Connection (Atom Amp + Schiit DAC  to Line-In) 609 cm cable 10 tests
### Average: 0.16394ms
```
Latency = 0.15477ms
Latency = 0.15806ms
Latency = 0.15777ms
Latency = 0.18646ms
Latency = 0.15719ms
Latency = 0.16233ms
Latency = 0.15570ms
Latency = 0.15727ms
Latency = 0.16254ms
Latency = 0.18732ms
```
## 2.4GHz transeiver (Atom Amp + Schiit DAC to Line-In) 122cm between 10 tests
### Average: 0.18552ms
```
Latency = 0.18565ms
Latency = 0.18909ms
Latency = 0.18925ms
Latency = 0.15773ms
Latency = 0.18874ms
Latency = 0.18962ms
Latency = 0.18812ms
Latency = 0.18942ms
Latency = 0.18869ms
Latency = 0.18894ms
```
## 2.4GHz transeiver (Line-Out to Line-In) 122cm between 10 tests
### Average: 0.18717ms
```
Latency = 0.18063ms
Latency = 0.18684ms
Latency = 0.18901ms
Latency = 0.18502ms
Latency = 0.18892ms
Latency = 0.18908ms
Latency = 0.18670ms
Latency = 0.19010ms
Latency = 0.18764ms
Latency = 0.18778ms
```
## Bluetooth transiever (Line-Out to Line-In) 122cm between 10 tests
### Average: 0.33987ms
```
Latency = 0.34211ms
Latency = 0.32019ms
Latency = 0.32134ms
Latency = 0.34488ms
Latency = 0.32052ms
Latency = 0.35162ms
Latency = 0.34641ms
Latency = 0.35065ms
Latency = 0.35130ms
Latency = 0.34971ms
```

# With Beacn
Not much point in posting all this but I recorded the data before realizing that it had an effect on the latency :3
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
### Average: 0.296539ms
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
### Average: 0.386003ms
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
### Average: 0.317595ms
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
## 2.4GHz transeiver (Scarlet Focusrite Solo to Line-In) 122cm between 10 tests
### Average: 0.41358ms
```
Latency = 0.41679ms
Latency = 0.41152ms
Latency = 0.41133ms
Latency = 0.41062ms
Latency = 0.41251ms
Latency = 0.41101ms
Latency = 0.41204ms
Latency = 0.41078ms
Latency = 0.41945ms
Latency = 0.41976ms
```
## 2.4GHz transeiver (Atom Amp to Line-In) 122cm between 10 tests
### Average: 0.31025ms
```
Latency = 0.31473ms
Latency = 0.30949ms
Latency = 0.31375ms
Latency = 0.31173ms
Latency = 0.30887ms
Latency = 0.31254ms
Latency = 0.31246ms
Latency = 0.31019ms
Latency = 0.29769ms
Latency = 0.31107ms
```
## 2.4GHz transeiver (Atom Amp + Schiit DAC to Line-In) 122cm between 10 tests
### Average: 0.30662ms
```
Latency = 0.31340ms
Latency = 0.31268ms
Latency = 0.31120ms
Latency = 0.29982ms
Latency = 0.31006ms
Latency = 0.29871ms
Latency = 0.31084ms
Latency = 0.29910ms
Latency = 0.29859ms
Latency = 0.31179ms
```
## Bluetooth transiever (Line-Out to Line-In) 10 tests
### Average: 0.453861ms
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
