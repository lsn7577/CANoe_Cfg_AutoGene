# DoIP_DataReq

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_DataReq( byte buffer[], dword count, dword vehicleAddress, dword testerAddress);
```

## Description

Request the transfer of the given data to the DoIP peer.

## Return Values

—

## Example

```c
_Diag_DataRequest( BYTE data[], DWORD count,
                   long furtherSegments)
{
   // send data via DoIP
   DoIP_DataReq( data, count, gDoIPAddress, 0);
}
```

## Availability

| Since Version |
|---|
