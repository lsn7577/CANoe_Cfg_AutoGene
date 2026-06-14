# canDisturbanceFrameTrigger::SetMessage

> Category: `CANDisturbance` | Type: `function`

## Syntax

```c
long canDisturbanceFrameTrigger::SetMessage(message msg, dword deviceID, dword validityMask);
```

## Description

Sets the frame for the trigger condition. The mask is filled automatically with the data of the frame. The used data can be configured with the validity mask.

## Availability

| Since Version |
|---|
