# mostSendError

> Category: `MOST` | Type: `function`

## Syntax

```c
mostSendError_Code (mostAmsMessage * msgcmd, byte code); // form 1
mostSendError_CodeByte (mostAmsMessage * msgcmd, byte code, byte byte1); // form 2
mostSendError_CodeByteByte(mostAmsMessage * msgcmd, byte code, byte byte1, byte byte2); // form 3
mostSendError_CodeByteWord(mostAmsMessage * msgcmd, byte code, byte byte1, word word1); // form 4
void SendError_CodeBytes(mostAMSMessage * msgcmd, byte code, byte data[], long datalen); // form 5
```

## Description

Generates and sends an error message directly based on a received command message.

The various signatures make it easy to transfer the most common error codes with their ancillary information.

Any wildcard InstId in the command message is transferred to a concrete value in the error message with the help of the device’s Local FBlock list.

## Parameters

| Name | Description |
|---|---|
| msgcmd | Received command message to be responded to |
| code | Error Code (see MOST specification) |
| byte1 | First ancillary information as byte |
| byte2 | Second ancillary information as byte |
| word1 | Second ancillary information as word |
| data | Ancillary information as byte array |
| datalen | Number of valid bytes in the array with the ancillary information |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.2 | 5.2 | — | — | — | —✔ |
| Restricted To | MOST25 MOST50 MOST150 | MOST25 MOST50 MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
