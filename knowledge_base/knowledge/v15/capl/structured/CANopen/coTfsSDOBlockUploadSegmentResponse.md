# coTfsSDOBlockUploadSegmentResponse

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOBlockUploadSegmentResponse( dword ccs, dword cs, dword ackSeq, dword blkSize, dword expMsgNumber, dword startSeqNumber );
```

## Description

This function waits for a SDO segmented upload request and sends the corresponding response. Before the call of this function, no time-delay functions should be inserted in order to prevent a loss of the request message.

## Parameters

| Name | Description |
|---|---|
| ccs (client command specifier) | 5: block upload |
| cs (client subcommand) | 2: block upload response |
| ackSeq | Sequence number of the message that should be confirmed. |
| blkSize | Block size |
| expMsgNumber | Number of requests awaited (generally corresponds to the value ackSeq), deviations can be used in order to provoke protocol violations. |
| startSeqNumber | SDO block number of the first block expected. |

## Return Values

Error code

## Example

```c
see example of coTfsSDOBlockInit
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 | 13.0 | — | — | 2.1 SP3 |
| Restricted To | — | CANopen | CANopen | — | — | CANopen |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
