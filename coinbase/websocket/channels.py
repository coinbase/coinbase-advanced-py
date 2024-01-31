from typing import List

from coinbase.constants import (
    CANDLES,
    HEARTBEATS,
    LEVEL2,
    MARKET_TRADES,
    STATUS,
    TICKER,
    TICKER_BATCH,
    USER,
)


def heartbeats(self, product_ids: List[str]):
    """
    Subscribe to heartbeats channel for a list of products_ids.
    """
    self.subscribe(product_ids, [HEARTBEATS])


async def heartbeats_async(self, product_ids: List[str]):
    """
    Async subscribe to heartbeats channel for a list of products_ids.
    """
    await self.subscribe_async(product_ids, [HEARTBEATS])


def heartbeats_unsubscribe(self, product_ids: List[str]):
    """
    Unsubscribe to heartbeats channel for a list of products_ids.
    """
    self.unsubscribe(product_ids, [HEARTBEATS])


async def heartbeats_unsubscribe_async(self, product_ids: List[str]):
    """
    Async unsubscribe to heartbeats channel for a list of products_ids.
    """
    await self.unsubscribe_async(product_ids, [HEARTBEATS])


def candles(self, product_ids: List[str]):
    """
    Subscribe to candles channel for a list of products_ids.
    """
    self.subscribe(product_ids, [CANDLES])


async def candles_async(self, product_ids: List[str]):
    """
    Async subscribe to candles channel for a list of products_ids.
    """
    await self.subscribe_async(product_ids, [CANDLES])


def candles_unsubscribe(self, product_ids: List[str]):
    """
    Unsubscribe to candles channel for a list of products_ids.
    """
    self.unsubscribe(product_ids, [CANDLES])


async def candles_unsubscribe_async(self, product_ids: List[str]):
    """
    Async unsubscribe to candles channel for a list of products_ids.
    """
    await self.unsubscribe_async(product_ids, [CANDLES])


def market_trades(self, product_ids: List[str]):
    """
    Subscribe to market_trades channel for a list of products_ids.
    """
    self.subscribe(product_ids, [MARKET_TRADES])


async def market_trades_async(self, product_ids: List[str]):
    """
    Async subscribe to market_trades channel for a list of products_ids.
    """
    await self.subscribe_async(product_ids, [MARKET_TRADES])


def market_trades_unsubscribe(self, product_ids: List[str]):
    """
    Unsubscribe to market_trades channel for a list of products_ids.
    """
    self.unsubscribe(product_ids, [MARKET_TRADES])


async def market_trades_unsubscribe_async(self, product_ids: List[str]):
    """
    Async unsubscribe to market_trades channel for a list of products_ids.
    """
    await self.unsubscribe_async(product_ids, [MARKET_TRADES])


def status(self, product_ids: List[str]):
    """
    Subscribe to status channel for a list of products_ids.
    """
    self.subscribe(product_ids, [STATUS])


async def status_async(self, product_ids: List[str]):
    """
    Async subscribe to status channel for a list of products_ids.
    """
    await self.subscribe_async(product_ids, [STATUS])


def status_unsubscribe(self, product_ids: List[str]):
    """
    Unsubscribe to status channel for a list of products_ids.
    """
    self.unsubscribe(product_ids, [STATUS])


async def status_unsubscribe_async(self, product_ids: List[str]):
    """
    Async unsubscribe to status channel for a list of products_ids.
    """
    await self.unsubscribe_async(product_ids, [STATUS])


def ticker(self, product_ids: List[str]):
    """
    Subscribe to ticker channel for a list of products_ids.
    """
    self.subscribe(product_ids, [TICKER])


async def ticker_async(self, product_ids: List[str]):
    """
    Async subscribe to ticker channel for a list of products_ids.
    """
    await self.subscribe_async(product_ids, [TICKER])


def ticker_unsubscribe(self, product_ids: List[str]):
    """
    Unsubscribe to ticker channel for a list of products_ids.
    """
    self.unsubscribe(product_ids, [TICKER])


async def ticker_unsubscribe_async(self, product_ids: List[str]):
    """
    Async unsubscribe to ticker channel for a list of products_ids.
    """
    await self.unsubscribe_async(product_ids, [TICKER])


def ticker_batch(self, product_ids: List[str]):
    """
    Subscribe to ticker_batch channel for a list of products_ids.
    """
    self.subscribe(product_ids, [TICKER_BATCH])


async def ticker_batch_async(self, product_ids: List[str]):
    """
    Async subscribe to ticker_batch channel for a list of products_ids.
    """
    await self.subscribe_async(product_ids, [TICKER_BATCH])


def ticker_batch_unsubscribe(self, product_ids: List[str]):
    """
    Unsubscribe to ticker_batch channel for a list of products_ids.
    """
    self.unsubscribe(product_ids, [TICKER_BATCH])


async def ticker_batch_unsubscribe_async(self, product_ids: List[str]):
    """
    Async unsubscribe to ticker_batch channel for a list of products_ids.
    """
    await self.unsubscribe_async(product_ids, [TICKER_BATCH])


def level2(self, product_ids: List[str]):
    """
    Subscribe to level2 channel for a list of products_ids.
    """
    self.subscribe(product_ids, [LEVEL2])


async def level2_async(self, product_ids: List[str]):
    """
    Async subscribe to level2 channel for a list of products_ids.
    """
    await self.subscribe_async(product_ids, [LEVEL2])


def level2_unsubscribe(self, product_ids: List[str]):
    """
    Unsubscribe to level2 channel for a list of products_ids.
    """
    self.unsubscribe(product_ids, [LEVEL2])


async def level2_unsubscribe_async(self, product_ids: List[str]):
    """
    Async unsubscribe to level2 channel for a list of products_ids.
    """
    await self.unsubscribe_async(product_ids, [LEVEL2])


def user(self, product_ids: List[str]):
    """
    Subscribe to user channel for a list of products_ids.
    """
    self.subscribe(product_ids, [USER])


async def user_async(self, product_ids: List[str]):
    """
    Async subscribe to user channel for a list of products_ids.
    """
    await self.subscribe_async(product_ids, [USER])


def user_unsubscribe(self, product_ids: List[str]):
    """
    Unsubscribe to user channel for a list of products_ids.
    """
    self.unsubscribe(product_ids, [USER])


async def user_unsubscribe_async(self, product_ids: List[str]):
    """
    Async unsubscribe to user channel for a list of products_ids.
    """
    await self.unsubscribe_async(product_ids, [USER])
