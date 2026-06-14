# AREthRegisterCallback

> Category: `IP` | Type: `function`

## Syntax

```c
LONG AREthRegisterCallback( dword objHandle, char callbackName[] );
```

## Description

Enables to register/unregister a CAPL callback function for an object which has been created separately.

## Parameters

| Name | Description |
|---|---|
| objHandle | Handle of an already existing AUTOSAR Eth IL object for which a new CAPL callback function should be registered/unregistered . The following objects and their corresponding callbacks are supported: Provided events (<OnAREthPrepareEvent>) Provided methods (<OnAREthMethodRequest>) Consumed events (<OnAREthEventReceived>) Consumed fields (<OnAREthFieldNotification>) Consumed methods (<OnAREthMethodResponse>) |
| callbackName | The name of the new callback function to register.If a callback function was already registered, it is first unregistered and then replaced by the new one. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP2 | — | — | — | 2.1 SP3 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
