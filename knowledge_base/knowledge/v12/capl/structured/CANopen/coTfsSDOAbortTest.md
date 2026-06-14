# coTfsSDOAbortTest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOAbortTest( dword noOfMsgs );
```

## Description

The function aborts the following test after the transmission of messages specified in noOfMsgs. If the test function sends less messages, the test is not aborted.

## Return Values

Error code

## Example

```c
coTfsSDOAbortTest (3); // stop transmission after third message
```
