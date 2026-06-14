# xcpDisconnect

> Category: `XCP` | Type: `function`

## Syntax

```c
long xcpDisconnect(char ecuQualifier[]);
```

## Description

Disconnects from a XCP/CCP device.

Use xcpIsConnected to be aware of the disconnection.

The callback function OnXcpDisconnect is called after the ECU acknowledged the disconnect command.

## Return Values

0: OK

## Availability

| Since Version |
|---|
