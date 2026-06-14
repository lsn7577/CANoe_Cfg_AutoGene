# on diagRequest

> Category: `Diagnostics` | Type: `event`

## Syntax

```c
on diagRequest
```

## Description

In case Additional Diagnostic Descriptions are configured for the ECU, the first description with a matching definition for the PDU is searched in the interpretation order. Otherwise the diagnostic description assigned to the simulation is used immediately. Then the first matching event procedure (top-down) is called.

Is called when a request is received in the ECU simulation that belongs to the indicated diagnostic service.

Is called when the service of the request received belongs to the specified class and instance.

This procedure may therefore be called for several services!

Is called when the service of the request received belongs to the specified class.

Is called when no other event procedure matches.

Please note that, after every sending of a request, all responses are signaled only to the sender. Diagnostic requests that are sent from the Diagnostic Console are thus invisible for a CAPL program as are the received responses. Similarly, no responses to requests sent from a CAPL program are displayed in the Diagnostic Console.

When the procedure is called in the analysis branch of the Measurement Setup, only a fraction of the diagnostic functions is available.

Please refer to Diagnostics Event Handlers in Measurement Setup for details. The event must be forwarded with output(this) if processing shall continue in blocks of the Measurement Setup.

_______________________

(1) While the CANdela process knows the concept of a "diagnostic instance", ODX does not. Starting with CANoe 7.0 it is possible to use new unique service qualifiers, while CAPL programs for earlier CANoe versions might indicate the equivalent long qualifier path.

It is not recommended to mix these forms of declaration!

## Example

Also, mixing diagnostic requests from a master description and any of its additional descriptions is possible without setting a target.

```c
GetSomeInfo()
{
  DiagRequest ECU1.Service1 req1;
  DiagRequest ECU1.Additional1.ServiceA req2;

  // DiagSetTarget is NOT necessary!

  // Put both requests in the send queue of the integrated channel
  req1.SendRequest();
  req2.SendRequest();

  // Wait for the responses that must arrive in sending order since
  // the requests are sent on the same channel
  TestWaitForDiagResponse( req1, 1000);
  TestWaitForDiagResponse( req2, 1000);

  // ... access responses via the requests
  write( "Service1: %f", req1.GetRespParameter( "Param1");
  write( "ServiceA: %f", req2.GetRespParameter( "ParamA");
}
```

## Availability

| Since Version |
|---|
