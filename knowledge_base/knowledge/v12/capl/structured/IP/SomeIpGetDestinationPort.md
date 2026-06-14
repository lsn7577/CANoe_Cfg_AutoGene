# SomeIpGetDestinationPort

> Category: `IP` | Type: `function`

## Syntax

```c
dword SomeIpGetDestinationPort ( dword messageHandle );
```

## Description

This function returns the destination port (UDP/TCP).

## Parameters

| Name | Description |
|---|---|
| Note This function can only be called within the OnSomeIpMessage callback function. |  |

## Return Values

Destination port.
In the Event of an error, the function returns the value 0. The SomeIpGetLastError function can then be used to check whether the value is valid or an error has occurred.

## Example

```c
void OnSomeIpMessage( DWORD messageHandle )
{
  DWORD dstPort       = 0;
  LONG  errorCode     = 0;
  LONG  errorOccured  = 0;

  // get data from SOME/IP message
  if((dstPort = SomeIpGetDestinationPort(messageHandle)) == 0)
  {
    // check if last function was executed correct
    if((errorCode = SomeIpGetLastError()) != 0)
    {
      write("SOME/IP IL error occured: Error code: %d", errorCode);
      errorOccured = 1;
    } // if
  } // if

  if(errorOccured == 0)
  {
    write("SOME/IP message received. Destination Port: %d",dstPort);
  } // if
}
```

## Availability

| Since Version |
|---|
