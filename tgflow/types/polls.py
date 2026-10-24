from typing import Any, Optional


class PollOption:
    def __init__(self, text: str, voter_count: int = 0) -> None:
        self.text = text
        self.voter_count = voter_count


class Poll:
    def __init__(
        self,
        id: str,
        question: str,
        options: list[PollOption],
        total_voter_count: int = 0,
        is_closed: bool = False,
        is_anonymous: bool = True,
        type: str = "regular",
        allows_multiple_answers: bool = False,
        correct_option_id: int | None = None,
        explanation: str | None = None,
    ) -> None:
        self.id = id
        self.question = question
        self.options = options
        self.total_voter_count = total_voter_count
        self.is_closed = is_closed
        self.is_anonymous = is_anonymous
        self.type = type
        self.allows_multiple_answers = allows_multiple_answers
        self.correct_option_id = correct_option_id
        self.explanation = explanation


class PollAnswer:
    def __init__(self, poll_id: str, voter_chat: Any = None, user: Any = None, option_ids: list[int] | None = None) -> None:
        self.poll_id = poll_id
        self.voter_chat = voter_chat
        self.user = user
        self.option_ids = option_ids or []
