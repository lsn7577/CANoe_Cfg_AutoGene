# mostSyncAlloc

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSyncAlloc(long numChannels);
Callback: void OnMostSyncAllocResult(long allocResult, long numChannels, long channels[]);
```

## Description

MOST25:

This function reserves synchronous bandwidth by sending an Alloc system message to the MOST TimingMaster.

The result is reported by means of the callback function OnMostSyncAllocResult(). This requires defining OnMostSyncAllocResult() in the CAPL program using the following signature: OnMostSyncAllocResult(long allocResult, long numChannels, long channels[])

MOST150:

Allocates synchronous bandwidth on MOST150.

Callback:

This function is called on completion of the allocation of channels triggered by the call of the function.

Whether the allocation was successful and if so, which channels were allocated, is indicated in the parameters described below.

## Parameters

| Name | Description |
|---|---|
| numChannels | The number of channels to be reserved: MOST25: 1 <= numChannels <= 8 MOST150: 1 <= numChannels <= MaxSyncBandwidth (depends on boundary settings - max. value: 372) |
| kGrant = 0x01 | The channels were reserved |
| kBusy = 0x02 | The channels were not reserved, because the TimingMaster is busy processing another request |
| kDeny = 0x03 | The channels were not reserved, because there are no more channels available |
| kWrong = 0x04 | The reservation request contains invalid parameters |
| kUnknown = 0xFF | Unspecified error (e.g. a timeout while waiting for the TimingMaster to respond) |
| numChannels | The number of reserved channels. (1 <= numChannels <= 8). |
| channels[] | The values contained in this parameter are valid for allocResult = 0x01 only. It passes numChannels channel numbers reserved via mostSyncAlloc(). The value in channels[0] designates the label used for administration of the reserved channels. |

## Return Values

See error codes

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.0 | — | — | — | —✔ |
| Restricted To | — | MOST25 MOST150 After measurement start Not in Stopmeasurement | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | — | ✔ | — | N/A | — | —✔ |
| 64-Bit | — | ✔ | — | — | — | —✔ |
