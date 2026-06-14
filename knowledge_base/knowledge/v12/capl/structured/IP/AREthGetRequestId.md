# AREthGetRequestId

> Category: `IP` | Type: `function`

## Syntax

```c
dword AREthGetRequestId ( dword messageHandle );
```

## Description

This function returns the Request ID from the SOME/IP message header.

## Return Values

Request ID
In the Event of an error, the function returns the value 0. The AREthGetLastError function can then be used to check whether the value is valid or an error has occurred.

## Example

```c
void OnAREthMessage( dword messageHandle )
{
  dword requestId    = 0;
  LONG  errorCode    = 0;
  LONG  errorOccured = 0;

  // get data from SOME/IP message
  if((requestId = AREthGetRequestId(messageHandle)) == 0)
  {
    // check if last function was executed correct
    if((errorCode = AREthGetLastError()) != 0)
    {
      write("AUTOSAR Eth IL error occured: Error code: %d", errorCode);
      errorOccured = 1;
    } // if
  } // if

  if(errorOccured == 0)
  {
    write("SOME/IP message with Request ID 0x%08x received",requestId);
  } // if
}
```

## Availability

| Since Version |
|---|
