# on diagRequestSent

> Category: `Diagnostics` | Type: `event`

## Description

The procedure is sub-divided into the following events; the first matching event procedure (top-down) is called:

## Example

Example 1

Example 2

For event handlers, it is also possible to specify an ECU qualifier to filter specific events. And all services that belong to the same diagnostic class can be processed in one handler.

```c
on diagRequestSent *
{
   // A request was sent, therefore on LIN the schedule has to be changed
   linChangeSchedTable( cSchedulingTableForDiagResponse);
}

on diagRequestSent ECU_SoftReset
{
   // The ECU will perform a reset for some time, so inform the rest of the CAPL program
   gECUisResetting = 1;
}
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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 | 7.5 | — | — | — | 1.0 |
| Restricted To | — | — | — | — | — | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
