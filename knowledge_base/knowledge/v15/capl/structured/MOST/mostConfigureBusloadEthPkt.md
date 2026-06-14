# mostConfigureBusloadEthPkt

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostConfigureBusloadEthPkt(long channel, long rate, long countertype, long counterpos, int64 srcadr, int64 destadr, long datalen, BYTE data[]);
```

## Description

The function configures the bus load generator for the Ethernet channel.

As an option, the packets can be supplied with a sequence counter.

Load generation can be started with the mostGenerateBusloadEthPkt function.

## Parameters

| Name | Description |
|---|---|
| channel | Channel of the connected interface. |
| rate | Number of Ethernet packets per second. The maximum transmission rate depends on the packet length, the synchronous bandwidth control (SBC) and the MOST loop frequency. Due to arbitration delays, the bus load actually generated can deviate from the specified rate. |
| 0 | No sequence counter |
| 1 | 1 byte counter |
| 2 | 2 byte counter (higher quality byte first) |
| 3 | 3 byte counter (higher quality bytes first) |
| 4 | 4 byte counter (higher quality bytes first) |
| counterpos | Position of the lowest counter byte. |
| Note It is possible to set another source MAC address as the own one. The value "-1" is also valid and is used as wildcard to set the own MAC address. |  |
| destadr | Target MAC address (6 Byte). |
| dataLen | Number of data bytes to be sent (2 <= dataLen <= 1506). |
| Note At least two bytes have to be sent (Ethernet Type Field). In case more than 1502 Bytes should be sent, the VLAN Tag has to be set in the first two data bytes (0x81, 0x00). |  |

## Return Values

See error codes

## Example

See mostGenerateBusloadEthPkt

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 SP2 | 7.5 SP2 | — | — | — | —✔ |
| Restricted To | MOST150 | MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
