# TCIL_SetMsgEvent

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_SetMsgEvent( dbMessage msg );
```

## Description

The message is send immediately, the send type is ignored. The TC IL must be in state active and the message must be assigned to the node as Tx message.

To modify signal values prior to message transmission the CAPL functions TCIL_SetSignal or TCIL_SetSignalRaw can be used.

## Return Values

0: Function has been executed successfully

## Example

```c
on key 'i'
{
 TCIL_SetMsgEvent( ICC_TC );
}
```

## Availability

| Since Version |
|---|
