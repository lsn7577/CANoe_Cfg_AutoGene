# SerialSetOnSendHandler

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long SysVarNamespace.SerialSetOnSendHandler( char onSendCallback[]);
```

## Description

Sets the callback that notifies when a send operation on the serial port of the specified channel is completed successfully.

The set callback must have following signature: void <OnSerialSend>( byte sendBuffer[], dword number)

## Return Values

0: Successful call

## Availability

| Since Version |
|---|
