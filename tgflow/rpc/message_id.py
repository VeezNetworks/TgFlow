import time


class MessageIdGenerator:
    def __init__(self) -> None:
        self._last_msg_id = 0

    def get_new_msg_id(self) -> int:
        now = time.time()
        nanos = int(now * 1e9)
        sec = nanos // int(1e9)
        nsec = nanos % int(1e9)
        msg_id = (sec << 32) | int((nsec * (2**32)) // 1e9)
        if msg_id <= self._last_msg_id:
            msg_id = self._last_msg_id + 4
        msg_id |= 1
        self._last_msg_id = msg_id
        return msg_id
