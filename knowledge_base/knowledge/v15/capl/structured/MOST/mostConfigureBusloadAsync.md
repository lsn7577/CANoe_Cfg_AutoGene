# mostConfigureBusloadAsync

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostConfigureBusloadAsync (long channel, long rate, long countertype, long counterpos, long destadr, long pktdatalen, BYTE pktdata[]);
```

## Description

The function configures the bus load generator for the asynchronous channel. With the specified rate the generator tries to send packets.Due to arbitration delays, the bus load actually generated can deviate from the specified rate.

As an option, the packets can be supplied with a sequence counter.

Load generation can be started with the mostGenerateBusloadAsync() function.

Bus load can also be generated without CAPL programming using the MOST Stress Window.

## Parameters

| Name | Description |
|---|---|
| channel | Channel of the connected MOST hardware. |
| rate | Number of packets per second. The maximum transmission rate depends on the packet length, the synchronous bandwidth control (SBC) and the MOST loop frequency. |
| 0 | No sequence counter |
| 1 | 1 byte counter |
| 2 | 2 byte counter (higher quality byte first) |
| 3 | 3 byte counter (higher quality bytes first) |
| 4 | 4 byte counter (higher quality bytes first) |
| counterpos | Position of the lowest value sequence counter byte. |
| destadr | Destination address |
| pktdatalen | Number of user data bytes (MOST25: 0<= pktdatalen <= 1014, MOST150: 1 <= pktdatalen <= 1524) |
| pktdata[] | User data |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.2 | 5.2 | — | — | — | —✔ |
| Restricted To | MOST25 MOST150 Not in StopMeasurement | MOST25 MOST150 Not in StopMeasurement | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
