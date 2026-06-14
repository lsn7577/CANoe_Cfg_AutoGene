# A429 CAPL Functions

> Category: `A429` | Type: `notes`

## Description

Declaration of ARINC Words | ARINC Word Selectors | Scheduling an ARINC Word | Reconfigure a Channel

| A429 Only available with option .A429. |
|---|

| Functions | Short Description |
|---|---|
| a429CalcBitLength | Returns the bit length for a given channel. |
| a429CheckParity | Checks the parity of an ARINC word. |
| a429GetBitLength | Returns the length of an erroneous measured bit in an Rx error. |
| a429GetConfiguration | Returns the current channel configuration settings. |
| a429GetErrorPosition | Gets the error position of a Rx error. |
| a429InitPayload | Initialize the payload of an existing a429word. |
| a429ResetEx | Re-initialize a selected channel with current channel parameters. |
| a429SetConfiguration | Sets the current channel configuration settings. |
| a429SetGap | Sets the selector gap of an ARINC word. |
| a429SetParity | Sets the selector parity of an ARINC word. |
| a429SetScheduleTx | Prepares an ARINC word to be transmitted cyclically by means of the hardware scheduling support. |
| a429StopTx | Stops the cyclic transmission of an ARINC word. |
| a429Transmit | Triggers the transfer of several ARINC words to the network hardware interface at once. |
| output | Transmits an ARINC word to the network hardware interface. |
| Event Procedures | Short Description |
| on a429error | Receives an ARINC error event. |
| on a429word | Receives an ARINC word event. |
| on a429worderror | Receives an ARINC word error event. |

| Version 15© Vector Informatik GmbH |
|---|
