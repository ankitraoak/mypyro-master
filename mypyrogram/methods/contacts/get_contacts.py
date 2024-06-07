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

import logging
from typing import List

import mypyrogram
from mypyrogram import raw
from mypyrogram import types

log = logging.getLogger(__name__)


class GetContacts:
    async def get_contacts(
        self: "mypyrogram.Client"
    ) -> List["types.User"]:
        """Get contacts from your Telegram address book.

        .. include:: /_includes/usable-by/users.rst

        Returns:
            List of :obj:`~mypyrogram.types.User`: On success, a list of users is returned.

        Example:
            .. code-block:: python

                contacts = await app.get_contacts()
                print(contacts)
        """
        contacts = await self.invoke(raw.functions.contacts.GetContacts(hash=0))
        return types.List(types.User._parse(self, user) for user in contacts.users)
