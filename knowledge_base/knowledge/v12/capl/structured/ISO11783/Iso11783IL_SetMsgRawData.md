# Iso11783IL_SetMsgRawData

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_SetMsgRawData( dbMessage msg, long dataSize, byte data[] );
```

## Description

Sets the data bytes of the message. The length of the parameter group is adjusted to size of parameter dataSize.

## Example

```c
on key 't'
{
  char data[10] = "TPMS*V1.0*";
 Iso11783IL_SetMsgRawData( ECUID, elCount(data), data );
}
```

## Availability

| Since Version |
|---|
