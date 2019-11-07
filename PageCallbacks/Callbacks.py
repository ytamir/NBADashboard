from PageCallbacks import StockPriceCallbacks, FinancialMetricsCallbacks, MachineLearningCallbacks, StocksInfo


def register_callbacks(app,  cache, cache_timeout, redis_instance):
    StockPriceCallbacks.register_callbacks(app)
    FinancialMetricsCallbacks.register_callbacks(app, cache, cache_timeout, redis_instance)
    # MachineLearningCallbacks.register_callbacks(app)
    StocksInfo.register_callbacks(app)
