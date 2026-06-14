# TestCaseReportMeasuredValue

> Category: `Test` | Type: `function`

## Syntax

```c
void TestCaseReportMeasuredValue(char semanticName[], float value);
```

## Description

Adds a report entry in the measured values table for the given parameter at the test case level. Accepted parameters are: user defined values, signals, system variables and environment variables.

If the function is called several times inside a test case using the same semantic name, only the last value will be reported in the measured values table.

## Return Values

—

## Example

```c
testcase TestMeasuredValues()
{
  double acc;
  TestCaseTitle("", "Report Measured Values");

  TestCaseReportMeasuredValue("Version", "1.0");
  TestCaseReportMeasuredValue("Start time", 210, "ms");

  TestCaseReportMeasuredValue("Crash", VehicleMotion::CrashDetected);
  TestCaseReportMeasuredValue("Acceleration", sysvar::SystemUnderTest::Accelerate);

  TestStep("", "Value Conversion");
  acc = @sysvar::SystemUnderTest::Accelerate * 1000.0 / 3600.0;
  TestCaseReportMeasuredValue("Acceleration", acc, "mp/s2");

  TestWaitForTimeout(2000);
}
```

## Availability

| Since Version |
|---|
