# AvbILControlInit

> Category: `IP` | Type: `function`

## Syntax

```c
dword AvbILControlInit();
```

## Description

Initialization of the AVB IL.

Initializes, but prevents the AVB IL, i.e. the simulated time aware end station (PTP clock instance), from starting automatically. If this function is used, the AVB IL must then be started with the AvbILControlStart function.

This function may only be used in on preStart.

## Return Values

0: The function was successfully executed.

## Availability

| Since Version |
|---|
