# on diagResponse

> Category: `Diagnostics` | Type: `event`

## Syntax

```c
on diagResponse
```

## Description

The procedure is sub-divided into the following events; the first matching event procedure (top-down) is called:

Is called when a response from the indicated ECU (specified with its ECU qualifier) is received in the tester, that belongs to the indicated diagnostic service.

This is especially useful in situations where the tester program communicates with more than one diagnostic targets, e.g. sending functional requests.

Is called when a response is received in the tester that belongs to the indicated diagnostic service.

Is called when the service of the response received belongs to the specified class and instance. If an ECU qualifier is given, the procedure is called only when the response was sent by this ECU.

This procedure may therefore be called for several services!

Is called when the service of the response received belongs to the specified class. If an ECU qualifier is given, the procedure is called only when the response was sent by this ECU.

Is called when no other event procedure matches. If an ECU qualifier is given, the procedure is called only when the response was sent by this ECU.

Please note that, after every sending of a request, all responses are signaled only to the sender. Diagnostic requests that are sent from the Diagnostic Console are thus invisible for a CAPL program as are the received responses. Similarly, no responses to requests sent from a CAPL program are displayed in the Diagnostic Console.

When the procedure is called in the analysis branch of the Measurement Setup, only a fraction of the diagnostic functions is available.

Please refer to Diagnostics Event Handlers in Measurement Setup for details. The event must be forwarded with output(this) if processing shall continue in blocks of the Measurement Setup.

_______________________

(1) While the CANdela process knows the concept of a "diagnostic instance", ODX does not. Starting with CANoe 7.0 it is possible to use new unique service qualifiers, while CAPL programs for earlier CANoe versions might indicate the equivalent long qualifier path.

It is not recommended to mix these forms of declaration!

## Example

```c
// Indicate all responses in the write window
diagResponse *
{
  char objectPath[200];
  char currentEcu[100];
  this.GetObjectPath(objectPath, elcount(objectPath));
  DiagGetCurrentEcu(currentEcu, elcount(currentEcu));

  write( "Response %s from ECU %s", objectPath, currentEcu);
  output(this); // forward down the measurment branch
}
```

## Availability

| Since Version |
|---|
