# VTIL_SetMsgEvent

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_SetMsgEvent( dbMessage msg );
```

## Description

The message is send immediately, the send type is ignored. The VT IL must be in state active and the message must be assigned to the node as Tx message.

To modify signal values prior to message transmission the CAPL functions VTIL_SetSignal or VTIL_SetSignalRaw can be used.

## Return Values

0: Function has been executed successfully

## Example

```c
on key 'i'
{
 VTIL_SetMsgEvent( ICC_VT );
}
```

## Availability

| Since Version |
|---|
