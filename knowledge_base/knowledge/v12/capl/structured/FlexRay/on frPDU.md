# on frPDU

> Category: `FlexRay` | Type: `event`

## Syntax

```c
on frPDU <PDU name>
```

## Description

This procedure is called when a PDU with the corresponding name is received.

on frPDU <ID> is not allowed!

An optional channel parameter for event filtering can be assigned to all handlers:

In this example, the event procedure is only called for PDUs whose application channel is 2 and its name is <PDU name>.

on frPDU MsgChannel2.<PDU name>

An optional qualifier can be used to assign the handler to a specific network:

In this example, the event procedure is only called for specific PDUs from the application channel that is named "network" in the Simulation Setup (only available for CANoe).

on frPDU network.<PDU name>

## Example

The following program reacts on PDUs and prints them in the Write Window.

```c
on frPDU PDU_XY // PDU_XY name from FIBEX database
{
   float var;
   write( "%10.6f: PDU PDU_XY received with update bit = %d!", TimeNowNS()/1000000000.0, this.updateBit);
   var = this.signalname;
   output(this); // only required in Measurement Setup
}
```

## Availability

| Since Version |
|---|
