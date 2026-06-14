# Class: CanDisturbanceSequence

> Category: `CANDisturbance` | Type: `notes`

## Description

An object of this class represents a user defined sequence. A sequence can contain up to 4096 segments. A segment can be added by using the function AppendToSequence. To clear the current configured sequence the Clear method can be used. The ToString method can be used to write the current configured sequence to a text buffer or a test report.

You can access control information of a CanDisturbanceSequence object with the following attributes:

| Keyword | Description | Type | Access Limitations |
|---|---|---|---|
| SegmentCount | The count of the segments currently added to the sequence. | dword | read-only |

| Example CanDisturbanceSequence sequence; //Object of sequencedword deviceID; //Device Id of disturbance interfacechar buffer[1024]; //text buffer for ToString methoddeviceID = 1;//clear the sequence if(sequence.SegmentCount > 0){sequence.Clear();}//configure a sequence 320 FPGA ticks long and send a recessive bit at the Ack slot bit on the bus. A FPGA tick is 6.25 ns long, which leads to a bit time of 2 µsresult = sequence.AppendToSequence(320, 'd');//Configure the frame trigger and the sequence to the CAN Disturbance Deviceif(result == 1){ //Send the sequence immediately on the bus result = canDisturbanceTriggerNow(deviceID, sequence); if(result == 1) { result = sequence.ToString(buffer, 1024); write("Sequence %s was send with length %d", buffer, result); //Output: //Sequence ddddddd…ddddd was send with length 320 } else { write("Error by sequence sending Result =%d", result); }} |
|---|

| Version 15© Vector Informatik GmbH |
|---|
