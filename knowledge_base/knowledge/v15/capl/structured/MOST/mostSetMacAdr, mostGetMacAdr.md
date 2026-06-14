# mostSetMacAdr, mostGetMacAdr

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSetMacAdr(long channel, int64 macAdr);
int64 mostGetMacAdr(long channel);
```

## Description

The functions set and retrieve the 48 bit MAC address of the network interface controller. The MAC address identifies the network node during Ethernet-over-MOST150 communication (see OnMostEthPkt, outputMostEthPkt).

## Parameters

| Name | Description |
|---|---|
| channel | Channel of the connected interface |
| macAdr | 48 bit MAC address. |

## Example

```c
// Set MAC address on channel MOST 1 to 01:02:03:04:05:06
mostSetMacAdr(1, 0x010203040506LL);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.2 | 7.2 | — | — | — | —✔ |
| Restricted To | MOST150 | MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
