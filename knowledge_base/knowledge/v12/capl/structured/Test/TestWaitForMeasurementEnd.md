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

## Return Values

0: Resume due to timeout

## Example

```c
// monitoring of condition is active until measurement end
dword checkId;
long result;
checkId = ChkStart_InconsistentDlc(VehicleMotion);
result = TestWaitForMeasurementEnd(5000);
```

## Availability

| Since Version |
|---|
