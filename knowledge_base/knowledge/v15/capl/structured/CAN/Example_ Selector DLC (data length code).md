# Example: Selector DLC (data length code)

> Category: `CAN` | Type: `selector`

### Example Selector DLC (data length code)

```c
on message OneByteMessage {
  if (this.DLC != 1) {
    write("error: OneByteMessage has DLC != 1");
    stop();
  }
}
```
