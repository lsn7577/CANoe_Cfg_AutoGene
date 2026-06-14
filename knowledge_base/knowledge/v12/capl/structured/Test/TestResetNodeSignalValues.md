# TestResetNodeSignalValues

> Category: `Test` | Type: `function`

## Syntax

```c
long TestResetNodeSignalValues (dbNode aNode);
```

## Description

Resets all tx-signals of the given node to their initial value. The sending of the messages depends on the messages send typ.

The reset-function does not contain a waiting time which guarantees that all signals are sent out on the bus. If a waiting time is desired, the TestWaitForTimeout function has additionally been executed.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

0: No error

## Example

```c
// check reaction of signal “LockState” after crash
$CrashDetected = 1;
TestWaitForTimeout(100);
if ($LockState !=  Unlocked)
    TestStepFail(“Doors are locked after crash is detected!”);

// reset test signals of node “SUT”
TestResetNodeSignalValues(SUT);
TestWaitForTimeout(200);
```

## Availability

| Since Version |
|---|
