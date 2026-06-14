# diagSetCurrentEcu

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long diagSetCurrentEcu (char[] qualifier)
```

## Description

When the current diagnostic target is a physical network request description, select the given ECU as target for single physical requests.

This function is only supported for physical network requests. If a request is sent using diagSendRequest, and not diagSendNetwork, the request is sent physically to the current ECU alone.

## Return Values

Error code

## Example

```c
// Select a physical network request description as target
diagSetTarget( "PNR1");
// Send request to all targets on the network
req1.SendNetwork();

// Collect all responses from all ECUs
while( 1 == TestWaitForDiagResponse( req1, 1000))
{
  diagGetCurrentEcu( current, elcount(current));
  write( "Received response from %s", current);
}

if( current[0] != 0)
{
  // If there was a response, chose the last ECU to send another request to
  diagSetCurrentEcu( current);
  req2.SendRequest();
}
```

## Availability

| Up to Version |
|---|
