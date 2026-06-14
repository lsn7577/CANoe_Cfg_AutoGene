# GBT27930IL_SetMsgRawData

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_SetMsgRawData(dbMessage msg, long dataSize, byte data[] ); // form 1
```

## Description

Sets the data bytes of the message. The length of the parameter group is adjusted to size of parameter dataSize.

## Example

```c
on key 't'
{
  char data[10] = "TPMS*V1.0*";
 GBT27930IL_SetMsgRawData( ECUID, elCount(data), data );
}
```

## Availability

| Since Version |
|---|
