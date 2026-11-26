import asyncio
import json
import unittest
from unittest.mock import AsyncMock, patch

import websockets

from coinbase.constants import SUBSCRIBE_MESSAGE_TYPE, UNSUBSCRIBE_MESSAGE_TYPE
from coinbase.websocket import (
    WSClient,
    WSClientConnectionClosedException,
    WSClientException,
)

from ..constants import TEST_API_KEY, TEST_API_SECRET
from . import mock_ws_server


class WSBaseTest(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        # set the event when on_message_mock is called
        self.message_received_event = asyncio.Event()
        self.on_message_mock = unittest.mock.Mock(
            side_effect=lambda message: self.message_received_event.set()
        )

        # set up mock websocket messages
        connection_closed_exception = websockets.ConnectionClosedOK(
            1000, "Normal closure", False
        )
        self.mock_websocket = AsyncMock()
        self.mock_websocket.recv = AsyncMock(
            side_effect=[
                "test message",
                connection_closed_exception,
                connection_closed_exception,
            ]
        )

        # initialize client
        self.ws = WSClient(
            TEST_API_KEY,
            TEST_API_SECRET,
            on_message=self.on_message_mock,
            retry=False,
        )

        # initialize public client
        self.ws_public = WSClient(
            on_message=self.on_message_mock,
            retry=False,
        )

    @patch("websockets.connect", new_callable=AsyncMock)
    def test_open_twice(self, mock_connect):
        # assert you cannot open a websocket client twice consecutively
        mock_connect.return_value = self.mock_websocket

        self.ws.open()
        self.assertIsNotNone(self.ws.websocket)

        with self.assertRaises(Exception):
            self.ws.open()

    @patch("websockets.connect", new_callable=AsyncMock)
    def test_err_after_close(self, mock_connect):
        # assert you cannot close a websocket client twice consecutively
        mock_connect.return_value = self.mock_websocket

        self.ws.open()
        self.assertIsNotNone(self.ws.websocket)

        self.ws.close()

        # assert you cannot close a websocket client twice consecutively
        with self.assertRaises(Exception):
            self.ws.close()

        # assert you cannot message a websocket client after closing
        with self.assertRaises(Exception):
            self.ws.subscribe(product_ids=["BTC-USD"], channels=["ticker"])

        with self.assertRaises(Exception):
            self.ws.unsubscribe(product_ids=["BTC-USD"], channels=["ticker"])

    @patch("websockets.connect", new_callable=AsyncMock)
    async def test_on_message_exception_reaches_checker(self, mock_connect):
        mock_connect.return_value = self.mock_websocket
        for error in (RuntimeError("Stop"), websockets.ConnectionClosedOK(None, None)):
            with self.subTest(error=type(error).__name__):
                self.mock_websocket.recv.reset_mock()
                self.mock_websocket.recv.side_effect = ["update", "next update"]
                self.on_message_mock.reset_mock()
                self.on_message_mock.side_effect = error
                with self.assertLogs("coinbase.WSClient", level="ERROR") as log:
                    await self.ws.open_async()
                    try:
                        await self.ws._task
                    finally:
                        await self.ws.close_async()

                self.on_message_mock.assert_called_once_with("update")
                self.mock_websocket.recv.assert_awaited_once()
                self.assertTrue(
                    any(r.exc_info and r.exc_info[1] is error for r in log.records)
                )
                with self.assertRaises(WSClientException) as raised:
                    self.ws.sleep_with_exception_check(0)
                self.assertIn(str(error), str(raised.exception))
                self.assertIs(raised.exception.__cause__, error)
                self.ws.raise_background_exception()

    @patch("websockets.connect", new_callable=AsyncMock)
    async def test_on_message_cancellation_propagates(self, mock_connect):
        mock_connect.return_value = self.mock_websocket
        self.on_message_mock.side_effect = asyncio.CancelledError()
        await self.ws.open_async()
        try:
            with self.assertRaises(asyncio.CancelledError):
                await self.ws._task
            self.ws.raise_background_exception()
        finally:
            await self.ws.close_async()

    def test_err_unopened(self):
        # assert you cannot close an unopened websocket client
        with self.assertRaises(Exception):
            self.ws.close()

        # assert you cannot message an unopened websocket client
        with self.assertRaises(Exception):
            self.ws.subscribe(product_ids=["BTC-USD"], channels=["ticker"])

        with self.assertRaises(Exception):
            self.ws.unsubscribe(product_ids=["BTC-USD"], channels=["ticker"])

    @patch("websockets.connect", new_callable=AsyncMock)
    def test_open_and_close(self, mock_connect):
        # assert you can open and close a websocket client
        mock_connect.return_value = self.mock_websocket

        # open
        self.ws.open()
        self.assertIsNotNone(self.ws.websocket)

        # assert on_message received
        self.on_message_mock.assert_called_once_with("test message")

        # close
        self.ws.close()
        self.mock_websocket.close.assert_awaited_once()

    @patch("websockets.connect", new_callable=AsyncMock)
    def test_open_and_close_unauthenticated(self, mock_connect):
        # assert you can open and close a websocket client
        mock_connect.return_value = self.mock_websocket

        # open
        self.ws_public.open()
        self.assertIsNotNone(self.ws_public.websocket)

        # assert on_message received
        self.on_message_mock.assert_called_once_with("test message")

        # close
        self.ws_public.close()
        self.mock_websocket.close.assert_awaited_once()

    @patch("websockets.connect", new_callable=AsyncMock)
    def test_reopen(self, mock_connect):
        # assert you can open, close, reopen and close a websocket client
        mock_connect.return_value = self.mock_websocket

        # open
        self.ws.open()
        self.assertIsNotNone(self.ws.websocket)

        # close
        self.ws.close()
        self.mock_websocket.close.assert_awaited_once()

        # reopen
        self.ws.open()
        self.assertIsNotNone(self.ws.websocket)
        self.assertTrue(self.ws.websocket.open)

        # close
        self.ws.close()
        self.assertEqual(self.mock_websocket.close.await_count, 2)

    @patch("websockets.connect", new_callable=AsyncMock)
    def test_subscribe_and_unsubscribe_channel(self, mock_connect):
        # assert you can subscribe and unsubscribe to a channel
        mock_connect.return_value = self.mock_websocket

        # open
        self.ws.open()
        self.assertIsNotNone(self.ws.websocket)

        # subscribe
        self.ws.subscribe(product_ids=["BTC-USD", "ETH-USD"], channels=["ticker"])
        self.mock_websocket.send.assert_awaited_once()

        # assert subscribe message
        subscribe = json.loads(self.mock_websocket.send.call_args_list[0][0][0])
        self.assertEqual(subscribe["type"], SUBSCRIBE_MESSAGE_TYPE)
        self.assertEqual(subscribe["product_ids"], ["BTC-USD", "ETH-USD"])
        self.assertEqual(subscribe["channel"], "ticker")

        # unsubscribe
        self.ws.unsubscribe(product_ids=["BTC-USD", "ETH-USD"], channels=["ticker"])
        self.assertEqual(self.mock_websocket.send.await_count, 2)

        # assert unsubscribe message
        unsubscribe = json.loads(self.mock_websocket.send.call_args_list[1][0][0])
        self.assertEqual(unsubscribe["type"], UNSUBSCRIBE_MESSAGE_TYPE)
        self.assertEqual(unsubscribe["product_ids"], ["BTC-USD", "ETH-USD"])
        self.assertEqual(unsubscribe["channel"], "ticker")

        # close
        self.ws.close()
        self.mock_websocket.close.assert_awaited_once()

    @patch("websockets.connect", new_callable=AsyncMock)
    def test_subscribe_and_unsubscribe_channel_unauthenticated(self, mock_connect):
        # assert you can subscribe and unsubscribe to a channel
        mock_connect.return_value = self.mock_websocket

        # open
        self.ws_public.open()
        self.assertIsNotNone(self.ws_public.websocket)

        # subscribe
        self.ws_public.subscribe(
            product_ids=["BTC-USD", "ETH-USD"], channels=["ticker"]
        )
        self.mock_websocket.send.assert_awaited_once()

        # assert subscribe message
        subscribe = json.loads(self.mock_websocket.send.call_args_list[0][0][0])
        self.assertEqual(subscribe["type"], SUBSCRIBE_MESSAGE_TYPE)
        self.assertEqual(subscribe["product_ids"], ["BTC-USD", "ETH-USD"])
        self.assertEqual(subscribe["channel"], "ticker")

        # unsubscribe
        self.ws_public.unsubscribe(
            product_ids=["BTC-USD", "ETH-USD"], channels=["ticker"]
        )
        self.assertEqual(self.mock_websocket.send.await_count, 2)

        # assert unsubscribe message
        unsubscribe = json.loads(self.mock_websocket.send.call_args_list[1][0][0])
        self.assertEqual(unsubscribe["type"], UNSUBSCRIBE_MESSAGE_TYPE)
        self.assertEqual(unsubscribe["product_ids"], ["BTC-USD", "ETH-USD"])
        self.assertEqual(unsubscribe["channel"], "ticker")

        # close
        self.ws_public.close()
        self.mock_websocket.close.assert_awaited_once()

    @patch("websockets.connect", new_callable=AsyncMock)
    def test_subscribe_and_unsubscribe_channels(self, mock_connect):
        # assert you can subscribe and unsubscribe to multiple channels
        mock_connect.return_value = self.mock_websocket

        # open
        self.ws.open()
        self.assertIsNotNone(self.ws.websocket)

        # subscribe
        self.ws.subscribe(
            product_ids=["BTC-USD", "ETH-USD"], channels=["ticker", "level2"]
        )
        self.assertEqual(self.mock_websocket.send.await_count, 2)

        # assert subscribe messages
        subscribe_1 = json.loads(self.mock_websocket.send.call_args_list[0][0][0])
        self.assertEqual(subscribe_1["type"], SUBSCRIBE_MESSAGE_TYPE)
        self.assertEqual(subscribe_1["product_ids"], ["BTC-USD", "ETH-USD"])
        self.assertEqual(subscribe_1["channel"], "ticker")

        subscribe_2 = json.loads(self.mock_websocket.send.call_args_list[1][0][0])
        self.assertEqual(subscribe_2["type"], SUBSCRIBE_MESSAGE_TYPE)
        self.assertEqual(subscribe_2["product_ids"], ["BTC-USD", "ETH-USD"])
        self.assertEqual(subscribe_2["channel"], "level2")

        # unsubscribe
        self.ws.unsubscribe(
            product_ids=["BTC-USD", "ETH-USD"], channels=["ticker", "level2"]
        )
        self.assertEqual(self.mock_websocket.send.await_count, 4)

        # assert unsubscribe messages
        unsubscribe_1 = json.loads(self.mock_websocket.send.call_args_list[2][0][0])
        self.assertEqual(unsubscribe_1["type"], UNSUBSCRIBE_MESSAGE_TYPE)
        self.assertEqual(unsubscribe_1["product_ids"], ["BTC-USD", "ETH-USD"])
        self.assertEqual(unsubscribe_1["channel"], "ticker")

        unsubscribe_2 = json.loads(self.mock_websocket.send.call_args_list[3][0][0])
        self.assertEqual(unsubscribe_2["type"], UNSUBSCRIBE_MESSAGE_TYPE)
        self.assertEqual(unsubscribe_2["product_ids"], ["BTC-USD", "ETH-USD"])
        self.assertEqual(unsubscribe_2["channel"], "level2")

        # close
        self.ws.close()
        self.mock_websocket.close.assert_awaited_once()

    @patch("websockets.connect", new_callable=AsyncMock)
    def test_subscribe_and_unsubscribe_channels_unauthenticated(self, mock_connect):
        # assert you can subscribe and unsubscribe to multiple channels
        mock_connect.return_value = self.mock_websocket

        # open
        self.ws_public.open()
        self.assertIsNotNone(self.ws_public.websocket)

        # subscribe
        self.ws_public.subscribe(
            product_ids=["BTC-USD", "ETH-USD"], channels=["ticker", "level2"]
        )
        self.assertEqual(self.mock_websocket.send.await_count, 2)

        # assert subscribe messages
        subscribe_1 = json.loads(self.mock_websocket.send.call_args_list[0][0][0])
        self.assertEqual(subscribe_1["type"], SUBSCRIBE_MESSAGE_TYPE)
        self.assertEqual(subscribe_1["product_ids"], ["BTC-USD", "ETH-USD"])
        self.assertEqual(subscribe_1["channel"], "ticker")

        subscribe_2 = json.loads(self.mock_websocket.send.call_args_list[1][0][0])
        self.assertEqual(subscribe_2["type"], SUBSCRIBE_MESSAGE_TYPE)
        self.assertEqual(subscribe_2["product_ids"], ["BTC-USD", "ETH-USD"])
        self.assertEqual(subscribe_2["channel"], "level2")

        # unsubscribe
        self.ws_public.unsubscribe(
            product_ids=["BTC-USD", "ETH-USD"], channels=["ticker", "level2"]
        )
        self.assertEqual(self.mock_websocket.send.await_count, 4)

        # assert unsubscribe messages
        unsubscribe_1 = json.loads(self.mock_websocket.send.call_args_list[2][0][0])
        self.assertEqual(unsubscribe_1["type"], UNSUBSCRIBE_MESSAGE_TYPE)
        self.assertEqual(unsubscribe_1["product_ids"], ["BTC-USD", "ETH-USD"])
        self.assertEqual(unsubscribe_1["channel"], "ticker")

        unsubscribe_2 = json.loads(self.mock_websocket.send.call_args_list[3][0][0])
        self.assertEqual(unsubscribe_2["type"], UNSUBSCRIBE_MESSAGE_TYPE)
        self.assertEqual(unsubscribe_2["product_ids"], ["BTC-USD", "ETH-USD"])
        self.assertEqual(unsubscribe_2["channel"], "level2")

        # close
        self.ws_public.close()
        self.mock_websocket.close.assert_awaited_once()

    @patch("websockets.connect", new_callable=AsyncMock)
    async def test_open_and_close_async(self, mock_connect):
        # assert you can open and close a websocket client
        mock_connect.return_value = self.mock_websocket

        # open
        await self.ws.open_async()
        self.assertIsNotNone(self.ws.websocket)

        # assert on_message received
        await self.message_received_event.wait()
        self.on_message_mock.assert_called_once_with("test message")

        # close
        await self.ws.close_async()
        self.mock_websocket.close.assert_awaited_once()

    @patch("websockets.connect", new_callable=AsyncMock)
    async def test_open_and_close_async_unauthenticated(self, mock_connect):
        # assert you can open and close a websocket client
        mock_connect.return_value = self.mock_websocket

        # open
        await self.ws_public.open_async()
        self.assertIsNotNone(self.ws_public.websocket)

        # assert on_message received
        await self.message_received_event.wait()
        self.on_message_mock.assert_called_once_with("test message")

        # close
        await self.ws_public.close_async()
        self.mock_websocket.close.assert_awaited_once()

    @patch("websockets.connect", new_callable=AsyncMock)
    async def test_reopen_async(self, mock_connect):
        # assert you can open, close, reopen and close a websocket client
        mock_connect.return_value = self.mock_websocket

        # open
        await self.ws.open_async()
        self.assertIsNotNone(self.ws.websocket)

        # close
        await self.ws.close_async()
        self.mock_websocket.close.assert_awaited_once()

        # reopen
        await self.ws.open_async()
        self.assertIsNotNone(self.ws.websocket)
        self.assertTrue(self.ws.websocket.open)

        # close
        await self.ws.close_async()
        self.assertEqual(self.mock_websocket.close.await_count, 2)

    @patch("websockets.connect", new_callable=AsyncMock)
    async def test_subscribe_and_unsubscribes_channel_async(self, mock_connect):
        # assert you can subscribe and unsubscribe to a channel
        mock_connect.return_value = self.mock_websocket

        # open
        await self.ws.open_async()
        self.assertIsNotNone(self.ws.websocket)

        # subscribe
        await self.ws.subscribe_async(
            product_ids=["BTC-USD", "ETH-USD"], channels=["ticker"]
        )
        self.mock_websocket.send.assert_awaited_once()

        # assert subscribe message
        subscribe = json.loads(self.mock_websocket.send.call_args_list[0][0][0])
        self.assertEqual(subscribe["type"], SUBSCRIBE_MESSAGE_TYPE)
        self.assertEqual(subscribe["product_ids"], ["BTC-USD", "ETH-USD"])
        self.assertEqual(subscribe["channel"], "ticker")

        # unsubscribe
        await self.ws.unsubscribe_async(
            product_ids=["BTC-USD", "ETH-USD"], channels=["ticker"]
        )
        self.assertEqual(self.mock_websocket.send.await_count, 2)

        # assert unsubscribe message
        unsubscribe = json.loads(self.mock_websocket.send.call_args_list[1][0][0])
        self.assertEqual(unsubscribe["type"], UNSUBSCRIBE_MESSAGE_TYPE)
        self.assertEqual(unsubscribe["product_ids"], ["BTC-USD", "ETH-USD"])
        self.assertEqual(unsubscribe["channel"], "ticker")

        # close
        await self.ws.close_async()
        self.mock_websocket.close.assert_awaited_once()

    @patch("websockets.connect", new_callable=AsyncMock)
    async def test_subscribe_and_unsubscribes_channel_async_unauthenticated(
        self, mock_connect
    ):
        # assert you can subscribe and unsubscribe to a channel
        mock_connect.return_value = self.mock_websocket

        # open
        await self.ws_public.open_async()
        self.assertIsNotNone(self.ws_public.websocket)

        # subscribe
        await self.ws_public.subscribe_async(
            product_ids=["BTC-USD", "ETH-USD"], channels=["ticker"]
        )
        self.mock_websocket.send.assert_awaited_once()

        # assert subscribe message
        subscribe = json.loads(self.mock_websocket.send.call_args_list[0][0][0])
        self.assertEqual(subscribe["type"], SUBSCRIBE_MESSAGE_TYPE)
        self.assertEqual(subscribe["product_ids"], ["BTC-USD", "ETH-USD"])
        self.assertEqual(subscribe["channel"], "ticker")

        # unsubscribe
        await self.ws_public.unsubscribe_async(
            product_ids=["BTC-USD", "ETH-USD"], channels=["ticker"]
        )
        self.assertEqual(self.mock_websocket.send.await_count, 2)

        # assert unsubscribe message
        unsubscribe = json.loads(self.mock_websocket.send.call_args_list[1][0][0])
        self.assertEqual(unsubscribe["type"], UNSUBSCRIBE_MESSAGE_TYPE)
        self.assertEqual(unsubscribe["product_ids"], ["BTC-USD", "ETH-USD"])
        self.assertEqual(unsubscribe["channel"], "ticker")

        # close
        await self.ws_public.close_async()
        self.mock_websocket.close.assert_awaited_once()

    def test_err_calling_private_unauthenticated(self):
        # open
        self.ws_public.open()
        self.assertIsNotNone(self.ws_public.websocket)

        # assert you cannot call a private endpoint unauthenticated
        with self.assertRaises(Exception):
            self.ws.subscribe(product_ids=["BTC-USD"], channels=["user"])


class WSDisconnectionTests(unittest.IsolatedAsyncioTestCase):
    # tests that run against a mock websocket server to simulate disconnections
    async def mock_send(self, message):
        self.messages_queue.put_nowait(message)

    async def asyncSetUp(self):
        self.messages_queue = asyncio.Queue()
        self.server = await mock_ws_server.start_mock_server()

        def on_message(msg):
            self.messages_queue.put_nowait(msg)

        self.ws = WSClient(
            TEST_API_KEY,
            TEST_API_SECRET,
            base_url=f"ws://{self.server.host}:{self.server.port}",
            on_message=on_message,
            retry=False,
        )

    # self.ws._retry_base = 1
    # self.ws._retry_factor = 1.5
    # self.ws._retry_max = 5

    async def asyncTearDown(self):
        await self.server.stop()

    async def test_disconnect_error(self):
        # tests that client can catch a WSClientConnectionClosedException

        # open ws connection
        await self.ws.open_async()

        # trigger connection closed error
        await self.server.trigger_connection_closed_error()

        # Check for background exceptions
        with self.assertRaises(WSClientConnectionClosedException):
            await asyncio.wait_for(
                self.ws.run_forever_with_exception_check_async(), timeout=5
            )

    async def test_reconnect(self):
        # tests that client can automatically reconnect after a WSClientConnectionClosedException

        self.ws.retry = True

        # Open WebSocket connection
        await self.ws.open_async()
        await self.ws.subscribe_async(
            product_ids=["BTC-USD", "ETH-USD"], channels=["ticker"]
        )

        await self.messages_queue.get()
        await self.ws.subscribe_async(product_ids=["BTC-USD"], channels=["heartbeats"])
        await self.messages_queue.get()

        # disconnect and restart the server
        await self.server.restart_with_error()

        # assert resubscribe messages
        resubscribe_1 = await self.messages_queue.get()
        resubscribe_1_json = json.loads(resubscribe_1)
        self.assertEqual(resubscribe_1_json["type"], SUBSCRIBE_MESSAGE_TYPE)
        self.assertEqual(
            sorted(resubscribe_1_json["product_ids"]), ["BTC-USD", "ETH-USD"]
        )
        self.assertEqual(resubscribe_1_json["channel"], "ticker")

        resubscribe_2 = await self.messages_queue.get()
        resubscribe_2_json = json.loads(resubscribe_2)
        self.assertEqual(resubscribe_2_json["type"], SUBSCRIBE_MESSAGE_TYPE)
        self.assertEqual(resubscribe_2_json["product_ids"], ["BTC-USD"])
        self.assertEqual(resubscribe_2_json["channel"], "heartbeats")

    async def test_reconnect_fail(self):
        # tests that client can catch WSClientConnectionClosedException after failed reconnection
        self.ws.retry = True
        self.ws._retry_max_tries = 1

        # Open WebSocket connection
        await self.ws.open_async()
        await self.ws.subscribe_async(
            product_ids=["BTC-USD", "ETH-USD"], channels=["ticker"]
        )

        await self.messages_queue.get()
        await self.ws.subscribe_async(product_ids=["BTC-USD"], channels=["heartbeats"])
        await self.messages_queue.get()

        with patch(
            "websockets.connect", new=AsyncMock(side_effect=ConnectionRefusedError())
        ) as reconnect:
            await self.server.trigger_connection_closed_error()
            with self.assertRaises(WSClientConnectionClosedException):
                await asyncio.wait_for(
                    self.ws.run_forever_with_exception_check_async(), timeout=5
                )
            reconnect.assert_awaited_once()
