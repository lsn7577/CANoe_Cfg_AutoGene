# TestWaitForLinSpike

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForLinSpike (dword aTimeout);
```

## Description

Waits for the occurrence of a LIN Spike event. Should the event not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

## Parameters

| Name | Description |
|---|---|
| aTimeout | Maximum time that should be waited [ms]. (Transmission of 0: no timeout controlling) |

## Example

```c
testcase tcTFS_linSpikeEvent ()
{
   linSpikeEvent linSpikeEventData;
   if (testWaitForLinSpike (5000) == 1)
   {
      if (testGetWaitLinSpikeData(linSpikeEventData) == 0)
      {
         testStep("Evaluation", "LIN Spike event occurred. Signal length is %d ns", linSpikeEventData.length_ns);
      }
   }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 | 13.0 | — | — | 1.0 |
| Restricted To | — | LIN | LIN | — | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
