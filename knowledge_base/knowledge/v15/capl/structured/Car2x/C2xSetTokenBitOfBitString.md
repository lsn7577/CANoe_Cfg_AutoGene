# C2xSetTokenBitOfBitString

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSetTokenBitOfBitString( long packet, char protocolDesignator[], char tokenDesignator[], char namedBit[], long value ); // form 1
long C2xSetTokenBitOfBitString( long packet, char protocolDesignator[], char tokenDesignator[], long bitPosition, long value ); // form 2
```

## Description

This function sets a bit of a bit string that is specified either by its name (form 1) or by its position (form 2) to a new value.

If the bit string does not yet contain the specified bit the bit string is resized up to the specified bit. On resizing the new bits before the specified bit are set to 0.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of a packet that has been created with C2xInitPacket. |
| protocolDesignator | Name of the protocol, e.g. geo_cnh. |
| tokenDesignator | Name of the token, e.g. data. |
| namedBit | Name of the bit. |
| bitPosition | Zero based index of the bit. |
| value | New value of the bit. |

## Example

```c
long packetHandle;
long result;

packetHandle = C2xInitPacket("userDefinedPayload");
if ((result = C2xSetTokenBitOfBitString(packetHandle, "userDefinedPayload","bitString", "secondBitsName", 1)) == 0)
{
  //bit string "bitString" now has the value "01"
}
else if (result == 460103)
{
  //Invalid Argument – in this case this most probably means
  //that the passed bit name "secondBitsName" is unknown
}
else
{
  //other error
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.6 SP4: form 1, 2 | — | — | — | 2.1 SP3: form 1, 2 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
