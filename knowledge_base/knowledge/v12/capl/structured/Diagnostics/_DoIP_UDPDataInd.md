# _DoIP_UDPDataInd

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void _DoIP_UDPDataInd( char IPaddress[], BYTE data[]);
```

## Description

An UDP packet was received that cannot be interpreted by this DoIP implementation. The senders IP address is given as first argument, in text form.

Since the DoIP implementation is extended over time, the number of unknown packet types will be reduced. To process all UDP packets use the callback function _DoIP_UDPInd. It is called for every UDP packet received before any processing is done.

## Return Values

—

## Example

```c
void _DoIP_UDPDataInd( char IPaddress[], BYTE data[])
{
  write( "_DoIP_UDPDataInd( '%s', [%d]<%02x ...>)", IPaddress
  , elcount( data), elcount(data) > 0 ? data[0] : 0);
}
```

## Availability

| Since Version |
|---|
