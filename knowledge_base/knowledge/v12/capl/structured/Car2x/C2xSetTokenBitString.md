# C2xSetTokenBitString

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSetTokenBitString( long packet, char protocolDesignator[], char tokenDesignator[], long bufferSize, byte buffer[] ); // form 1
```

## Description

This function sets the bit string of a token.

## Return Values

0 on success or error code

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

| Since Version |
|---|
