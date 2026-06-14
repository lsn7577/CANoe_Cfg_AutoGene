# GPIBReqRelSysCtrl

> Category: `GPIB` | Type: `function`

## Syntax

```c
long GPIBReqRelSysCtrl (long boardIdx, long mode);
```

## Description

Sets or deletes the permission to send interface clear (IFC) or remote enable (REN). If mode is "0," the GPIB board surrenders system control and all controller-specific commands are not allowed. If mode = "1," then controller-specific commands are allowed.

## Return Values

Status

## Availability

| Since Version |
|---|
