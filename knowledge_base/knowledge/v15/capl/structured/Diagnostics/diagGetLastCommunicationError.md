# diagGetLastCommunicationError

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
syntax: long DiagGetLastCommunicationError();
```

## Description

Returns the error code of the last diagnostic request.

## Return Values

200: StartCommunication request wasn't answered by the ECU.
600: The requested function isn't supported.

## Example

```c
testcase TC()
{
  DiagRequest XY_Read req;
  int err;

  TestStep( "Test", "Step");
  DiagSetTarget("ECU");
  DiagSendRequest(req);
  if (0 == TestWaitForDiagResponse( req, 2000))
  {
    err = DiagGetLastCommunicationError();
    write("LastCommunicationError=%d", err);
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.2 | 8.2 | — | — | — | 1.1 |
| Restricted To | Online mode | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
