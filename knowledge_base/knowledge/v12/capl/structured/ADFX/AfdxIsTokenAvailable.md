# AfdxIsTokenAvailable

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxIsTokenAvailable( long packet, char protocolDesignator[], char tokenDesignator[] );
```

## Description

This function checks, if the specified token is part of the packet.

## Example

```c
long packet;
byte seqNo = 0;

packet = AfdxInitPacket(0x0a022600, 0xe0e01a0f, 11121, 0x1a0f, 640);
//check if Sequence number is available already
if (!AfdxIsTokenAvailable(packet, "afdx","seqNo"))
{
  write("error!  SeqNo  is not available in AFDX-packet");
}
else
{
  // set SeqNo to specific value
  if (AfdxSetTokenInt(packet, "afdx", "SeqNo", 0, 1, 1, seqNo) != 0)
  {
    write("error! AfdxSetTokenInt failed");
  }
}
```

## Availability

| Since Version |
|---|
