# mostGetHWCapability

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostGetHWCapability(long channel, long capID);
```

## Description

mostGetHWCapability() can be used to query the properties of the MOST interface used.

## Parameters

| Name | Type | Description |
|---|---|---|
| channel |  | Channel of the connected interface. |
| ID | Return Value | Description of the Return Value |
| kMostHWCap_MaxNumberOfInstances = 0 | >0 | Number of interfaces of this type being used simultaneously |
| kMostHWCap_MaxWriteOS8104Registers = 1 | >=0 | Number of OS8104 registers that can be written with a command |
| kMostHWCap_MaxReadOS8104Registers = 2 | >=0 | Number of OS8104 registers that can be read with a command |
| kMostHWCap_TwinklePowerLed = 3 | 0, 1 | 1: The mostTwinklePowerLed command functions with the interface |
| kMostHWCap_LightLockStress = 4 | 0, 1 | 1: The mostGenerateLightError and mostGenerateLockError commands function with the interface |
| kMostHWCap_CtrlNode = 8 | 0, 1 | 1: Can be operated in Node Mode for the control channel (sending/receiving control messages) |
| kMostHWCap_CtrlSpy = 9 | 0, 1 | 1: Can be operated in Spy Mode for the control channel |
| kMostHWCap_CtrlNodeAndSpySimultaneous = 10 | 0, 1 | 1: Can be operated simultaneously in Node and Spy Mode (control channel) |
| kMostHWCap_CtrlNodeAndSpyEventDoubling = 11 | 0, 1 | 1: Always generates node and spy message for a received message from the control channel |
| kMostHWCap_CtrlRxBufferFullSimulation = 12 | 0, 1 | 1: The mostSetRxBufferCtrl command functions with the interface |
| kMostHWCap_AsyncNode = 16 | 0, 1 | 1: Can be operated in Node Mode for the asynchronous channel |
| kMostHWCap_AsyncSpy = 17 | 0, 1 | 1: Can be operated in Spy Mode for the asynchronous channel |
| kMostHWCap_AsyncNodeAndSpySimultaneous = 18 | 0, 1 | 1: Can be operated simultaneously in Node and Spy Mode (asynchronous channel) |
| kMostHWCap_AsyncNodeAndSpyEventDoubling = 19 | 0, 1 | 1: Always generates node and spy message for a received message from the asynchronous channel |
| kMostHWCap_SyncAnalogInChannels = 24 | >=0 | Number of analog-in channels (16 bit stereo) |
| kMostHWCap_SyncAnalogOutChannels = 25 | >=0 | Number of analog-out channels (16 bit stereo) |
| kMostHWCap_SyncAnalogInMute = 26 | 0, 1 | 1: Can mute the analog-in channel |
| kMostHWCap_SyncAnalogOutMute = 27 | 0, 1 | 1: Can mute the analog-out channel |
| kMostHWCap_SyncAllocTableReporting = 28 | 0, 1 | 1: Reports changes to the allocation table |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.2 | 5.2 | — | — | — | —✔ |
| Restricted To | MOST25 MOST50 MOST150 | MOST25 MOST50 MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
