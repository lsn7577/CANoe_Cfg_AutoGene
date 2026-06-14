# mostApplicationNode

> Category: `MOST` | Type: `function`

## Syntax

```c
void mostApplicationNode()
```

## Description

This CAPL function can only be called in on preStart and switches the CAPL node into application mode. The node will

This mode is especially useful for nodes connected to a single MOST channel in the Simulation Setup.Checks like "if (this.MsgChannel!=XY) return;" or "if (this.IsSpy()) return;" or event handler "on mostMessage MsgChannel1.*" explicit for a channel can be omitted. In many cases the assignment of a channel before sending a message can be omitted.With declaration of a message variable the channel will be initialized with a wildcard (0xFFFF), which will be mapped to the channel with which the node is connected in the Simulation Setup on transmission.This makes the CAPL code easily reusable because it is independent of any hard coded channel numbers.The application mode is independent of the activation of the application socket, however it especially utilizes the implementation of function block behavior.

## Return Values

—

## Availability

| Since Version |
|---|
