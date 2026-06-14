# output (CAN)

> Category: `CAN` | Type: `function`

## Syntax

```c
void output(message msg); // form 1
```

## Description

Outputs a message (form 1) or an Error Frame (form 2) from the program block.

## Return Values

—

## Example

Except for the first channel for all other channels the key word errorFrame has to be qualified with the number of the CAN channel.

```c
variables {
message can2.125 msg = { // define CAN message 
dlc = 1,
byte(0) = 1
};
}
on key F1 {
output (msg); // output Message
}
on key F10 {
output(errorFrame); // output Error Frame on CAN channel 1
}
on CAN2.errorFrame {
output (CAN3.errorFrame); // output Error Frame on CAN channel 3
}
```

## Availability

| Since Version |
|---|
