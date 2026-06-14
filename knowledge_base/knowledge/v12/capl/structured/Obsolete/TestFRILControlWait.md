# TestFRILControlWait

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long TestFRILControlWait(char aNodeName[])
```

## Description

Stops the Interaction Layer of the selected simulation node.

This function influences a simulation node with an assigned CANoe Interaction Layer.

## Return Values

0: No error.

## Example

```c
// stops the interaction layer of ECU A for 2000 ms
TestFRILControlWait (“ECU_A”);
TestWaitForTimeout(2000);
TestFRILControlResume ((“ECU_A”);
```

## Availability

| Up to Version |
|---|
