# coTfsSDOGetAbortCode

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOGetAbortCode( dword nodeID, dword outSrcNodeId[1], qword outTimeStamp[1], dword outIndex[1], dword outSubIndex[1], dword outAbortCode[1] ); // form 1
```

## Description

This function returns received SDO abort codes. In addition, the following information is delivered:

Via the parameter nodeID, the returned SDO abort codes can be filtered. The value nodeID=0 returns all SDO abort codes that occur. All SDO abort codes can only be read out once with this function.

(2) It is possible to omit the parameter nodeID. In this case, the internal saved value set with coTfsSetNodeId() is used as node-ID.

## Return Values

If no SDO abort code was received, the function returns the return value 0.
Otherwise, the number of still-outstanding SDO abort codes (current SDO abort code is contained in this number) is returned. For a return value 0, all return arrays are invalid.

## Example

```c
dword pNodeId[1], pIndex[1], pSubIndex[1], pAbortCode[1];
qword pNanoSecondsTime[1];
dword counter;

if ((counter = coTfsSDOGetAbortCode( pNodeId, pNanoSecondsTime, pIndex, pSubIndex, pAbortCode))!=0) {
  write("SDO abort message caught: counter %d, node-ID 0x%x, time %I64d [ns], index 0x%x, subIndex 0x%x, abortcode 0x%x", counter, pNodeId[0], pNanoSecondsTime[0], pIndex[0], pSubIndex[0], pAbortCode[0]);
}
else {
  write("no SDO abort code received");
}
```
