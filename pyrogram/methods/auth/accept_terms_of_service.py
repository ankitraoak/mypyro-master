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

import mypyrogram
from mypyrogram import raw


class AcceptTermsOfService:
    async def accept_terms_of_service(
        self: "mypyrogram.Client",
        terms_of_service_id: str
    ) -> bool:
        """Accept the given terms of service.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            terms_of_service_id (``str``):
                The terms of service identifier.
        """
        r = await self.invoke(
            raw.functions.help.AcceptTermsOfService(
                id=raw.types.DataJSON(
                    data=terms_of_service_id
                )
            )
        )

        return bool(r)
