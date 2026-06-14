# C2xSetTokenBitString

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSetTokenBitString( long packet, char protocolDesignator[], char tokenDesignator[], long bufferSize, byte buffer[] ); // form 1
long C2xSetTokenBitString( long packet, char protocolDesignator[], char tokenDesignator[], long bufferSize, char buffer[] ); // form 2
```

## Description

This function sets the bit string of a token.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of a packet that has been created with C2xInitPacket. |
| protocolDesignator | Name of the protocol, e.g. userDefinedPayload. |
| tokenDesignator | Name of the token, e.g. bitString. |
| bufferSize | Size of buffer in bits. |
| buffer | Buffer in which the data is copied. |

## Example

```c
void accelCtrl(long packet, byte value)
{
  byte accelerationControl[1];
  accelerationControl[0] = value;

  C2xSetTokenBitString(packet, "CAM", "cam.camParameters.highFrequencyContainer.basicVehicleContainerHighFrequency.accelerationControl", 7, accelerationControl);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.6 SP4 | — | — | — | 2.1 SP3 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
