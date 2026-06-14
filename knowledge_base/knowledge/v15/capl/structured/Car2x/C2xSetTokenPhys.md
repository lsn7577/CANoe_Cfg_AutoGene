# C2xSetTokenPhys

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSetTokenPhys(long packet, char[] protocolDesignator, char[] tokenDesignator, double value)
```

## Description

This function sets the physical value of the token in the packet. This function succeeds only if following requirements apply:

## Parameters

| Name | Description |
|---|---|
| packet | Handle of a packet that has been created with C2xInitPacket or was provided as callback function parameter. |
| protocolDesignator | Name of the protocol, e.g. CAM. |
| tokenDesignator | Name of the ASN.1 token, e.g. cam.camParameters.basicContainer.referencePosition.latitude. |
| value | The physical value of the token. |

## Example

```c
void OnPreTxDENM(LONG packet)
{
  C2xSetTokenPhys(packet, "DENM", "denm.management.eventPosition.latitude", 10.11);
  C2xSetTokenPhys(packet, "DENM", "denm.management.eventPosition.longitude", -2.2);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | — | — | — | 5.0 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
