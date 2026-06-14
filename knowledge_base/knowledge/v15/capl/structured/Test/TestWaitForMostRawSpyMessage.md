# TestWaitForMostRawSpyMessage

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForMostRawSpyMessage(long aSourceAddress, long aDestinationAddress, long aRType, BYTE aMsgData [], dword aMsgDataLength, dword aTimeout);
long TestWaitForMostRawSpyMessage(long aSourceAddress, long aDestinationAddress, long aRType, char aMsgDesc[], dword aTimeout);
```

## Description

This function waits for the occurrence of the specified MOST raw spy control message. Should the message not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

## Parameters

| Name | Description |
|---|---|
| aSourceAddress | Source address |
| aDestinationAddress | Target address |
| 0 | Normal |
| 1 | RemoteRead |
| 2 | RemoteWrite |
| 3 | Allocate |
| 4 | Deallocate |
| 5 | GetSource |
| aMsgData | Byte array containing the data bytes of the raw message to be matched. |
| aMsgDataLength | Length of byte array aMsgData. Data bytes at positions larger than the value of this parameter will not be considered when comparing with incoming messages. |
| aMsgDataDesc | String with hexadecimal values describing the message data bytes of the raw spy message to be matched, starting at byte position 0, f. e. "0A 0B 0C 0D 0E 0F 10 11 12 13 FF" Blanks will be ignored and can be used to enhance readability. Wildcards can be applied by replacing a nibble with "_", e.g. "0A 0B 0C __ __ __ 10" Data bytes at positions beyond the ones described in this parameter will not be considered when comparing with incoming messages. |
| aTimeout | Maximum wait time [ms] |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.1 | — | — | — | — |
| Restricted To | — | MOST25, MOST50, MOST150 | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
