# linResetNAD

> Category: `LIN` | Type: `function`

## Syntax

```c
long linResetNAD()
```

## Description

This function resets NAD (Node Address for Diagnostic) of the Slave node determined by the CAPL program context to its initial NAD.

See Option .LIN: Notes to the way initial NAD is determined to understand how initial NAD is determined in CANoe.

If the CAPL program calling this function, does not model a LIN 2.x Slave node, then this function will have no effect.

## Return Values

On success this function returns a value unequal to -1, otherwise -1.

## Example

CAPL program modeling Slave node

```c
// Force NAD reset on a keyboard event
on key 'r'
{
linFrame 0x3C frameMasterReq;
linFrame 0x3D frameSlaveResp;
// reset NAD of the modeled Slave node 
// we assume that by default initial NAD differs from configured NAD
linResetNAD();
}
CAPL program modeling Master node
...
// Test Slave node reaction after its NAD has been 
 reset.
// Prepare AssignFrameId command for one of the Slave's configurable frames
// In this example it is assumed that the configured NAD differs from the initial 
// NAD
// set command's data
frameMasterReq.byte(0) = 0x02; // configured NAD
frameMasterReq.byte(1) = 0x06; // PCI
frameMasterReq.byte(2) = 0xB1; // SID
frameMasterReq.byte(3) = 0x1E; // Supplier Id LSB
frameMasterReq.byte(4) = 0x0;  // Supplier Id MSB
frameMasterReq.byte(5) = 0x22; // Message Id LSB
frameMasterReq.byte(6) = 0x22; // Message Id MSB
frameMasterReq.byte(7) = linGetProtectedID(0x33); // Protected ID
// update response data
frameMasterReq.RTR = 0;
output(frameMasterReq);
// send the command (issue request header)
frameMasterReq.RTR = 1;
output(frameMasterReq);
// send header of SlaveResponse frame
frameSlaveResp.RTR = 1;
output(frameSlaveResp);
// In Trace Window transmission error shall occur for SlaveResponse frame because
// Slave doesn’t know the configured NAD yet
```

## Availability

| Since Version |
|---|
