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

import asyncio
import inspect

import mypyrogram
from mypyrogram.methods.utilities.idle import idle


class Run:
    def run(
        self: "mypyrogram.Client",
        coroutine=None
    ):
        """Start the client, idle the main script and finally stop the client.

        When calling this method without any argument it acts as a convenience method that calls
        :meth:`~mypyrogram.Client.start`, :meth:`~mypyrogram.idle` and :meth:`~mypyrogram.Client.stop` in sequence.
        It makes running a single client less verbose.

        In case a coroutine is passed as argument, runs the coroutine until it's completed and doesn't do any client
        operation. This is almost the same as :py:obj:`asyncio.run` except for the fact that mypyrogram's ``run`` uses the
        current event loop instead of a new one.

        If you want to run multiple clients at once, see :meth:`mypyrogram.compose`.

        Parameters:
            coroutine (``Coroutine``, *optional*):
                Pass a coroutine to run it until it completes.

        Raises:
            ConnectionError: In case you try to run an already started client.

        Example:
            .. code-block:: python

                from mypyrogram import Client

                app = Client("my_account")
                ...  # Set handlers up
                app.run()

            .. code-block:: python

                from mypyrogram import Client

                app = Client("my_account")


                async def main():
                    async with app:
                        print(await app.get_me())


                app.run(main())
        """
        loop = asyncio.get_event_loop()
        run = loop.run_until_complete

        if coroutine is not None:
            run(coroutine)
        else:
            if inspect.iscoroutinefunction(self.start):
                run(self.start())
                run(idle())
                run(self.stop())
            else:
                self.start()
                run(idle())
                self.stop()
