# outputMostEthPkt

> Category: `MOST` | Type: `function`

## Syntax

```c
outputMostEthPkt(long channel, int64 destMacAdr, long dataLen, byte[] data); // form 1
outputMostEthPkt(long channel, long prio, long retryCount, int64 sourceMacAdr, int64 destMacAdr, long dataLen, byte[] data); // form 2
```

## Description

Sends out an Ethernet packet over the asynchronous channel.

## Parameters

| Name | Description |
|---|---|
| channel | Application channel number. |
| destMacAdr | Destination MAC address (6 Byte). |
| dataLen | Number of data bytes to be sent (2 <= dataLen <= 1506). |
| Note At least two bytes have to be sent (Ethernet Type Field). In case more than 1502 Bytes should be sent, the VLAN Tag has to be set in the first two data bytes (0x81, 0x00). |  |
| Note Value range: 0x01..0x07. The value "-1" is also valid and used as wildcard to set the default priority (0x07). |  |
| Note Value range: 0x00..0x07. The value "-1" is also valid and used as wildcard to set the number of retries configured for the asynchronous channel (see mostSetRetryParameter). |  |
| Note It is possible to set another source MAC address as the own one. The value "-1" is also valid and is used as wildcard to set the own MAC address. |  |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.1 SP4 | 7.1 SP4 | — | — | — | —✔ |
| Restricted To | MOST150 After measurement start Not in Stopmeasurement | MOST150 After measurement start Not in Stopmeasurement | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
