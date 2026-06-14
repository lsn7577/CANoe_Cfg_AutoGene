# testWaitForAllParallel

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitForAllParallel(dword timeout);
```

## Description

Waits until execution of all parallel threads finished. In case all threads already finished execution, the function returns instantly.

## Parameters

| Name | Description |
|---|---|
| timeout | Maximum time to wait [ms]. Specify 0 to wait without timeout. |

## Example

```c
export testcase TestParallelExecution()
{
  write("Start parallel execution.");
  testStartParallel(ParallelFunction, 500);
  teststartParallel(ParallelFunctionTwo);

testWaitForAllParallel(2000);

write("End parallel execution");
}

testfunction ParallelFunction(dword aTimeout)
{
  testWaitForTimeout(aTimeout);
  write("Wait in parallel.");
}

testfunction ParallelFunctionTwo()
{
  testWaitForTimeout(400);
  write("Wait in parallel again.");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | —✔ | —✔ | — | —✔ | 4.0 |
| Restricted To | — | —✔ | —✔ | — | —✔ | Test units |
| CANalyzer Measurement Setup (Transmit Branch) | — | —✔ | —✔ | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | —✔ | —✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | —✔ | —✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | —✔ | —✔ | — | N/A | N/A |
| CANoe Test Setup for Test Modules | N/A | —✔ | —✔ | — | —✔ | N/A |
| CANoe Test Setup for Test Units | N/A | —✔ | —✔ | — | —✔ | N/A |
| 32-Bit | — | —✔ | —✔ | N/A | —✔ | N/A |
| 64-Bit | — | —✔ | —✔ | — | —✔ | N/A |
