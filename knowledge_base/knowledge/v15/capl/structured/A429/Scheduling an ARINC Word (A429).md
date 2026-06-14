# Scheduling an ARINC Word (A429)

> Category: `A429` | Type: `notes`

## Description

An ARINC word may be transmitted either on request or cyclically (supported by the hardware scheduler). The transmission behavior is controlled via the selectors TxCtrl and TxCycle. The transmission of an ARINC word is initiated with the function output or a429Transmit. If a real hardware is used the ARINC word is transferred to the hardware with this call.

If an ARINC word is initialized based on a message in a database, the cycle time is taken from the database attribute A429Cycle. For every ARINC word you may also modify the minimum distance to the previous sent ARINC word via the selector gap.

If you want to schedule ARINC words with just the minimum allowed gap phase in between, you have to use the function a429Transmit.

See Also

| Example: Schedule the Cyclic Transmission of an ARINC Word variables { a429Word LBL_103 myWord = {msgChannel = 1};} on start { myWord.SSM_103 = 3; output (myWord); // start scheduling} on key '+' { myWord.SelAirspeed.phys += 22.5; output(myWord); // update} on key '-' { myWord.SelAirspeed.phys -= 22.5; output(myWord); // update} |
|---|

| Example: Transmit ARINC Words on Request variables { a429Word LBL_103 myWord = {msgChannel = 2}; msTimer myTimer; // major schedule} on start { a429SetScheduleTx (myWord, 0); // erase cycle time myWord.SSM_103 = 3; setTimer (myTimer, 10); // fire up timer} on timer myTimer { int i; setTimer (myTimer, 10); // rearm timer // send 3 ARINC words with 40, 80 and 120 us gap for (i = 0; i < 3; i++) { a429SetGap (myWord, ((i * 40000) + 40000)); myWord.SelAirspeed.phys += 22.5; output(myWord); // update }} |
|---|

| Version 15© Vector Informatik GmbH |
|---|
