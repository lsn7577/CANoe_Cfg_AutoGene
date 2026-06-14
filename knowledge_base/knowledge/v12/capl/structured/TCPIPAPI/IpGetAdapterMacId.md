# IpGetAdapterMacId

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetAdapterMacId( dword ifIndex, byte macId[]); // form 1
```

## Description

The function returns the MAC ID of the given interface.

## Return Values

Form 1: 0: The function completed successfully.

## Example

```c
on start
{
  long result;
  long ifIndex;
  char adapterDesc[255];
  byte macId[6];

  ifIndex = 1;

  result = ipGetAdapterDescription(ifIndex, adapterDesc, elcount(adapterDesc));
  if( result != 0 )
  {
    writeLineEx(1, 3, "Failed to get the adapter description. Result: %d", result);
  }

  result = IpGetAdapterMacId(ifIndex, macId);
  if( result != 0 )
  {
    writeLineEx(1, 3, "Failed to get the adapter MAC ID. Result: %d", result);
  }
  else
  {
    writeLineEx(1, 0, "The Mac Id of Adapter %s is %02x:%02x:%02x:%02x:%02x:%02x",
    adapterDesc, macId[0], macId[1], macId[2], macId[3], macId[4], macId[5]);
  }
}
```

## Availability

| Since Version |
|---|
