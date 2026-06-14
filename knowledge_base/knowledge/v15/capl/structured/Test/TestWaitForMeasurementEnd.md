# TestWaitForMeasurementEnd

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForMeasurementEnd (dword aTimeout);
```

## Description

Waits for the end of the measurement. As the final command within a test module, this function can be used to keep the test module and therefore the monitoring of constraints and conditions active. With measurement end this wait condition can be resolved. The test result and therefore also the report are not negatively impacted by the end of the measurement, if the test module does not contain any further wait commands after this one.

If a timeout time unequal to "0" is entered, the wait point is also resolved when the specified waiting time expires.

Application:

The test module monitors constraints and conditions. This monitoring process should be implemented precisely as long as the measurement runs.

## Parameters

| Name | Description |
|---|---|
| aTimeout [ms] | Maximum time that should be waited. |

## Example

```c
// monitoring of condition is active until measurement end
dword checkId;
long result;
checkId = ChkStart_InconsistentDlc(VehicleMotion);
result = TestWaitForMeasurementEnd(5000);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
