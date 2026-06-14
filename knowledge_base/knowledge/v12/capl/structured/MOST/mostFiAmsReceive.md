# mostFiAmsReceive

> Category: `MOST` | Type: `function`

## Syntax

```c
mostFiAmsReceive(mostAmsMessage * msg)
```

## Description

Simulates the receipt of an AMS message to the simulation node (CAPL program or node layer module).

mostFiAmsReceive can only be used within the callback OnMostFiAmsPreReceive or OnMostFiAmsPreSend. If mostFiAmsReceive is called more than once within the callback, only the last fed-in message is passed on to the simulation node.

Altered received messages are neither displayed in the Trace Window nor logged. They are only visible for the one node in the Simulation Setup from which mostFiAmsReceive was called.

Exception: a CAPL program with fault injection for the MOST application socket (see mostAsFiEnable) can call mostFiAmsReceive as many times as necessary and at any time in order to simulate a received message to the CANoe-side application socket. These altered messages are then visible only for the services of the MOST application socket in CANoe.

## Return Values

—

## Availability

| Since Version |
|---|
