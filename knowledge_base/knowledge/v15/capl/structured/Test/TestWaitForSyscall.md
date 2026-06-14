# TestWaitForSyscall

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForSyscall(char aCommandline[], long aExitcode, dword aTimeout)
long TestWaitForSyscall(char aWorkingdir[], char aCommandline[], long aExitcode, dword aTimeout)
```

## Description

This function can be used to start an external application and check its exit code. Once the application has been started successfully the system waits for it to exit at the end of the specified wait time. The result depends on whether the application's exit code matches the specified expected value.

You should either use the absolute path to the external application or use the call with the declaration of the working directory. To keep the configuration independent of installation paths on a concrete computer you can use <workingdir> alternatively to reference an environment variable of the target system, e.g. %MYAPP_DIR%.

## Parameters

| Name | Description |
|---|---|
| aWorkingdir | The working directory for the external application. The directory name may include spaces. |
| aCommandline | The command line for the application including any parameters which might be required. Path names or parameters containing blank spaces must be enclosed in quotation marks (as an escape sequence \"). |
| aExitcode | The expected exit code for the application. If the application is exited within the wait time, the result of the call will also depend on whether it was exited with this exit code. |
| aTimeout [ms] | The maximum wait time at the end of which the application is expected to exit. |

## Example

```c
//starts an external application
long ret;
TestStepBegin("tc1", "syscall");
ret = TestWaitForSyscall("C:\\My Project", "\"My Tester.EXE\" 0", 0, 1000);
if (ret != 1) {
   TestStepFail("Syscall failed or timed out.");
   TestCaseFail();
} else {
   TestStepPass("Syscall succeeded.");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.0: form 1 7.0 SP4: form 2 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
