# C2xSetTokenBitOfBitString

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSetTokenBitOfBitString( long packet, char protocolDesignator[], char tokenDesignator[], char namedBit[], long value ); // form 1
```

## Description

This function sets a bit of a bit string that is specified either by its name (form 1) or by its position (form 2) to a new value.

If the bit string does not yet contain the specified bit the bit string is resized up to the specified bit. On resizing the new bits before the specified bit are set to 0.

## Return Values

0 or error code

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

| Since Version |
|---|
