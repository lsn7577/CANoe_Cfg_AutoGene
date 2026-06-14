# on diagResponse

> Category: `Diagnostics` | Type: `event`

## Description

The procedure is sub-divided into the following events; the first matching event procedure (top-down) is called:

_______________________

(1) While the CANdela process knows the concept of a "diagnostic instance", ODX does not. Starting with CANoe 7.0 it is possible to use new unique service qualifiers, while CAPL programs for earlier CANoe versions might indicate the equivalent long qualifier path.

It is not recommended to mix these forms of declaration!

## Example

Example 1 - Simulation Setup

Example 2 - Measurement Setup

```c
// e.g. used in a Tester module
on diagResponse *
{
  byte data[4096];
  long size;
  double param_value1=0xFF;
  double param_value2=0xFF;
  diagResponse * resp; // declare response with no concrete interpretation
  size=this.GetPrimitiveSize();             // get length of response
  this.GetPrimitiveData(data, elcount(data));  // copy actual response from "on diagResponse *" into data array

  switch(data[0])
  {
    case 0x50: // UDS: DiagnosticSessionControl_Process positive Response
      diagInitialize(resp, "DiagnosticSessionControl_Process");
      resp.Resize(size); // make sure there is room for the received bytes
      resp.SetPrimitiveData(data, size);           // initialize resp with actual response from data array
      param_value1=diagGetParameter(resp, "diagnosticSessionType");
      param_value2=diagGetParameter(resp, "sessionParameterRecord");
      break;
    case 0x51: // UDS: EcuReset_Process positive Response
      diagInitialize(resp, "EcuReset_Process");
      resp.Resize(size); // make sure there is room for the received bytes
      resp.SetPrimitiveData(data, size);           // initialize resp with actual response from data array
      param_value1=diagGetParameter(resp, "resetType");
      param_value2=diagGetParameter(resp, "powerDownTime");
      break;
    default:
      break;
  }
  write("Tester: Value of parameter according to chosen interpretation: 0x%x 0x%x %3.0lf %3.0lf",data[0], data[1], param_value1, param_value2);
}
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
