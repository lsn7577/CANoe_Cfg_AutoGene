# AvbILControlStart

> Category: `IP` | Type: `function`

## Syntax

```c
dword AvbILControlStart();
```

## Description

Starts the AVB IL.

Enables sending and receiving of AVB/TSN related messages. After the start of the AVB IL, the time aware end station (PTP clock instance) starts up and Talkers and/or Listeners can be created.

The AVB IL can be stopped using the AvbILControlStop function.

## Return Values

0: The function was successfully executed.

## Availability

| Since Version |
|---|
