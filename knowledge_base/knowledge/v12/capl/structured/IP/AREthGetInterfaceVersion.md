# AREthGetInterfaceVersion

> Category: `IP` | Type: `function`

## Syntax

```c
dword AREthGetInterfaceVersion ( dword messageHandle );
```

## Description

This function returns the Interface Version from the SOME/IP message header.

## Return Values

Interface Version
In the Event of an error, the function returns the value 0. The AREthGetLastError function can then be used to check whether the value is valid or an error has occurred.

## Example

```c
void OnAREthMessage( dword messageHandle )
{
  dword interfaceVers = 0;
  LONG  errorCode = 0;
  LONG  errorOccured  = 0;

  // get data from SOME/IP message
  if((interfaceVers = AREthGetInterfaceVersion(messageHandle)) == 0)
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
    write("SOME/IP message with Interface Version 0x%02x (%d) received",interfaceVers,interfaceVers);
  } // if
}
```

## Availability

| Since Version |
|---|
