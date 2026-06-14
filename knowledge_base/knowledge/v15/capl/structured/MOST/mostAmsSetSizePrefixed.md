# mostAmsSetSizePrefixed

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostAmsSetSizePrefixed(long channel, long minlength);
```

## Description

Configures the minimum length of an AMS message above which an initiating message with TelID==4 is sent.

## Parameters

| Name | Description |
|---|---|
| channel | Channel of the connected hardware interface. |
| minlength | Minimum length of an AMS message. minlength == -1: use the size configured in the hardware configuration dialog, AMS pageminlength == 0: never send an initiating message with TelID==4minlength >= 46: send an initiating message with TelID==4, when the length of the AMS message is >=minlength Note: Maximum value of minlength is 65535 (0xFFFF), since this is the maximum size of an AMS message. |

## Example

Activate special size prefix length for exactly one AMS message.

Activate special size prefix length for AMS messages with more than 200 bytes payload.

```c
mostAmsSetSizePrefixed(1, 46);
mostAmsOutput(1, "Telephone.List.Status(0,1,2,3,4,5,6,7)");
mostAmsSetSizePrefixed(1, -1);
mostAmsSetSizePrefixed(1, 200);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.2: MOST150 7.2 SP3: MOST50 | 7.2: MOST150 7.2 SP3: MOST50 | — | — | — | —✔ |
| Restricted To | MOST50 MOST150 | MOST50 MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
