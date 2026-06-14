# TestWaitForEthernetLinkStatus

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForEthernetLinkStatus(long channel, long status, dword aTimeout); // form 1
long TestWaitForEthernetLinkStatus(long channel, Int64 hwChannel, long status, dword aTimeout); // form 2
long TestWaitForEthernetLinkStatus(ethernetport hwport, long status, dword aTimeout); // form 3
```

## Description

Waits for the occurrence of the specified Ethernet link status. Should the Ethernet link status not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless. If the Ethernet link has already the expected state, the function returns immediately with return value 1.

## Parameters

| Name | Description |
|---|---|
| channel | Ethernet channel number.Value range: 1..32 |
| hwChannel | Ethernet hardware channel number.Value range: 1..64 |
| hwPort | Hardware port qualifier. |
| Status | Wait for this status: 0 = link down 1 = link up |
| aTimeout | Maximum time that should be waited [ms] (Transmission of 0: no timeout controlling). |

## Example

```c
void MainTest ()
{
  long result;
  dword timeout;
  ethernetport myEthernetPort;

  // form 1 - waits for link status up to occur on channel 1
  result = TestWaitForEthernetLinkStatus(1, 1, timeout);

  // form 2 - waits for link status up to occur on hardware channel 3 of channel 1
  result = TestWaitForEthernetLinkStatus(1, 3, 1, timeout);

  // form 3 - waits for link status down to occur on myEthernetPort;
  result = TestWaitForEthernetLinkStatus(myEthernetPort, 0, timeout);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 SP3 | 13.0 | — | — | 4.0 SP3 |
| Restricted To | — | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
