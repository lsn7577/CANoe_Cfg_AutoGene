# on diagRequest

> Category: `Diagnostics` | Type: `event`

## Description

In case Additional Diagnostic Descriptions are configured for the ECU, the first description with a matching definition for the PDU is searched in the interpretation order. Otherwise the diagnostic description assigned to the simulation is used immediately. Then the first matching event procedure (top-down) is called.

_______________________

(1) While the CANdela process knows the concept of a "diagnostic instance", ODX does not. Starting with CANoe 7.0 it is possible to use new unique service qualifiers, while CAPL programs for earlier CANoe versions might indicate the equivalent long qualifier path.

It is not recommended to mix these forms of declaration!

## Example

Example 1 Simulation Setup

Example 2 Measurement Setup

Example 3

Starting with CANoe 9.0 SP3 The CAPL compiler supports diagnostic objects that are declared with an ECU qualifier or target (like a functional group). This allows the compiler to check if the diagnostic service used to initialize the object is defined in the diagnostic description of the ECU/target. If not, a compile error will be reported.

Example 4

Specifying a target in the declaration of a diagnostic object has the benefit that it is NOT necessary to call DiagSetTarget, and it is possible to communicate with several targets in parallel.

Example 5

Also, mixing diagnostic requests from a master description and any of its additional descriptions is possible without setting a target.

```c
on diagRequest FaultMemory_ReadAllIdentified
{
   diagResponse this resp;

   // Set the number of bytes needed to transfer the response with 2 DTCs (in this example: overall 11 bytes)
diagResize( resp, 11); // 3 Bytes Header (SID, Subfunction, AvailabilityMask) + 2 * 4 Bytes for DTCs = 11 bytes
   // Set the value of the DTCs
   diagSetComplexParameter ( resp, "ListOfDTC", 0, "DTC", 0x000001 );
   diagSetComplexParameter ( resp, "ListOfDTC", 0, "DtcStatusbyte", 0xF1 );
   diagSetComplexParameter ( resp, "ListOfDTC", 1, "DTC", 0x000002 );
   diagSetComplexParameter ( resp, "ListOfDTC", 1, "DtcStatusbyte", 0xF3 );

   diagSendResponse ( resp );
}
// Indicate all requests in the write window
diagRequest *
{
  char objectPath[200];
  char currentEcu[100];
  this.GetObjectPath(objectPath, elcount(objectPath));
  DiagGetCurrentEcu(currentEcu, elcount(currentEcu));

  write( "Request %s to ECU %s", objectPath, currentEcu);
  output(this); // forward down the measurment branch
}
On start
{
  DiagRequest ECU1.Service1 req1;			// OK since Service1 is defined for ECU1
  DiagRequest ECU1.NotExisting req2;		// compile error since service unknown
}
ParallelCommunication()
{
  DiagRequest ECU1.Service1 req1;
  DiagRequest ECU2.Service2 req2;

  // DiagSetTarget is NOT necessary!

  // Put the requests in the send queues of the integrated channels
  req1.SendRequest();
  req2.SendRequest();

  {
    // Since the order in which the responses will be received is not known,
    // join the response events to wait for them to arrive in any order
    long cond1;
    long cond2;
    long status;
    cond1 = testJoinDiagResponseFromEcu( "ECU1");
    cond2 = testJoinDiagResponseFromEcu( "ECU2");

    status = testWaitForAllJoinedEvents( 1000);
    if( cond1 == status || cond2 == status)
      testStepPass("Joined events received.");
    else
      testStepFail( "", "Waiting for all joined events returns %d", status);
  }
}
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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.0 SP3 | 7.0 SP3 | — | — | — | 1.0 |
| Restricted To | — | — | — | — | — | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ (since 9.0) | ✔ (since 9.0) | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
