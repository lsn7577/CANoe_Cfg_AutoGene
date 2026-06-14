# TestSendMostRawMessage

> Category: `Test` | Type: `function`

## Syntax

```c
long TestSendMostRawMessage(long aDestinationAddress, long aRType, BYTE aMsgData[], dword aMsgDataLength, dword aTimeout);
long TestSendMostRawMessage(long aDestinationAddress, long aRType, char aMsgDataDesc[], dword aTimeout);
```

## Description

This function immediately sends a MOST raw control message with the specified data and waits for the associated Tx acknowledgment from the recipient. The AckNack bit is evaluated and the return value specifies whether the creation and sending of the message was successful or not.

The first signature specifies the message data by a byte array, the second uses a string to describe the data bytes as a hex dump.

## Parameters

| Name | Description |
|---|---|
| aDestinationAddress | Target address |
| 0 | Normal |
| 1 | RemoteRead |
| 2 | RemoteWrite |
| 3 | Allocate |
| 4 | Deallocate |
| 5 | GetSource |
| aMsgData | Byte array containing the data bytes of the raw message to be send. |
| aMsgDataLength | Length of byte array aMsgData. Data bytes at positions larger than the value of this parameter will be set to 0 automatically. |
| aMsgDataDesc | String with hexadecimal values describing the message data bytes of the raw message to be send, starting at byte position 0, f. e. "0A 0B 0C 0D 0E 0F 10 11 12 13 FF" Blanks will be ignored and can be used to enhance readability. Data bytes at positions beyond the ones described in this parameter will be set to 0 automatically. |
| aTimeout | Maximum wait time [ms] |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.1 | 13.0 | — | — | — |
| Restricted To | — | MOST25 | MOST25 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
