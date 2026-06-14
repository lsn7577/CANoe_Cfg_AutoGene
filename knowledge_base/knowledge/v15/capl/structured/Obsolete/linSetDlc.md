# linSetDlc

> Category: `Obsolete` | Type: `notes`

| Deprecated Function No replacement. |  |  |  |  |
|---|---|---|---|---|
| Note This function is only available with the LIN specification 1.2. This function does not have any effect in the event procedure on preStart. |  |  |  |  |
| Function Syntax | long linSetDlc(long frameID, long dlc) |  |  |  |
| Function | Initializes the Data Length Code (i.e. length in bytes) of a LIN frame. This function must be called in the event procedure on preStart. The DLC of each frame ID can only be initialized once using this function. To change the DLC of a LIN frame during the measurement, use the function linChangeDlc(). Per default the DLC of LIN frames is initialized according to the LIN Description File (LDF). This function is therefore only needed if you are simulating LIN nodes without using an LDF. |  |  |  |
| Context | Master or Slave node (in on preStart only) |  |  |  |
| Parameters | frameID LIN frame identifier in the range 0 ... 63. |  |  |  |
| DLC Frame length in bytes in the range 1 ... 8 |  |  |  |  |
| Return Values | If successful a value unequal to zero. Zero will be returned if for example the DLC has already been set for the selected ID. |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 3.1 - 5.1 | LIN | — | • |  |
| Example Set DLC of a LIN frame not defined in the database. on preStart{...linSetDLC(0x22, 5); // set DLC of frame with identifier 0x22 to be 5...} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
