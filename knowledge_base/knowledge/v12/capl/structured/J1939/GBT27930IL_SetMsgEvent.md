# GBT27930IL_SetMsgEvent

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_SetMsgEvent( dbMessage msg ); // form 1
```

## Description

The message is send immediately, the send type is ignored. The GBT27930 IL must be in state active and the message must be assigned to the node as Tx message.

To modify signal values prior to message transmission the CAPL functions GBT27930IL_SetSignal or GBT27930IL_SetSignalRaw can be used.

## Example

```c
on key 't'
{
 GBT27930IL_SetMsgEvent( EC1 );
}
```

## Availability

| Since Version |
|---|
