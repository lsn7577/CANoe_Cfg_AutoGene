# TCIL_MakeDdopAvailable

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_MakeDdopAvailable(char[] ddopPath[]); // form 1
```

## Description

Loads a device descriptor object pool (DDOP) into the Task Controller.

Represents the situation that the DDOP is available on the side of Task Controller (e.g. via task file). An available DDOP can be activated with the Object-pool Activate message.

## Return Values

0: Function has been executed successfully

## Example

```c
long result;
result =  TCIL_MakeDdopAvailable ( TC, "xml\\sprayerV1.xml");
if (result < 0)
{
  TestStepFail("Failed to make DDOP file available!");
}
```

## Availability

| Since Version |
|---|
