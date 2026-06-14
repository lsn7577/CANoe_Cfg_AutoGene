# coTfsTPDOGetDataBySyncCyclic

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsTPDOGetDataBySyncCyclic( dword index, dword outLength[], byte outValueBuf[], dword valueBufSize );
```

## Description

This function tries to extract TPDO data using synchronous cyclic method of the test node.

Test sequence

Test result

The test was successful if all parts of the tests are executed successfully. If that's the case, the TPDO data are written in outLength[] and outValueBuf[]. Otherwise the data are set invalid.

Syntax special

The parameters outLength[] and outValueBuf[] can be omitted both.

## Return Values

Error code

## Example

```c
dword outLength[1];
byte outValueBuf[8];

if (coTfsTPDOGetDataBySyncCyclic( 0x1800, outLength, outValueBuf, 8 )!= 1) {
  write("could not retrieve data ");
}
```
