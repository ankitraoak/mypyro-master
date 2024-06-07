#  mypyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of mypyrogram.
#
#  mypyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  mypyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with mypyrogram.  If not, see <http://www.gnu.org/licenses/>.

from uuid import uuid4

import mypyrogram
from mypyrogram import types
from ..object import Object


class InlineQueryResult(Object):
    """One result of an inline query.

    - :obj:`~mypyrogram.types.InlineQueryResultCachedAudio`
    - :obj:`~mypyrogram.types.InlineQueryResultCachedDocument`
    - :obj:`~mypyrogram.types.InlineQueryResultCachedAnimation`
    - :obj:`~mypyrogram.types.InlineQueryResultCachedPhoto`
    - :obj:`~mypyrogram.types.InlineQueryResultCachedSticker`
    - :obj:`~mypyrogram.types.InlineQueryResultCachedVideo`
    - :obj:`~mypyrogram.types.InlineQueryResultCachedVoice`
    - :obj:`~mypyrogram.types.InlineQueryResultArticle`
    - :obj:`~mypyrogram.types.InlineQueryResultAudio`
    - :obj:`~mypyrogram.types.InlineQueryResultContact`
    - :obj:`~mypyrogram.types.InlineQueryResultDocument`
    - :obj:`~mypyrogram.types.InlineQueryResultAnimation`
    - :obj:`~mypyrogram.types.InlineQueryResultLocation`
    - :obj:`~mypyrogram.types.InlineQueryResultPhoto`
    - :obj:`~mypyrogram.types.InlineQueryResultVenue`
    - :obj:`~mypyrogram.types.InlineQueryResultVideo`
    - :obj:`~mypyrogram.types.InlineQueryResultVoice`
    """

    def __init__(
        self,
        type: str,
        id: str,
        input_message_content: "types.InputMessageContent",
        reply_markup: "types.InlineKeyboardMarkup"
    ):
        super().__init__()

        self.type = type
        self.id = str(uuid4()) if id is None else str(id)
        self.input_message_content = input_message_content
        self.reply_markup = reply_markup

    async def write(self, client: "mypyrogram.Client"):
        pass
