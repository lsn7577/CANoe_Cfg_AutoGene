# AvbILControlStop

> Category: `IP` | Type: `function`

## Syntax

```c
dword AvbILControlStop();
```

## Description

Stops the AVB IL.

Disables sending and receiving of AVB/TSN related messages. Opened Talkers and Listeners are closed, and the associated handles become invalid.

Handles obtained via the Media API stay valid.

The AVB IL can be started again using the AvbILControlStart function.

## Return Values

0: The function was successfully executed.

## Availability

| Since Version |
|---|
