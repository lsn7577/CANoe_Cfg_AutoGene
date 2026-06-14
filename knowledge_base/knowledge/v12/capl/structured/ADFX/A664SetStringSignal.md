# A664SetStringSignal

> Category: `ADFX` | Type: `function`

## Syntax

```c
long A664SetStringSignal (dbSignal aSignal, char val[]) (1)
```

## Description

This function can be used to set a string-signal within a specific a664Message (form 2) or to set the Tx-signal of the CANoe-subsystem (form 1).

For AFDX the usual string format contains the string length information at the first 2 bytes of the signal position, so the usual string operations won’t work correct on string signal.

Note: To set opaque-type signals use the generic function SetRawSignal.

## Example

```c
a664Message TESTMSG_ALLTYPES testMsg = { msgChannel = 1};
a664SetStringSignal(TEST_STRING14_CITY, "STR126"); // set signal value on signalServer
a664InitPayload (testMsg); 	// set payload to last known signal values
a664TriggerMessage(testMsg, 1);
a664Message TESTMSG_ALLTYPES testMsg = { msgChannel = 1};
testMsg.VFG_OIL_TEMP_AB_32 = 86;
a664SetStringSignal(TEST_STRING14_CITY, "STR126", testMsg);
a664TriggerMessage(testMsg, 1);
```

## Availability

| Since Version |
|---|
