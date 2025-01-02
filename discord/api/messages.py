from typing import Optional, List, Literal
from 

class Embed:
    title: Optional[str]
    _type: Optional[Literal["rich", "image", "video", "gifv", "article", "link", "poll_result"]]
    description: Optional[str]
    url: Optional[str]
    timestamp: Optional[str]

class Message:
    content: Optional[str]
    tts: Optional[bool]
    embeds: List[Embed]


