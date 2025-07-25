# pyre-strict
import argparse

from opensfm.actions import detect_features
from opensfm.dataset import DataSet

from . import command


class Command(command.CommandBase):
    name = "detect_features"
    help = "Compute features for all images"

    def run_impl(self, dataset: DataSet, args: argparse.Namespace) -> None:
        detect_features.run_dataset(dataset)

    def add_arguments_impl(self, parser: argparse.ArgumentParser) -> None:
        pass
