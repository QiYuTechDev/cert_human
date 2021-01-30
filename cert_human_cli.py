#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Command line interface to request a URL and get the server cert or cert chain."""

import argparse
import sys

import cert_human_py3


def cli(argv):
    """Parse arguments.

    Args:
        argv (:obj:`list`): sys.argv or manual list of args to parse.

    Returns:
        (:obj:`argparse.Namespace`)

    """
    fmt = argparse.ArgumentDefaultsHelpFormatter
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=fmt)
    parser.add_argument(
        "host",
        metavar="HOST",
        action="store",
        type=str,
        help="Host to get cert or cert chain from",
    )
    parser.add_argument(
        "--port",
        default=443,
        action="store",
        required=False,
        type=int,
        help="Port on host to connect to",
    )
    return parser.parse_args(argv)


def main(cli_args):
    """Process arguments and run the workflows.

    Args:
        cli_args (:obj:`argparse.Namespace`): Parsed args from sys.argv or list.

    """
    store_obj = cert_human_py3.CertChainStore.from_socket(
        host=cli_args.host, port=cli_args.port
    )

    print(store_obj.dump_json)


if __name__ == "__main__":
    cli_args = cli(argv=sys.argv[1:])
    main(cli_args)
