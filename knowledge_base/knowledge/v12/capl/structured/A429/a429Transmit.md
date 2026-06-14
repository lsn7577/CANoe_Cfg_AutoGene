# a429Transmit

> Category: `A429` | Type: `function`

## Syntax

```c
long a429Transmit (a429word myA429Word[], dword myNum);
```

## Description

This function triggers the transfer of myNum A429words to the network hardware interface at once. When the mode Simulated bus is used, a built-in simulation layer takes care of the ARINC word.

The following restrictions apply:

The ARINC word selectors TxCtrl and TxCycle are ignored.

Note that the ARINC word selector Gap (see a429SetGap) may be used to adjust the distance between the ARINC words. A single ARINC word is transmitted or updated with output.

Attention: Be aware that the hardware queue size is limited; therefore calling this method rapidly may cause a queue overflow.

## Example

Transmit ARINC words on request:

```c
variables
{
  a429Word * myWord[3];
}

on start {
  int i;
  for (i = 0; i < elCount(myWord); i++) {
    myWord[i].msgChannel = 2;
    myWord[i].Id = 64 + i; // create different label numbers
    // send 3 ARINC words with 38.75 and 37.5 us gap
    a429SetGap (myWord[i],
      a429CalcBitLength(myWord[i].msgChannel, 32 - i));
  }
}

on key 's' {
  int i;
  for (i = 0; i < elCount(myWord); i++) {
    myWord[i].byte(1) += 1;
  }
  a429Transmit(myWord, elCount(myWord)); // update
}
```

## Availability

| Since Version |
|---|
