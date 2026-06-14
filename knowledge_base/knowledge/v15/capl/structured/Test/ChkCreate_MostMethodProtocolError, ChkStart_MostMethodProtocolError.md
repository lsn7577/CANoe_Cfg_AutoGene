# ChkCreate_MostMethodProtocolError, ChkStart_MostMethodProtocolError

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_MostMethodProtocolError(char aMethod[], long aInstanceID, dword aTimeoutWaitForProcessing1, dword aTimeoutWaitForProcessing2, dword aTimeoutMaxDuration, Callback aCallback);
dword ChkStart_MostMethodProtocolError(char aMethod[], long aInstanceID, dword aTimeoutWaitForProcessing1, dword aTimeoutWaitForProcessing2, dword aTimeoutMaxDuration, Callback aCallback);
dword ChkCreate_MostMethodProtocolError(char aMethod[], long aInstanceID, dword aTimeoutWaitForProcessing1, dword aTimeoutWaitForProcessing2, dword aTimeoutMaxDuration);
dword ChkStart_MostMethodProtocolError(char aMethod[], long aInstanceID, dword aTimeoutWaitForProcessing1, dword aTimeoutWaitForProcessing2, dword aTimeoutMaxDuration);
dword ChkCreate_MostMethodProtocolError(char aMethod[], dword aTimeoutWaitForProcessing1, dword aTimeoutWaitForProcessing2, dword aTimeoutMaxDuration, Callback aCallback);
dword ChkStart_MostMethodProtocolError(char aMethod[], dword aTimeoutWaitForProcessing1, dword aTimeoutWaitForProcessing2, dword aTimeoutMaxDuration, Callback aCallback);
dword ChkCreate_MostMethodProtocolError(char aMethod[], dword aTimeoutWaitForProcessing1, dword aTimeoutWaitForProcessing2, dword aTimeoutMaxDuration);
dword ChkStart_MostMethodProtocolError(char aMethod[], dword aTimeoutWaitForProcessing1, dword aTimeoutWaitForProcessing2, dword aTimeoutMaxDuration);
dword ChkCreate_MostMethodProtocolError(char aMethod[], long aInstanceID, dword aTimeoutMaxDuration, Callback aCallback);
dword ChkStart_MostMethodProtocolError(char aMethod[], long aInstanceID, dword aTimeoutMaxDuration, Callback aCallback);
dword ChkCreate_MostMethodProtocolError(char aMethod[], long aInstanceID, dword aTimeoutMaxDuration);
dword ChkStart_MostMethodProtocolError(char aMethod[], long aInstanceID, dword aTimeoutMaxDuration);
dword ChkCreate_MostMethodProtocolError(char aMethod[], dword aTimeoutMaxDuration, Callback aCallback);
dword ChkStart_MostMethodProtocolError(char aMethod[], dword aTimeoutMaxDuration, Callback aCallback);
dword ChkCreate_MostMethodProtocolError(char aMethod[], dword aTimeoutMaxDuration);
dword ChkStart_MostMethodProtocolError(char aMethod[], dword aTimeoutMaxDuration);
```

## Description

This check monitors MOST protocol compliance for a given method supporting the optypes "StartResult" or "StartResultAck". This includes monitoring of the messages sequences and timeout conditions on answer times and send intervals.

## Parameters

| Name | Description |
|---|---|
| aMethod | Name of the method to be monitored in one of the following formats: FBlock.InstanceID.Function FBlock.Function |
| aInstanceID | InstanceID of the method to be monitored. Since command messages are often addressed to wildcard InstanceID (0x00) it is recommended to set this parameter to 0x00. The check includes requests/responses with InstanceIDs from 0x00 to 0xFE then. If a signature without InstanceID parameter is choosen, 0x00 is applied. InstanceID=0xFF=All observes requests with InstanceID=0xFF only. In this case it cannot be checked if all FBlock instances reply, because the number of instances in a device is not known to the algorithm. |
| aTimeoutWaitForProcessing1 | Timeout to wait for the observation of the first "Processing" or "ProcessingAck" message. The unit can be set with ChkConfig_SetPrecision. Signatures that do not provide this parameter, assume the maximum value of 250 ms given for tWaitForProcessing1 in the MOST specification. |
| aTimeoutWaitForProcessing2 | Timeout to wait for the following Processing messages. The unit can be set with ChkConfig_SetPrecision. Signatures that do not provide this parameter, assume the typical value of 200 ms given for tWaitForProcessing2 in the MOST specification. |
| aTimeoutMaxDuration | Maximum response time for the observed method to return a "Result"/ "Resul-tAck" or "Error"/ "ErrorAck" message. The unit can be set with ChkConfig_SetPrecision. |
| aCallback | Name of the callback function, which should be called as soon as a protocol violation is detected. In simulation nodes this parameter has to be set. In test modules this parameter is optional. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.0 7.0 SP5: method | — | — | — | — |
| Restricted To | — | MOST | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
