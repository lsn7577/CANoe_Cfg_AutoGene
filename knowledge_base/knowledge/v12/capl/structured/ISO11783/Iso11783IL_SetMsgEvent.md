# Iso11783IL_SetMsgEvent

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_SetMsgEvent( dbMessage msg );
```

## Description

The message is send immediately, the send type is ignored. The ISO11783 IL must be in state active and the message must be assigned to the node as Tx message.

To modify signal values prior to message transmission the CAPL functions Iso11783IL_SetSignal or Iso11783IL_SetSignalRaw can be used.

## Example

```c
on key 't'
{
 Iso11783IL_SetMsgEvent( EC1 );
}
```

## Availability

| Since Version |
|---|
