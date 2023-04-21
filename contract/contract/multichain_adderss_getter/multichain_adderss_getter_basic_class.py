import abc

from pydantic import BaseModel

from contract.enum.chain_id_enum import ChainIdEnum


class MultichainAddressGetterBasicClass(abc.ABC):

    @abc.abstractmethod
    def __init__(self, config: dict[ChainIdEnum, BaseModel]):
        self.config = config

    @abc.abstractmethod
    def get_chain(self, address):
        raise NotImplementedError
