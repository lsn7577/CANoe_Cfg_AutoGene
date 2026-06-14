# testWaitForScopeEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitForScopeEvent(dword aTimeout);
long testWaitForScopeEvent(enum ScopeEventType scopeEvent, dword aTimeout);
```

## Description

Waits for the occurrence of CANoe Scope event. Should the event not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

## Parameters

| Name | Description |
|---|---|
| aTimeout | Timeout in milliseconds |
| Value | Description |
| scopeConnected | Occurs when the Connect Scope action initiated with the scopeConnect() CAPL call is successfully completed. |
| scopeDisconnected | Occurs when the Disconnect Scope action initiated with the scopeDisconnect() CAPL call is successfully completed. |
| scopeTriggerActivated | Occurs when the Scope trigger activation initiated with the scopeActivateTrigger() CAPL call is successfully completed. |
| scopeTriggerDeactivated | Occurs when the Scope trigger deactivation initiated with the scopeDeactivateTrigger() CAPL call is successfully completed. |
| scopeTriggered | Occurs when the Scope triggering action initiated with the scopeTriggerNow() CAPL call is successfully completed. |

## Example

```c
long res;

res = scopeTriggerNow();
if (res != 1)
{
   testStepFail("Initialization","Call to scopeTriggerNow() failed. Return code =%d", res);
   return;
}

// wait till action done
if (testWaitForScopeEvent(eScopeTriggered, 8000) != 1)
{
   testStepFail("Initialization ","Scope event eScopeTriggered was not received");
   return;
}
testStep("Initialization","Scope hardware triggered successefully");
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.6 SP3 | 13.0 | — | — | 1.0 |
| Restricted To | — | Scope | Scope | — | — | Scope |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
