"""Modelo reproducible y acotado para configuraciones esfericas centradas."""

from .configurations import named_configurations
from .geometry import configuration_report, epsilon_threshold

__all__ = ["named_configurations", "configuration_report", "epsilon_threshold"]
