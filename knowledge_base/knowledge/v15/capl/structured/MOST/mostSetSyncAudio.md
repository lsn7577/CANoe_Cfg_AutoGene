# mostSetSyncAudio

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSetSyncAudio(long channel, long channels[4], long device, long mode); // form 1
MOST50 / MOST150: long mostSetSyncAudio(long channel, long label, long width, long device, long mode); // form 2
```

## Description

The function programs the routing engine for the audio input or output of the bus interface. The functions works independently of whether the synchronous channels are reserved. The user must ensure the reservation, e.g. by sending an Alloc message to the timing master.

MOST50 / MOST150: The function performs the routing of audio input or output of the bus interface. At completion of the routing operation the event procedure OnMostSyncAudio() will be called.

## Parameters

| Name | Description |
|---|---|
| channel | Channel of the connected interface |
| device = 0 | Synchronous channels on which the Line input signal should be routed to. |
| device = 1 | Synchronous channels from which the data should be routed to the Line output. |
| Note This parameter is ignored in case the routing is canceled (mode==0). |  |
| 0 | Line-In: Audio input signals are put on synchronous channels. |
| 1 | Line-Out: Synchronous channel signals are grabbed for audio output. |
| 0 | Cancels the routing. |
| 1 | Executes the routing. |
| label | Connection label. In case of Line-In routing (device=0; mode=1) the label parameter has no meaning. |
| width | Number of channels to be routed. |

## Return Values

See error codes

## Example

See CANoe online help MOST Access to Analog Audio Channels (Line In/ Headphone Out).

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.1 SP4 | 5.2 | — | — | — | —✔ |
| Restricted To | MOST25 MOST50 (since version 7.2 SP3) MOST150 (since version 7.1 SP2) Not in Stopmeasurement | MOST25 MOST50 (since version 7.2 SP3) MOST150 (since version 7.1 SP2) Not in Stopmeasurement | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
