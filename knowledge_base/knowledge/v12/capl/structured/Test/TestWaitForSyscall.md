# TestWaitForSyscall

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForSyscall(char aCommandline[], long aExitcode, dword aTimeout)
```

## Description

This function can be used to start an external application and check its exit code. Once the application has been started successfully the system waits for it to exit at the end of the specified wait time. The result depends on whether the application's exit code matches the specified expected value.

You should either use the absolute path to the external application or use the call with the declaration of the working directory. To keep the configuration independent of installation paths on a concrete PC you can use <workingdir> alternatively to reference an environment variable of the target system, e.g. %MYAPP_DIR%.

## Return Values

1: The application exited with the expected exit code.

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

| Since Version |
|---|
