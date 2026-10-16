import unittest

from coinbase.deribit.errors import (
    DeribitInsufficientFundsError,
    DeribitInvalidParamsError,
    DeribitMatchingQueueFullError,
    DeribitRateLimitError,
    DeribitRPCError,
    rpc_error_from,
)


class DeribitErrorsTest(unittest.TestCase):
    def test_rate_limit_mapping_with_retry_after(self):
        e = rpc_error_from(
            {
                "code": 10028,
                "message": "too_many_requests",
                "data": {"retry_after": 1.5},
            }
        )
        self.assertIsInstance(e, DeribitRateLimitError)
        self.assertEqual(e.retry_after, 1.5)

    def test_matching_queue_full(self):
        self.assertIsInstance(
            rpc_error_from({"code": 10047, "message": "full"}),
            DeribitMatchingQueueFullError,
        )

    def test_insufficient_funds(self):
        self.assertIsInstance(
            rpc_error_from({"code": 10009, "message": "nsf"}),
            DeribitInsufficientFundsError,
        )

    def test_invalid_params(self):
        self.assertIsInstance(
            rpc_error_from({"code": 11030, "message": "bad"}),
            DeribitInvalidParamsError,
        )

    def test_unknown_code_falls_back_to_base(self):
        e = rpc_error_from({"code": 99999, "message": "unknown"})
        self.assertIs(type(e), DeribitRPCError)
        self.assertEqual(e.code, 99999)
        self.assertEqual(e.message, "unknown")

    def test_jsonrpc_invalid_params_maps_to_invalid_params_error(self):
        from coinbase.deribit.errors import DeribitInvalidParamsError, rpc_error_from

        err = rpc_error_from({"code": -32602, "message": "Invalid params"})
        self.assertIsInstance(err, DeribitInvalidParamsError)


if __name__ == "__main__":
    unittest.main()
