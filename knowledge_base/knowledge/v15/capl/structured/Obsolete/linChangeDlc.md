# linChangeDlc

> Category: `Obsolete` | Type: `notes`

## Description

linGetDlc

| Deprecated Function Replaced by linSetExpectedRespLength and linSetRespLength. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long linChangeDlc(long frameID, long dlc) |  |  |  |
| Function | Changes the Data Length Code (i.e. length in bytes) of a LIN frame during the measurement. Per default the DLC of LIN frames is initialized according to the LIN Description File (LDF). This function is therefore only needed if you are simulating LIN nodes without using a LDF and need to change the DLC of a LIN frame during the measurement. To initialize the DLC of a LIN frame the function linSetDlc should be used in the event procedure on preStart. |  |  |  |
| Context | Master or Slave node |  |  |  |
| Parameters | frameID LIN frame identifier in the range 0 .. 63 |  |  |  |
| dlc Frame length in bytes in the range 1 .. 8 |  |  |  |  |
| Return Values | If successful a value unequal to zero. |  |  |  |
| Availability | Since Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 5.1 | LIN | — | • |  |
| Example Change DLC of a frame from database ...linFrame MotorControl frameMotorControl;linChangeDLC(frameMotorControl.id, frameMotorControl.dlc-1);// now on transmitting the above frame a checksum error will come |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
