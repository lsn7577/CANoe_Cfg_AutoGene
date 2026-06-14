# _DoIP_TCPPreSend

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long _DoIP_TCPPreSend( BYTE DoIPVersion[], WORD payloadType[], DWORD payloadLen[], BYTE payload[]);
```

## Description

The DoIP implementation is about to send a TCP DoIP PDU with the given content. It is possible to change the values in header and data, to drop the PDU, and to reduce the length of the payload. Only DoIP PDUs with valid layout are sent.

## Parameters

| Name | Description |
|---|---|
| DoIPVersion | Protocol version value to send, defaults to configured value. |
| payloadType | Type of the PDU sent. The value is converted from and to network byte order automatically. |
| payloadLen | Length of the payload as indicated in the header and actually sent. The value is converted from and to network byte order automatically. |
| payload | Payload itself. Elcount( payload) indicates the maximum number of bytes that can be accessed in the callback, and the maximum value payloadLen can be set to. |

## Example

```c
long _DoIP_TCPPreSend( BYTE DoIPVersion[], WORD payloadType[], DWORD payloadLen[], BYTE payload[])
{
  long retVal;
  write( "TCPPreSend( version=%02x, payloadtype=%04x, payloadLen=%d, [%d]<%02x ...>)",
  , DoIPVersion[0], payloadType[0], payloadLen[0], elcount( payload)
  , elcount( payload) > 0 ? payload[0] : 0);
  retVal = 0;
  switch( sNextTCPFault)
  {
    case 1: // Cut off 1 byte of data, if present
    if( payloadLen[0] > 0)
    {
      --payloadLen[0];
    }
    break;
    case 2: // patch payload type and DoIP version
    DoIPVersion[0] = 0x7;
    payloadType[0] += 0x100;
    break;
    case 3: // drop packet
    retVal = -1;
    break;
    default:
    return 0;
  }
  sNextTCPFault = 0;
  return retVal;
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
