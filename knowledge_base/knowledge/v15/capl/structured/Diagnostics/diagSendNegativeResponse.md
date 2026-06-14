# diagSendNegativeResponse

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagSendNegativeResponse (diagResponse obj, DWORD code)
long diagSendNegativeResponse (diagRequest obj, DWORD code)
```

## Description

Sends a negative response to the tester, whereby the specified value is transmitted as error code.

## Parameters

| Name | Description |
|---|---|
| obj | Diagnostics object |
| code | Error code. |

## Return Values

Error code

## Example

```c
on diagRequest FaultMemory::FaultMemory::ReportByStatusMask
{
  // Send neg response with code 0x78 (requestCorrectlyReceived-ResponsePending)
  DiagSendNegativeResponse(this, 0x78);
  // Optionally set a timer to respond with a positive response later
  setTimer(posReq, 1);
  // pos resp after 1s
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 7.0 SP3: methods | — | — | — | 1.0 |
| Restricted To | — | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
