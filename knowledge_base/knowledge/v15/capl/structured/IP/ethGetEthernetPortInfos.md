# ethGetEthernetPortInfos

> Category: `IP` | Type: `function`

## Syntax

```c
long ethGetEthernetPortInfos (ethernetportinfo portInfos[]);
```

## Description

Retrieves port related information of all connected network-based Ethernet devices.

You must provide an array of ethernetPortInfo elements of sufficient size for all available hardware ports.

## Parameters

| Name | Description |
|---|---|
| portInfos | Array of type <ethernetPortInfo>, which contains the retrieved hardware info as a struct with the following members: char PortName[32] char NetworkName[32] char SegmentName[32] uint32_t IsPhysical |

## Return Values

Number of valid ethernetPortInfo elements (0 in case of any error).

## Example

```c
on key 'C'  // retrieve complete hardware info
{
  ethernetportinfo  allPorts[128];
  long numPorts, j;
  numPorts = ethGetEthernetPortInfos(allPorts);
  write("Found hardware info of %d ports ", numPorts);
  for (j=0; j < numPorts; j++)
  {
    write("#%d %s::%s::%s isPhy:%d", j,
      allPorts[j].NetworkName,
      allPorts[j].SegmentName,
      allPorts[j].PortName,
      allPorts[j].IsPhysical);
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 12.0 SP4 | 12.0 SP4 | 13.0 | — | — | 5.0 |
| Restricted To | Ethernet | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
