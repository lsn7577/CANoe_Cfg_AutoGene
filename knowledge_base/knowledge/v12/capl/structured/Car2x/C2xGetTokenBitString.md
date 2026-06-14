# C2xGetTokenBitString

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetTokenBitString( long packet, char protocolDesignator[], char tokenDesignator[], long bufferSize, byte buffer[]); // form 1
```

## Description

This function gets the bit string value of a token.

## Return Values

0 on success or error code

## Example

```c
byte brakePedalActive(long channel, longdir, longradioChannel, long signalStrength, long sigQuality, long packet)
{
  byte accelerationControl[1];

  if (C2xGetTokenBitString(packet, "CAM", "cam.camParameters.highFrequencyContainer.basicVehicleContainerHighFrequency.accelerationControl", 7, accelerationControl))
  {
    return accelerationControl[0] & 0x80;
  }
  return 0;
}
```

## Availability

| Since Version |
|---|
