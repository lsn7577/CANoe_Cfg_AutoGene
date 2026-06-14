# AREthGetReturnCode

> Category: `IP` | Type: `function`

## Syntax

```c
dword AREthGetReturnCode ( dword messageHandle );
```

## Description

This function returns the Return Code from the SOME/IP message header.

## Return Values

Return Code
If message type is REQUEST, REQUEST_NO_RETURN or NOTIFICATION return code is N/A and set to 0x00 (E_OK).
In the Event of an error, the function returns the value 0. The AREthGetLastError function can then be used to check whether the value is valid or an error has occurred.

## Example

```c
void OnAREthMessage( dword messageHandle )
{
  dword retCode       = 0;
  LONG  errorCode     = 0;
  LONG  errorOccured  = 0;

  // get data from SOME/IP message
  if((retCode = AREthGetReturnCode(messageHandle)) == 0)
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
    write("SOME/IP message with Return Code 0x%02x received",retCode);
  } // if
}
```

## Availability

| Since Version |
|---|
