#!/usr/bin/env python3

from scipy.stats import bootstrap
import click
import json
import numpy as np


@click.command()
@click.argument("data", type=click.File(mode="r", encoding="UTF-8"), nargs=-1)
@click.option(
    "confidence_level",
    "-c",
    "--confidence_level",
    type=float,
    default=0.95,
    show_default=True,
    help="Confidence level",
)
@click.option(
    "n_resamples",
    "-n",
    "--n_resamples",
    type=int,
    default=1000,
    show_default=True,
    help="Number of resamples",
)
@click.option(
    "with_bootstrap_distribution",
    "--with-bootstrap-distribution/--no-with-bootstrap-distribution",
    type=bool,
    default=False,
    show_default=True,
    help="Output the bootstrap distribution",
)
def main(
    data,
    confidence_level: float,
    n_resamples: int,
    with_bootstrap_distribution: bool,
):
    """
    Calculate bootstrap resampling.
    """
    statistic = eval("np.mean") or np.mean
    for d in data:
        distribution = list(map(float, d.readlines()))
        res = bootstrap(
            [distribution],
            statistic,
            confidence_level=confidence_level,
            n_resamples=n_resamples,
        )
        dist = (
            {
                "bootstrap_distribution": res.bootstrap_distribution.tolist(),
            }
            if with_bootstrap_distribution
            else {}
        )
        print(
            json.dumps(
                {
                    "mean": np.mean(distribution).item(),
                    "confidence_interval": {
                        "low": res.confidence_interval.low,
                        "high": res.confidence_interval.high,
                    },
                    "standard_error": res.standard_error,
                    "data": distribution,
                }
                | dist
            )
        )


if __name__ == "__main__":
    main()
