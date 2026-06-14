# _DoIP_TCPDataInd

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void _DoIP_TCPDataInd( BYTE DoIPVersion, WORD payloadType, BYTE pay-load[]);
```

## Description

A DoIP PDU was received from the connected peer that cannot be interpreted by this implementation.

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

| Since Version |
|---|
