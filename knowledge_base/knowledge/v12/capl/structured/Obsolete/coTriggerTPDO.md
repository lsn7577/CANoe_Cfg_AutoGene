# coTriggerTPDO

> Category: `Obsolete` | Type: `function`

## Syntax

```c
dword coTriggerTPDO( dword pdoNumber, dword errCode[] );
```

## Description

Generally a simulated node is used with a defined cycle time. The default value is 5 ms, but it can be changed with the function coSetOperatingMode() for each node. The cycle time also defines the reaction time on data changes of the PDOs. Consider that a decrease of the node processing time leads to a higher load of the simulated system.

If it is necessary to transmit the PDO directly after the data change, this function can be used. It triggers the immediate transmission of a TPDO.

The following conditions have to be fulfilled to allow the transmission of a TPDO with this function:

If one of this conditions is not fulfilled, the transmission of the relating TPDO will not be triggered and the function returns with an error.

## Return Values

—

## Example

```c
dword errCode[1];

putValue(MyProcessData, 0x1234);
coTriggerTPDO( 1, errCode );

if (errCode[0] == 0) {
  write( "TPDO 1 triggered successfully" );
}
```

## Availability

| Up to Version |
|---|
