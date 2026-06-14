# FSIL_ControlStart

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long FSIL_ControlStart(); // form 1
```

## Description

Activates node to start Address Claiming.

The File Server starts Address Claiming (if NMT is activated). If the Address Claiming was successful, cyclic messages are sent.

## Return Values

0: Function has been executed successfully

## Availability

| Since Version |
|---|
