# diagSendFunctional

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagSendFunctional( diagRequest request)
```

## Description

Send a request to the functional group defined for the current target. The configuration of the functional transport protocol settings in the description configuration dialog must be present and consistent.

## Parameters

| Name | Description |
|---|---|
| request | The request to be sent. |

## Return Values

Error code

## Example

```c
on key 'f'
{
  diagRequest Serial_Number_Read req;
  long ret;
  if (0 != (ret=diagSetTarget("ECU1"))) write("diagSetTarget() failed with error code %ld!", ret);
  // Send request on functional channel
  if (0 != (ret=diagSendFunctional(req))) write("diagSendFunctional() failed with error code %ld!", ret);
}

on key 'p'
{
  diagRequest Serial_Number_Read req;
  long ret;
  // reset functional to physical addressing, if necessary
  if (0 != (ret=diagSetTarget("ECU1"))) write("diagSetTarget() failed with error code %ld!", ret);
  // Send request on physical channel
  if (0 != (ret=diagSendRequest(req))) write("diagSendRequest() failed with error code %ld!", ret);
}

on diagResponse Serial_Number_Read
{
  char ser_no[30];
  diagGetParameter(this, "Serial_Number", ser_no, elcount(ser_no));
  write("Response from serial no.: %s",ser_no);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 | 7.2 SP3 | — | — | — | 1.0 |
| Restricted To | Online mode | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
