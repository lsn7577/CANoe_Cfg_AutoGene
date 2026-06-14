# J1939ILSetMsgRawData

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILSetMsgRawData(dbMessage msg, long dataSize, byte data[] ); // form 1
```

## Description

Sets the data bytes of the message. The length of the parameter group is adjusted to size of parameter dataSize.

## Example

```c
on key 't'
{
  char data[10] = "TPMS*V1.0*";
 J1939ILSetMsgRawData( ECUID, elCount(data), data );
}
```

## Availability

| Since Version |
|---|
