# _DoIP_TCPPreSend

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long _DoIP_TCPPreSend( BYTE DoIPVersion[], WORD payloadType[], DWORD payloadLen[], BYTE payload[]);
```

## Description

The DoIP implementation is about to send a TCP DoIP PDU with the given content. It is possible to change the values in header and data, to drop the PDU, and to reduce the length of the payload. Only DoIP PDUs with valid layout are sent.

## Return Values

-1: Drop this PDU. This might violate the DoIP protocol.

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

| Since Version |
|---|
