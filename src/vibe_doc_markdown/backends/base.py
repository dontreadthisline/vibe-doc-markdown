from __future__ import annotations

from abc import ABC, abstractmethod

from ..types import Backend, ConvertInput, ConvertResult


class AbstractBackend(ABC):
    @abstractmethod
    def convert(self, input: ConvertInput) -> ConvertResult: ...

    @property
    @abstractmethod
    def name(self) -> Backend: ...
