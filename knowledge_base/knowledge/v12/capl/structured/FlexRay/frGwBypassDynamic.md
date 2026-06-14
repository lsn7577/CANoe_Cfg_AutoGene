# frGwBypassDynamic

> Category: `FlexRay` | Type: `function`

## Syntax

```c
long frGwBypassDynamic(long bypass, long channel)
```

## Description

Activates/deactivates the automatic routing for the dynamic part. The function can not be used during a measurement.

Settings from the Network Hardware Configuration dialog are overwritten with this function.

## Return Values

0 = Error

## Example

```c
...
frGwBypassDynamic (0,1)
// The gateway routing for the dynamic part will be deactivated 
// for the gateway that uses channel 1.
...
```

## Availability

| Since Version |
|---|
