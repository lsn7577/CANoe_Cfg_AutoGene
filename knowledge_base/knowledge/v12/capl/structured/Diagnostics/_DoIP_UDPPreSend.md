# _DoIP_UDPPreSend

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long _DoIP_UDPPreSend( BYTE DoIPVersion[], BYTE inverseVersion[], WORD payloadType[], DWORD payloadLen[], BYTE payload[]);
```

## Description

The DoIP implementation is about to send an UDP DoIP packet with the given content. It is possible to change the values in header and data, and to change the total length of the UDP packet.

Note that packets sent by DoIP_UDPSend are NOT indicated here since it is possi-ble to provide any data using these calls anyway.

## Return Values

-1: Drop this UDP packet, i.e. it is NOT sent. This may cause errors in the protocol state machine.

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

| Since Version |
|---|
