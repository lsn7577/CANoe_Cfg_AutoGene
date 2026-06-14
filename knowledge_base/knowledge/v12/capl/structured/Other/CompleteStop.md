# CompleteStop

> Category: `Other` | Type: `function`

## Syntax

```c
void CompleteStop ()
```

## Description

Indicates completion of pre-stop actions carried out in a certain node after a measurement stop has been deferred by DeferStop.

## Return Values

—

## Example

```c
on preStop
{
   message ShutdownReq m;

   output(m);
   DeferStop(1000);  // measurement is stopped if ACK has not
// yet been received after one second
}
on message ShutdownAck
{
   CompleteStop();
}
```

## Availability

| Since Version |
|---|
