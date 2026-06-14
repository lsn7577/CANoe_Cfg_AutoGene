# C2xGetTokenPhys

> Category: `Car2x` | Type: `function`

## Syntax

```c
double C2xGetTokenPhys(long packet, char[] protocolDesignator, char[] tokenDesignator)
```

## Description

This function returns the physical value of the existing ASN.1 token in the packet. This function succeeds only if following requirements apply:

## Parameters

| Name | Description |
|---|---|
| packet | Handle of a packet that has been created with C2xInitPacket or was provided as callback function parameter |
| protocolDesignator | Name of the protocol, e.g. CAM |
| tokenDesignator | Name of the ASN.1 token, e.g. cam.camParameters.basicContainer.referencePosition.latitude |

## Return Values

With C2xGetLastError you can check if the function has been processed successfully.
Example

## Example

```c
void OnPreTxDENM(LONG packet)
{
  write("DENM event positition latitude %f°", C2xGetTokenPhys(packet, "DENM" "denm.management.eventPosition.latitude"));
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
