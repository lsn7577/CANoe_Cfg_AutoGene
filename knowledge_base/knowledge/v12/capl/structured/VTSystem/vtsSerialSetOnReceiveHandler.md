# vtsSerialSetOnReceiveHandler

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long vtsSerialSetOnReceiveHandler (char Target[], char onReceiveCallback []);
```

## Description

Sets the callback that notifies when data has been received on the serial port of the specified channel.

The set callback has to have following signature: void <OnSerialReceive>( byte bffer[], dword number)

## Return Values

0: Successful call

## Availability

| Since Version |
|---|
