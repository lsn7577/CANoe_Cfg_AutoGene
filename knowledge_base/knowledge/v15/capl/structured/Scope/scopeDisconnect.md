# scopeDisconnect

> Category: `Scope` | Type: `function`

## Syntax

```c
long scopeDisconnect ();
```

## Description

Performs Disconnect Scope action for Scope Window. This action is equivalent to disconnecting Scope via the GUI.

The completion of this action is reported with an internal event which can be awaited via TFS-function testWaitForScopeEvent() in CAPL programs for test modules.

## Example

```c
long res;

res = scopeDisconnect();
if (res <= 0 || res > 2)
{
   testStepFail("Initialization","Call to scopeDisconnect() failed. Return code =%d", res);
   return;
}
else if (res == 1)
{ // wait till action done
   if (testWaitForScopeEvent(eScopeDisconnected, 8000) != 1)
   {
      testStepFail("Initialization ","Scope event eScopeDisconnected was not received");
      return;
   }
}
testStep("Initialization","USB connection with the scope hardware is interrupted");
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.6 SP3 | 7.6 SP3 | — | — | — | 1.1 SP2 |
| Restricted To | Scope | Scope Real bus mode | — | — | — | Scope Real bus mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
