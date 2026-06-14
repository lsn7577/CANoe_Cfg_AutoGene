# OnMostMHPBlock

> Category: `MOST` | Type: `function`

## Syntax

```c
long OnMostMHPBlock(long sourceDevID, long destDevID, long fBlockID, long instID, long functionID, long opType);
```

## Description

The event procedure is called up as soon as a block from a MOST High connection has been fully transmitted.

Within this event procedure the following functions are available

Copies the reference data of the block in a provided buffer.Parameter: buffer (buffer for the data bytes)bufferSize (size of the buffer)Returns: Number of data bytes copied

Indicates whether the block was made up of Spy messages.Parameter: NoneReturns:0: Comprised of node messages1: Comprised of Spy messages

Provides the number of Data Frames of the block.Parameter:NoneReturns:Number of actual Data Frames

Provides the number of Data Frames of the block that it should has according to the 0-frame.Parameter:NoneReturns:Number of Data Frames

Provides the size of the block.Parameter:NoneReturns:Number of data bytes (reference data only)

Provides the transmission mode of the block.Parameter:NoneReturns:1: Transmission on the control channel2: Transmission on the asynchronous channel

Provides the sequence number of the block.Parameter:NoneReturns:Cnt field of the 0-frame (see MHP specification)

Provides the options for the transmission of the block.Parameter:NoneReturns:Options field of the 0-frame (see MHP specification)

Provides the segmentation ID of the block.Parameter:NoneReturns:Options field of the 0-frame (see MHP specification)

The functions mostEventChannel, mostEventTime and mostEventTimeNS can be used to call up supplemental information.

## Parameters

| Name | Description |
|---|---|
| sourceDevID | Address of the transmitter |
| destDevID | Address of the receiver |
| fBlockID | FBlockID of the receiver |
| instID | Instance ID of the receiver |
| functionID | FunctionID of the receiver |
| opType | OpType of the receiver |

## Return Values

The return value determines whether the MHP block event is relayed to the next function block in the Measurement Setup (e.g. a Trace Window).

## Example

The example shows how the data of a block can be written to a file. The file (fileHandle variable) must be opened in advance. The block event is relayed by the "return 1" instruction to the next function block in the Measurement Setup.

```c
const long blockBufferSize = 64*1024;
long OnMostMHPBlock (long sourceDevID, long destDevID, long fBlockID, long instID,
long functionID, long opType)
{
   //Prepare a data buffer
   byte buffer[blockBufferSize];
   long byteCount;
   //Get data of the MHPBlock
   mostMHPBlockGetData(buffer, blockBufferSize);
   //Write data to the file
   byteCount = (mostMHPBlockSize() < blockBufferSize) ? 
mostMHPBlockSize() :
blockBufferSize;
   fileWriteBinaryBlock(buffer, byteCount, fileHandle);
   //Forward MHPBlock to the next CAPL node
   return 1;
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 6.0 | 6.0 | — | — | — | —✔ |
| Restricted To | MOST25 MOST50 MOST150 | MOST25 MOST50 MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | — | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | — | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | —✔ |
| 32-Bit | — | — | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
