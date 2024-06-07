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

from typing import Callable

import mypyrogram
from mypyrogram.filters import Filter


class OnEditedMessage:
    def on_edited_message(
        self=None,
        filters=None,
        group: int = 0
    ) -> Callable:
        """Decorator for handling edited messages.

        This does the same thing as :meth:`~mypyrogram.Client.add_handler` using the
        :obj:`~mypyrogram.handlers.EditedMessageHandler`.

        Parameters:
            filters (:obj:`~mypyrogram.filters`, *optional*):
                Pass one or more filters to allow only a subset of messages to be passed
                in your function.

            group (``int``, *optional*):
                The group identifier, defaults to 0.
        """

        def decorator(func: Callable) -> Callable:
            if isinstance(self, mypyrogram.Client):
                self.add_handler(mypyrogram.handlers.EditedMessageHandler(func, filters), group)
            elif isinstance(self, Filter) or self is None:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                func.handlers.append(
                    (
                        mypyrogram.handlers.EditedMessageHandler(func, self),
                        group if filters is None else filters
                    )
                )

            return func

        return decorator