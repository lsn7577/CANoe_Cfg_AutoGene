# TestCaseReportMeasuredValue

> Category: `Test` | Type: `function`

## Syntax

```c
void TestCaseReportMeasuredValue(char semanticName[], float value);
void TestCaseReportMeasuredValue(char semanticName[], float value, char unit[]);
void TestCaseReportMeasuredValue(char semanticName[], long value);
void TestCaseReportMeasuredValue(char semanticName[], long value, char unit[]);
void TestCaseReportMeasuredValue(char semanticName[], char text[]);
void TestCaseReportMeasuredValue(char semanticName[], char text, char unit[]);
void TestCaseReportMeasuredValue(char semanticName[], signal sig);
void TestCaseReportMeasuredValue(char semanticName[], signal sig, char unit[]);
void TestCaseReportMeasuredValue(char semanticName[], sysvar aSysVar);
void TestCaseReportMeasuredValue(char semanticName[], sysvar aSysVar, char unit[]);
void TestCaseReportMeasuredValue(char semanticName[], dbEnvVar aEnvVar);
void TestCaseReportMeasuredValue(char semanticName[], dbEnvVar aEnvVar, char unit[]);
```

## Description

Adds a report entry in the measured values table for the given parameter at the test case level. Accepted parameters are: user defined values, signals, system variables and environment variables.

## Parameters

| Name | Description |
|---|---|
| semanticName | Semantic name for one reported value. |
| value | Numerical value to be displayed in the measured values table. |
| text | String value to be displayed in the measured values table. |
| sig | Value of a signal to be reported in the measured values table. |
| aSysVar | Value of a system variable to be reported in the measured values table. Currently supported types for system variables are: integer, float and string. |
| aEnvVar | Value of an environment variable to be reported in the measured values table. Currently supported types for environment variables are: integer, float and string. |
| unit | Optional. User defined unit text to be displayed in the measured value. If omitted the default unit will be displayed. |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 SP3 | 13.0 | — | 14 | 1.1 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
