# testWaitForParallel

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitForParallel(long handle, dword timeout); // form 1
long testWaitForParallel(long handles[], dword timeout) // form 2
```

## Description

Waits until execution of the thread specified via the handle parameter has finished. In case the thread already finished execution, the function returns instantly.

## Parameters

| Name | Description |
|---|---|
| handle | Handle of the thread to wait for. |
| handles[] | Handles of the threads to wait for. |
| timeout | Maximum time to wait [ms]. Specify 0 to wait without timeout. |

## Example

Example // form 1

```c
export testcase TestParallelExecution()
{
  dword handle1;
  write("Start parallel execution.");
  handle1 = testStartParallel(ParallelFunction, 500);
  testStartParallel(ParallelFunctionTwo);

testWaitForParallel(handle1, 2000);

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
