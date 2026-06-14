# VTIL_SetMsgRawData

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_SetMsgRawData( dbMessage msg, long dataSize, byte data[] );
```

## Description

Sets the data bytes of the message. The length of the parameter group is adjusted to size of parameter dataSize.

## Return Values

0: Function has been executed successfully

## Example

```c
void SendPointingEvent(word x, word y, byte touchState)
{
  char buf[8];
  buf[0] = 0x02; // Pointing Event
  buf[1] = x & 0xFF;
  buf[2] = (x >> 8) & 0xFF;
  buf[3] = y & 0xFF;
  buf[4] = (y >> 8) & 0xFF;
  buf[5] = touchState;
  buf[6] = 0xFF;
  buf[7] = 0xFF;
  VTIL_SetMsgRawData(VT12_VT, elCount(buf), buf);
  VTIL_SetMsgEvent(VT12_VT);
}
```

## Availability

| Since Version |
|---|
