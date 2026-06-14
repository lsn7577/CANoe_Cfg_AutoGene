# _DoIP_MessageAcknowledgeInd

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void _DoIP_MessageAcknowledgeInd( WORD payloadType, long ackCode, WORD testerAddress, WORD ecuAddress);
```

## Description

A positive or negative acknowledgment was received in the tester. The code may provide additional information on the reason for a negative acknowledge.

## Parameters

| Name | Description |
|---|---|
| payloadType | ISO13400 0x8002: Diagnostic message positive acknowledgment 0x8003: Diagnostic message negative acknowledgment HSFZ 0x02: positive acknowledgment 0x40..0xFF: negative acknowledgment (different reasons) other reserved |
| ackCode | Response code transported in the acknowledgment, or -1 for HSFZ. -1: not available, i.e. HSFZ does not send a code 0: OK (ISO 13400 positive acknowledgment) 2..8: Not OK (ISO 13400 negative acknowledgment) other reserved |
| testerAddress | Logical address of the tester the acknowledgment is directed to. |
| ecuAddress | Logical address of the entity that sends the acknowledgment. |

## Return Values

—

## Example

```c
void _DoIP_MessageAcknowledgeInd( word payloadType, long code, word testerAddress, word ecuAddress)
{
  write( "_DoIP_MessageAcknowledgeInd type %04x, %d, tester=%04x, ecu=%04x", payloadType, code, testerAddress, ecuAddress);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.5 SP3 | — | — | — | 2.0 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
