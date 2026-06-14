# _DoIP_TCPDataInd

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void _DoIP_TCPDataInd( BYTE DoIPVersion, WORD payloadType, BYTE pay-load[]);
```

## Description

A DoIP PDU was received from the connected peer that cannot be interpreted by this implementation.

## Parameters

| Name | Description |
|---|---|
| DoIPVersion | Protocol version as sent in the header. |
| payloadType | Value from the header. |
| payload | The payload. |

## Return Values

—

## Example

```c
void _DoIP_TCPDataInd( BYTE DoIPVersion, WORD payloadType, BYTE payload[])
{
  write( "_DoIP_TCPDataInd( version=%d, type %04x, [%d]<%02x...>)"
  , DoIPVersion, payloadType
  , elcount( payload), elcount(payload) > 0 ? payload[0] : 0);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 SP4 | — | — | — | 1.0 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
