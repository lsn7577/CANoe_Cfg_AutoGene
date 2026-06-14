# FSIL_SetMsgEvent

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long FSIL_SetMsgEvent( dbMessage msg );
```

## Description

The message is send immediately, the send type is ignored. The FS IL must be in state active and the message must be assigned to the node as Tx message.

To modify signal values prior to message transmission the CAPL functions FSIL_SetSignal or FSIL_SetSignalRaw can be used.

## Return Values

0: Function has been executed successfully

## Example

```c
on key 'i'
{
 FSIL_SetMsgEvent( ICC_FS );
}
```

## Availability

| Since Version |
|---|
