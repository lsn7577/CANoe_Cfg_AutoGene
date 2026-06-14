# ILNodeControlMsg

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
ILNodeControlMsg(dbMessage msg, dword control, dword flags, dword param1, dword param2); // form 1
```

## Description

This generic function influences the sending of a certain message of a simulation node with an assigned CANoe Interaction Layer. The meaning of the parameters flags, param1 and param2 depends on the parameter control.

## Return Values

0: No error

## Availability

| Since Version |
|---|
