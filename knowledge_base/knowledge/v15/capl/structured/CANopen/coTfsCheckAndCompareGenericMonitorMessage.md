# coTfsCheckAndCompareGenericMonitorMessage

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsCheckAndCompareGenericMonitorMessage( dword canId, dword dlc, qword msgData, qword msgMask, dword order );
```

## Description

This function checks if the expected message data are received.

After monitoring is started with coTfsConfigureGenericMonitor the received messages can be checked with this function. The parameter order defines to which message the comparison is executed. The check is successfully passed if the message with the expected message number and the expected data is received.

The function can be used during a monitoring started with coTfsConfigureGenericMonitor as well as after coTfsDeactivateGenericMonitor. The internal list of received messages is reset not before the monitoring is restarted with coTfsConfigureGenericMonitor.

## Parameters

| Name | Description |
|---|---|
| canId | CAN-ID of the monitored message. |
| dlc | Message length in byte, [0..8]. |
| msgData | Expected message data. |
| msgMask | Message data mask, set bits are compared and the message is presumed to be valid if the bits match with the data. |
| order | 0: Any receive message must contain the data specified in msgData/msgMask1..0xFFFFFFFE: The numeric specified message must contain the data specified in msgData/msgMask, 1 is the oldest message0xFFFFFFFF: The last received message must contain the data specified in msgData/msgMask |

## Return Values

Error code

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
