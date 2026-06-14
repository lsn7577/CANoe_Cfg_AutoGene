# EthControlInit

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long EthControlInit();
```

## Description

This function initializes the Ethernet Interaction Layer.

The function call is only possible in on preStart. Then the Ethernet Interaction Layer has to be started with EthControlStart. If it is not called, the Ethernet Interaction Layer automatically starts with the properties defined in the node attributes.

## Availability

| Up to Version |
|---|
