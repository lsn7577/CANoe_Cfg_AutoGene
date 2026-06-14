# TestJoinEthernetPhyState

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinEthernetPhyState(ethernetport hwport, long state);
```

## Description

Completes the current set of joined events with the transmitted event. This function does not wait.

## Parameters

| Name | Description |
|---|---|
| hwPort | Hardware port qualifier. |
| state | Wait for this state: 1: normal state 2: sleep state 3: power off state 4: sleep request |

## Example

```c
void MainTest ()
{
  long result;
  ethernetport myEthernetPort = ethernetport::Ethernet1::myPort;

  // form 1 - waits for PHY state “normal” to occur on myEthernetPort;
  result = TestWaitForEthernetPhyState(myEthernetPort, 0, timeout);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 15 | 15 | — | — | 6 |
| Restricted To | — | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
