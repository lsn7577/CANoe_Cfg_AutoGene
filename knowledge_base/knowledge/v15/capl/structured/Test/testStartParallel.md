# testStartParallel

> Category: `Test` | Type: `function`

## Syntax

```c
long testStartParallel(caplFunction, ...);
```

## Description

Spawns a new thread to execute the specified function. Execution will start as soon as possible.

## Parameters

| Name | Description |
|---|---|
| caplFunction | CAPL function to execute in parallel. The function's parameters must be specified as parameters of the testStartParallel call in the correct order. The return value type of the function must be void. |

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
