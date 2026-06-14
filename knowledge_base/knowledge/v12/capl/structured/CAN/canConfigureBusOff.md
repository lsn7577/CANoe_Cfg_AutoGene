# canConfigureBusOff

> Category: `CAN` | Type: `function`

## Syntax

```c
long canConfigureBusOff(long channel, long canId, long flags);
```

## Description

Uses the defined ID of a message to set the bus state to BusOff.

This function requires minimum a Vector driver 9.6 and a network interface with ISO CAN FD support.

## Return Values

1 = The disturbance for the defined ID was switched on successfully.0 = The disturbance for the defined ID could not switched on.

## Availability

| Since Version |
|---|
