# DeferStop

> Category: `Other` | Type: `function`

## Syntax

```c
void DeferStop(dword maxDeferTime)
```

## Description

Defers measurement stop.

The function can be called in the on preStop handler or even at an earlier time instance. Measurement is deferred until CompleteStop is called in the same node or the simulation time has advanced by the amount given in parameter maxDeferTime since the arrival of a stop request (and call of the on preStop handler).

DeferStop enables waiting for completion of activities that have to be carried out before measurement stop takes effect, e.g. a reset of an attached ECU.

## Return Values

—

## Example

```c
on preStop
{
   message ShutdownReq m;
   output(m);
   DeferStop(1000);
}
on message ShutdownAck
{
   CompleteStop();
}
```

## Availability

| Since Version |
|---|
