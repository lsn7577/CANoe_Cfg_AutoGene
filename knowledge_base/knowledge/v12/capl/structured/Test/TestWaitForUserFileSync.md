# TestWaitForUserFileSync

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForUserFileSync(char aFileName[], long isDirectionClientToServer);
```

## Description

This function can be used to start synchronization of user files between client and server system in a distributed environment. Once the synchronization has been started successfully the system waits until the file is synchronized.

The function is not allowed in CANoe standalone mode. Errors are reported as error in test system or fail in case of 2-valued verdict concept.

## Return Values

1: The user file was successfully synchronized.

## Example

```c
long ret;
TestStepBegin("tc1", "sync");
ret = TestWaitForUserFileSync("UserFileCAPL.TXT", 1);
if (ret != 1) {
   TestStepFail("Transmit of \"UserFileCAPL.TXT\" from client to server failed.");
   TestCaseFail();
} else {
   TestStepPass("Synchronization succeeded.");
}
```

## Availability

| Since Version |
|---|
