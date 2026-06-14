# mostSetStressNodeParameterData

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSetStressNodeParameterData(long channel, long id, long datalen, byte data[]);
```

## Description

OptoLyzer G2 3150o:

The OptoLyzer G2 3150o for MOST150 provides stress functionality through an additional network interface controller (NIC).

With mostSetStressNodeParameterData the MOST node parameters of this additional NIC can be configured.

## Parameters

| Name | Description |
|---|---|
| channel | Channel of the connected interface. |
| ID | Description Value Range / Meaning Availability |
| 4 | Configure the response of the stress node when receiving NetBlock.FBlockIDs.Get. A sequence of pairs (FBLockID, InstID) with up to 22 entries (44 bytes) can be set. The response message NetBlock.FBlockIDs.Status transports the seqeunce in its parameter section. 0 <= datalen <= 44 OptoLyzer G2 3150o |
| datalen | Number of bytes to be set. |
| data | Bytes to be set. |

## Return Values

See error codes

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.6 SP4 | 7.6 SP4 | — | — | — | —✔ |
| Restricted To | MOST150 | MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
