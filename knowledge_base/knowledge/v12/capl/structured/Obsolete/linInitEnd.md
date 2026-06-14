# linInitEnd

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long linInitEnd();
```

## Description

Terminates the LIN initialization procedure and starts transmission of initialization data to the hardware.

After LINInitEnd() has been called it is not possible to execute another LIN initialization.

## Return Values

!=0: Call was successful

## Availability

| Up to Version |
|---|
