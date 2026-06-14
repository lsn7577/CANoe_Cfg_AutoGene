# SomeIpGetProtocol

> Category: `IP` | Type: `function`

## Syntax

```c
dword SomeIpGetProtocol ( dword messageHandle );
```

## Description

This function returns the protocol (UDP/TCP) the SOME/IP message was transmitted with.

## Parameters

| Name | Description |
|---|---|
| Note This function can only be called within the OnSomeIpMessage callback function. |  |

## Return Values

protocol

## Example

```c
void OnSomeIpMessage( DWORD messageHandle )
{
  DWORD protocol      = 0;
  LONG  errorCode     = 0;
  LONG  errorOccured  = 0;

  // get data from SOME/IP message
  if((protocol = SomeIpGetProtocol(messageHandle)) == 0)
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
    write("SOME/IP message with Protocol Type 0x%x (%d) received",protocol,protocol);
  } // if
}
```

## Availability

| Since Version |
|---|
