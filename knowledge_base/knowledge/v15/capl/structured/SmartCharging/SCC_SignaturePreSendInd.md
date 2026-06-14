# SCC_SignaturePreSendInd

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_SignaturePreSendInd(byte SessionId[], dword MessageId, byte Signature[], dword& SigLength)
```

## Description

This callback is called when a signature for a message has been created. It allows to peek for the signature and its length before it is sent with the indicated message. Also, both signature and length may be changed for the purpose of fault injection.

## Parameters

| Name | Description |
|---|---|
| SessionID | 8-byte long SessionID of SCC connection, range: 0 – 0xFF FF FF FF FF FF FF FF. |
| MessageID | Type of the message that will use the signature. |
| Signature | The signature data. |
| sigLength | The number of signature data bytes. |

## Return Values

—

## Example

```c
SCC_SignaturePreSendInd( byte SessionID[], dword MessageID, byte Signature[], dword& SignatureLength)
{
  WriteLineEx(writeTab, 1, "SCC: Signature of length %i created for message %d", SignatureLength, MessageID);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 14 | — | — | — | 5.0 SP3 |
| Restricted To | — | .SmartCharging | — | — | — | .SmartCharging |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
