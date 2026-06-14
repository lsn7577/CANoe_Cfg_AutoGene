# TestJoinMostMessageEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinMostMessageEvent (dbMsg aDBMsg, int aInstanceId)
long TestJoinMostMessageEvent (int aFBlockId, int aInstanceId)
long TestJoinMostMessageEvent (int aFBlockId, int aInstanceId, int aFunctionId)
long TestJoinMostMessageEvent (int aFBlockId, int aInstanceId, int aFunctionId, int aOpType)
long TestJoinMostMessageEvent (int aSourceAddress, int aDestinationAddress, int aFBlockId, int aInstanceId, int aFunctionId, int aOpType)
long TestJoinMostMessageEvent (int aSourceAddress, int aDestinationAddress, char[] aSymbolicMessage, int aInstanceId)
long TestJoinMostMessageEvent (int aSourceAddress, int aDestinationAddress, char[] aSymbolicMessage)
long TestJoinMostMessageEvent (char[] aSymbolicMessage, int aInstanceId)
long TestJoinMostMessageEvent (char[] aSymbolicMessage)
```

## Description

Completes the current set of "joined events" with the transmitted event, a MOST message (MOST control message or MOST spy message). This function does not wait.

## Parameters

| Name | Description |
|---|---|
| Note For parameters aSourceAddress, aDestinationAddress, aFBlockId, aInstanceId, aFunctionId and aOpType the following applies: If -1 is given, the corresponding field can get any value. This is also the standard for not explicit set values. |  |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 | — | — | — | — |
| Restricted To | — | MOST25, MOST50, MOST150 | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
