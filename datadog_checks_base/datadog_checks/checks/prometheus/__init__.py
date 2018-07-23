# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

try:
    # Agent5 compatibility layer
    from checks import (
        UnknownFormatError,
        PrometheusCheck
    )
except ImportError:
    from .mixins import UnknownFormatError
    from .prometheus_base import PrometheusCheck
    from .base_check import GenericPrometheusCheck

from .base_check import PrometheusScraper

__all__ = [
    'UnknownFormatError',
    'PrometheusCheck',
    'GenericPrometheusCheck',
    'PrometheusScraper',
]
