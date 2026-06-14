# J1939ILSetMsgEvent

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILSetMsgEvent( dbMessage msg ); // form 1
```

## Description

The message is send immediately, the send type is ignored. The J1939 IL must be in state active and the message must be assigned to the node as Tx message.

To modify signal values prior to message transmission the CAPL functions J1939ILSetSignal or J1939ILSetSignalRaw can be used.

## Example

```c
on key 't'
{
 J1939ILSetMsgEvent( EC1 );
}
```

## Availability

| Since Version |
|---|
