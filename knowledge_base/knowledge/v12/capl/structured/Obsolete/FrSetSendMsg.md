# FrSetSendMsg

> Category: `Obsolete` | Type: `function`

## Syntax

```c
FrSetSendMsg ( class VIMessage* const message, unsigned int channel )
```

## Description

Frames to be transmitted by the xModule/PC104 must first be registered in the Service Module.

The message can be selected via the associated databases.

The registration must occur in the on preStart routine in the Tx branch.

## Example

```c
variables
{
   message Identifier_01 msg_01;
   int gChannel_2 = 2;
int gId_02 = 2;
int gMux = 1;
int gNoSync = 0;
int gLen_Id2 = 4;
   Byte gData2a[12] = {0x21,0x22,0x23,0x24,0x25,0x26,0x27,0x28,0x29,0x2a,0x2b,0x2c};
Byte gData1a[12] = {0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0a,0x0b,0x0c};
}
on key 'z'
{
   FrSendFrame(gId_02, gNoMux, gChannel_2, gNoSync, gLen_Id2, gData2a, -1 );
   FrSendMsg (msg_01, gChannel_2, gData1a );
}
```

## Availability

| Up to Version |
|---|
