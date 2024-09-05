from typing import Optional
from dataclasses import dataclass

@dataclass
class Message:
    content: Optional|str
    tts: Optional|bool
    embeds:


