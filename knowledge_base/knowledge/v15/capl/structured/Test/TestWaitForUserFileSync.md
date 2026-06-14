# TestWaitForUserFileSync

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForUserFileSync(char aFileName[], long isDirectionClientToServer);
```

## Description

This function can be used to start synchronization of user files between client and server system in a distributed environment. Once the synchronization has been started successfully the system waits until the file is synchronized.

The function is not allowed in CANoe standalone mode. Errors are reported as error in test system or fail in case of 2-valued verdict concept.

## Parameters

| Name | Description |
|---|---|
| aFileName | The name of the user file to be synchronized (path component is ignored). |
| isDirectionClientToServer | If this parameter is set to true (≠0) the file is synchronized from the client (e.g. CANoe) to the server system. |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
