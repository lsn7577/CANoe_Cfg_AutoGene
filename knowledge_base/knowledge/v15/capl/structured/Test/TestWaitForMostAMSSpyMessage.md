# TestWaitForMostAMSSpyMessage

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForMostAMSSpyMessage(dbMsg aDBMsg, int aInstanceId, unsigned long aTimeout);
long TestWaitForMostAMSSpyMessage(int aFBlockId, int aInstanceId, unsigned long aTimeout);
long TestWaitForMostAMSSpyMessage(int aFBlockId, int aInstanceId, int aFunctionId, unsigned long aTimeout);
long TestWaitForMostAMSSpyMessage(int aFBlockId, int aInstanceId, int aFunctionId, int aOpType, dword aTimeout);
long TestWaitForMostAMSSpyMessage(int aSourceAddress, int aDestinationAddress, int aFBlockId, int aInstanceId, int aFunctionId, int aOpType, unsigned long aTimeout);
long TestWaitForMostAMSSpyMessage(int aSourceAddress, int aDestinationAddress, char[] aSymbolicMessage, int aInstanceId, unsigned long aTimeout);
long TestWaitForMostAMSSpyMessage(int aSourceAddress, int aDestinationAddress, char[] aSymbolicMessage, unsigned long aTimeout);
long TestWaitForMostAMSSpyMessage(char[] aSymbolicMessage, int aInstanceId, unsigned long aTimeout);
TestWaitForMostAMSSpyMessage(char[] aSymbolicMessage, unsigned long aTimeout);
```

## Description

Waits for the occurrence of the specified MOST AMS spy message.

This may deal with transmission of individual frames (TelID=0) or segmented transmissions. In the case of segmented transmission, the last control message of a correct transmission resolves the wait conditions.

If the message does not occur by the time the aTimeout expires, the wait condition is still resolved.

## Parameters

| Name | Description |
|---|---|
| Note For parameters aSourceAddress, aDestinationAddress, aFBlockId, aInstanceId, aFunctionId and aOpType the following applies: If -1 is given, the corresponding field can get any value. This is also the standard for not explicit set values. |  |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 | — | — | — | — |
| Restricted To | — | MOST25, MOST50, MOST150 | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
