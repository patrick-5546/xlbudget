"""The commands, implemented as implementations of the abstract class `Command`."""

import sys
from abc import ABC, abstractmethod
from argparse import ArgumentParser, Namespace, _SubParsersAction
from typing import List, Type


class Command(ABC):
    """The abstract class that the command implementations implement."""

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def aliases(self) -> List[str]:
        pass

    @classmethod
    @abstractmethod
    def configure_args(cls, subparsers: _SubParsersAction) -> None:
        pass

    @abstractmethod
    def __init__(self, args: Namespace) -> None:
        pass

    @abstractmethod
    def run(self) -> None:
        pass


class Generate(Command):
    """The `generate` command implementation.

    Attributes:
        name (str): The command's CLI name.
        aliases (List[str]): The command's CLI aliases.
    """

    name: str = "generate"
    aliases: List[str] = ["g"]

    @classmethod
    def configure_args(cls, subparsers: _SubParsersAction) -> None:
        """Configures the argument parser for the `generate` command.

        Args:
            subparsers (_SubParsersAction): The command `subparsers`.
        """
        parser = common_arg_config(
            subparsers,
            name=cls.name,
            aliases=cls.aliases,
            help="generate a new excelbudget file",
            init=Generate,
        )

        parser.add_argument(
            "-f", "--force", action="store_true", help="overwrite file if it exists"
        )

    def __init__(self, args: Namespace) -> None:
        pass

    def run(self) -> None:
        raise NotImplementedError


class Update(Command):
    """The `update` command implementation.

    Attributes:
        name (str): The command's CLI name.
        aliases (List[str]): The command's CLI aliases.
    """

    name: str = "update"
    aliases: List[str] = ["u"]

    @classmethod
    def configure_args(cls, subparsers: _SubParsersAction) -> None:
        """Configures the argument parser for the `update` command.

        Args:
            subparsers (_SubParsersAction): The command `subparsers`.
        """
        common_arg_config(
            subparsers,
            name=cls.name,
            aliases=cls.aliases,
            help="update an existing excelbudget file",
            init=Update,
        )

    def __init__(self, args: Namespace) -> None:
        pass

    def run(self) -> None:
        raise NotImplementedError


class Validate(Command):
    """The `validate` command implementation.

    Attributes:
        name (str): The command's CLI name.
        aliases (List[str]): The command's CLI aliases.
    """

    name: str = "validate"
    aliases: List[str] = ["v"]

    @classmethod
    def configure_args(cls, subparsers: _SubParsersAction) -> None:
        """Configures the argument parser for the `validate` command.

        Args:
            subparsers (_SubParsersAction): The command `subparsers`.
        """
        common_arg_config(
            subparsers,
            name=cls.name,
            aliases=cls.aliases,
            help="validate an existing excelbudget file",
            init=Validate,
        )

    def __init__(self, args: Namespace) -> None:
        pass

    def run(self) -> None:
        raise NotImplementedError


def get_cmd_cls_from_str(cls_name: str) -> Type[Command]:
    return getattr(sys.modules[__name__], cls_name)


def common_arg_config(
    subparsers: _SubParsersAction,
    name: str,
    aliases: List[str],
    help: str,
    init: Type[Command],
) -> ArgumentParser:
    parser = subparsers.add_parser(name, aliases=aliases, help=help)
    parser.set_defaults(init=init)
    return parser
