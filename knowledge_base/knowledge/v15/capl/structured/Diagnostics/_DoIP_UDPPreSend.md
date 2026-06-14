# _DoIP_UDPPreSend

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long _DoIP_UDPPreSend( BYTE DoIPVersion[], BYTE inverseVersion[], WORD payloadType[], DWORD payloadLen[], BYTE payload[]);
```

## Description

The DoIP implementation is about to send an UDP DoIP packet with the given content. It is possible to change the values in header and data, and to change the total length of the UDP packet.

## Parameters

| Name | Description |
|---|---|
| DoIPVersion | Protocol version value to send, defaults to configured value. |
| inverseVersion | Inverse protocol version value to send. |
| payloadType | Type of the PDU sent. The value is converted from and to network byte order automatically. |
| payloadLen | Length of the payload as indicated in the header. The value is converted from and to network byte order automatically. |
| payload | Payload itself. Elcount( payload) indicates the maximum number of bytes that can be accessed in the callback which might be longer than payloadLen, i.e. more bytes might be available than used for DoIP. |

## Example

```c
// Patch the UDP packet send depending on a global control variable
long _DoIP_UDPPreSend( BYTE DoIPVersion[], BYTE inverseVersion[], WORD payloadType[], DWORD payloadLen[], BYTE payload[])
{
  long retVal;
  write( "UDPPreSend( version=%02x, invVersion=%02x, payloadtype=%04x, payloadLen=%d, [%d]<%02x ...>)"
  , DoIPVersion[0], inverseVersion[0], payloadType[0], payloadLen[0], elcount( payload)
  , elcount( payload) > 0 ? payload[0] : 0);
  retVal = 0;
  switch( sNextUDPFault)
  {
    case 1: // increase payload by 2 bytes and patch type to force a UDP response
      payload[payloadLen[0]] = 0xFF;
      payload[payloadLen[0] + 1] = 0xFF;
      payloadLen[0] += 2;       // increase payload length!
      payloadType[0] += 0x200;  // patch type
      break;

    case 2: // increase packet length
      retVal = 1000;
      break;

    case 3: // drop packet
      retVal = -1;
      break;
    default:
      return 0;
  }
  sNextUDPFault = 0;
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
