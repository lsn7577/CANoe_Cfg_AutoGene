# ScanBaudrateActive

> Category: `CAN` | Type: `function`

## Syntax

```c
long ScanBaudrateActive( dword channel, dword messageID, double firstBaudrate, double lastBaudrate, dword timeout);
```

## Description

The function determines the baud rate for the given channel. Result of the function is written into the Write Window.

The baud rate scanner checks different baud rates and tries to send a message through the given channel. The function is finished if the message was sent successfully and the baud rate was determined. If a wrong baud rate is present, the other power supply takers cannot receive the message. CANoe as the transmitter does not receive an acknowledge and sends an Error Frame. In this case the next baud rate of the baud rate range is checked.

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
