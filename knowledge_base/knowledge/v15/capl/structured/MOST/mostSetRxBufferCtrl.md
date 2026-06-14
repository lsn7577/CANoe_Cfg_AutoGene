# mostSetRxBufferCtrl

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSetRxBufferCtrl(long channel, long mode);
```

## Description

Disables or enables the Rx buffer for messages of the control channel.

In case the parameter mode is set to '0' or '1' the result is reported by means of the callback function OnMostStress().

Disabling the Rx buffer means that exactly one more message is accepted. Afterwards the buffer is no longer enabled, i.e. further messages are rejected with "RxBuffer full" (see status flags of Tx acknowledgment).

After the measurement start the receive buffer is always enabled.

VN2640:

Disabling the Rx buffer means that up to four control messages will be accepted, before the buffer is disabled and low level retries on the bus are provoked.

OptoLyzerOL3150o:

The stress network interface controller (NIC) must have its bypass opened (see mostSetStressNodeParameter ).Only messages addressed to the StressNIC will be blocked.

## Parameters

| Name | Description |
|---|---|
| channel | Channel of the connected interface |
| 0 | Disable receive buffer |
| 1 | Enable receive buffer |
| 2 | Enable receive buffer exactly once for one message |

## Return Values

See error codes

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.1 | 5.1 | — | — | — | —✔ |
| Restricted To | MOST25 MOST50 MOST150 After measurement start Not in Stopmeasurement | MOST25 MOST50 MOST150 After measurement start Not in Stopmeasurement | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
