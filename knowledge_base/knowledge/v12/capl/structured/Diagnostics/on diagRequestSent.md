# on diagRequestSent

> Category: `Diagnostics` | Type: `event`

## Syntax

```c
on diagRequestSent
```

## Description

The procedure is sub-divided into the following events; the first matching event procedure (top-down) is called:

Is called when a request is sent completely in the Tester simulation that belongs to the indicated diagnostic service.

Is called when the service of the sent request belongs to the specified class.

Is called when no other event procedure matches.

This procedure may therefore be called for several services!

Please note that, after every sending of a request, all responses are signaled only to the sender. Diagnostic requests that are sent from the Diagnostic Console are thus invisible for a CAPL program as are the received responses. Similarly, no responses to requests sent from a CAPL program are displayed in the Diagnostic Console.

## Example

For event handlers, it is also possible to specify an ECU qualifier to filter specific events. And all services that belong to the same diagnostic class can be processed in one handler.

```c
// process all diagnostic requests from ECU1 without better match here
On diagResponse ECU1.*
{
  // access the response using 'this'
}

// Only Service1 responses from ECU1 will be reported here
On diagResponse ECU1.Service1
{
}

On diagRequestSent ECU2.*
{
  // ECU2 is using a transport protocol with confirmations
Write( "ECU2 has confirmed reception of event");
}

On diagResponse ECU1.Class1::*
{
  write( "A response for a service of Class1 was received");
}
```

## Availability

| Since Version |
|---|
