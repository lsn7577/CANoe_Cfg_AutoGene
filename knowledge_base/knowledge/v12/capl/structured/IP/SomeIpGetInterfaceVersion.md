# SomeIpGetInterfaceVersion

> Category: `IP` | Type: `function`

## Syntax

```c
dword SomeIpGetInterfaceVersion ( dword messageHandle );
```

## Description

This function returns the Interface Version from the SOME/IP message header.

## Return Values

Interface Version
In the Event of an error, the function returns the value 0. The SomeIpGetLastError function can then be used to check whether the value is valid or an error has occurred.

## Example

```c
void OnSomeIpMessage( DWORD messageHandle )
{
  DWORD interfaceVers = 0;
  LONG  errorCode = 0;
  LONG  errorOccured  = 0;

  // get data from SOME/IP message
  if((interfaceVers = SomeIpGetInterfaceVersion(messageHandle)) == 0)
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
    write("SOME/IP message with Interface Version 0x%02x (%d) received",interfaceVers,interfaceVers);
  } // if
}
```

## Availability

| Since Version |
|---|
