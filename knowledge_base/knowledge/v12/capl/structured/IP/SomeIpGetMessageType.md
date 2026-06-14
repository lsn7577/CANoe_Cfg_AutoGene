# SomeIpGetMessageType

> Category: `IP` | Type: `function`

## Syntax

```c
dword SomeIpGetMessageType ( dword messageHandle );
```

## Description

This function returns the Message Type from the SOME/IP message header.

## Return Values

Message Type
In the Event of an error, the function returns the value 0. The SomeIpGetLastError function can then be used to check whether the value is valid or an error has occurred.

## Example

```c
void OnSomeIpMessage( DWORD messageHandle )
{
  DWORD msgType       = 0;
  LONG  errorCode     = 0;
  LONG  errorOccured  = 0;

  // get data from SOME/IP message
  if((msgType = SomeIpGetMessageType(messageHandle)) == 0)
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
    write("SOME/IP message with Message Type 0x%02x received",msgType);
  } // if
}
```

## Availability

| Since Version |
|---|
