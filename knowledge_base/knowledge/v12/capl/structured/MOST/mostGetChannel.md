# mostGetChannel

> Category: `MOST` | Type: `function`

## Syntax

```c
mostGetChannel ()
```

## Description

This query returns the number of the MOST channel to which the CAPL node is connected in the Simulation Setup.

This query is especially useful with nodes that are only connected to one MOST channel in the Simulation Setup. The return value can be used directly as a parameter for all CAPL functions that expect specification of a channel, e.g. in driving the hardware interface.

With the help of this function CAPL programs can be created such that they are independent of channel numbers. By proper configuration of the Simulation Setup the user can choose the MOST interface over which the node should be operated.

## Return Values

0: the node is not connected to any MOST channel in the Simulation Setup

## Availability

| Since Version |
|---|
