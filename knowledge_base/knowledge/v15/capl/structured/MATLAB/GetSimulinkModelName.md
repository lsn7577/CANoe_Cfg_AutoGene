# GetSimulinkModelName

> Category: `MATLAB` | Type: `function`

## Syntax

```c
long GetSimulinkModelName( char[] buffer, dword bufferSize);
```

## Description

Gets the name of the Simulink model.

## Parameters

| Name | Description |
|---|---|
| buffer | The name of the Simulink model will be written to this buffer. |
| bufferSize | The size of buffer in bytes. |

## Return Values

On success 0, otherwise a value unequal to zero.

## Example

```c
on start
{
  char buffer[30];
  if (GetSimulinkModelName(buffer, 30) == 0)
  {
    write(“Simulink model: %s”, buffer);
  }
}
```

## Availability

- Availability
