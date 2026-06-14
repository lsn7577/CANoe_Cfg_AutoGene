# Example: Selector CAN (controller number)

> Category: `CAN` | Type: `selector`

### Example Selector CAN (controller number)

```c
message 0x100 msg = {dlc = 2, word(0) = 0x1234};

on key '1' {
  write("sende via CAN 1");
  msg.CAN = 1;
  output(msg);
}
on key '2' {
  write("sende via CAN 2");
  msg.CAN = 2;
  output(msg);
}
```
