# mostAsFiEnable

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostAsFiEnable(long mode)
```

## Description

This function allows to temporarily switch the Application Socket Fault Injection on and off.

To allow Fault Injection in general, the main switch in the Network Hardware Configuration dialog has to be activated for the corresponding channel.

The Application Socket Fault Injection allows modifications of the behavior of CANoe’s Appliction Socket services.

All AMS Tx messages from any Application Socket service will be passed through OnMostFiAmsPreSend before sending. All AMS Rx messages to any Application Socket service will be passed through OnMostFiAmsPreReceive before receiving. Incoming and outgoing messages can be blocked or modified within these callbacks in order to simulate an imperfect device.

## Return Values

See error codes

## Availability

| Since Version |
|---|
