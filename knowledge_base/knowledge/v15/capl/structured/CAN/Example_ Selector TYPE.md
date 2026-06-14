# Example: Selector TYPE

> Category: `CAN` | Type: `selector`

### Example Selector TYPE

```c
message 0x100 resp_msg = {dlc = 2, word(0) = 0x1234};

on message 0x100 {
  if (this.TYPE == RXREMOTE) {
    // remote frame 0x100 received
    output(resp_msg);
  }
}
```
