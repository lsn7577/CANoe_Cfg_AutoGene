# SomeIpGetReturnCode

> Category: `IP` | Type: `function`

## Syntax

```c
dword SomeIpGetReturnCode ( dword messageHandle );
```

## Description

This function returns the Return Code from the SOME/IP message header.

## Return Values

Return Code
If message type is REQUEST, REQUEST_NO_RETURN or NOTIFICATION return code is N/A and set to 0x00 (E_OK).
In the Event of an error, the function returns the value 0. The SomeIpGetLastError function can then be used to check whether the value is valid or an error has occurred.

## Example

```c
void OnSomeIpMessage( DWORD messageHandle )
{
  DWORD retCode       = 0;
  LONG  errorCode     = 0;
  LONG  errorOccured  = 0;

  // get data from SOME/IP message
  if((retCode = SomeIpGetReturnCode(messageHandle)) == 0)
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
    write("SOME/IP message with Return Code 0x%02x received",retCode);
  } // if
}
```

## Availability

| Since Version |
|---|
