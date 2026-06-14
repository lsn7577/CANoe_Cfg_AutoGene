# ScanBaudratePassive

> Category: `CAN` | Type: `function`

## Syntax

```c
long ScanBaudratePassive( dword channel, dword messageID, double firstBaudrate, double lastBaudrate, dword timeout, dword bAcknowledge);
```

## Description

Baud rate scanner checks different baud rates and tries to receive a message on the channel. Function starts the scan and detects the baud rate on the given channel. Result of the function is written into the Write Window.

If a wrong baud rate is present, CANoe cannot receive messages and sends an Error Frame, which can be put on the bus using the parameter bAcknowledge.

DLC of the message sent by the scanner.

Default value: 8

If this value is set to 0 the baud rate scanner stops after finding the first baud rate.

If the value is non-zero the scanner checks all baud rates and displays a list of values at the end.

Default value: 0

## Return Values

Returns 0 if the scan function was successfully started. Otherwise the return value is non-zero.

## Example

DLC of the message sent by the scanner.

Default value: 8

If this value is set to 0 the baud rate scanner stops after finding the first baud rate.

If the value is non-zero the scanner checks all baud rates and displays a list of values at the end.

Default value: 0

```c
[BaudrateScanner]
Dlc=8
DisplayBaudrateList=0
```

## Availability

| Since Version |
|---|
