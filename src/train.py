# -*- coding: utf-8 -*-

import argparse

from pykeen.pipeline import pipeline


def train(args: argparse.Namespace) -> None:
    """Train a pykeen pipeline object using TransE on Hetionet as reported in the paper"""

    result = pipeline(
        dataset="Hetionet",
        dataset_kwargs=dict(random_state=args.seed),
        model="TransE",
        model_kwargs=dict(embedding_dim=304, random_seed=args.seed),
        training_kwargs=dict(
            num_epochs=500,
            checkpoint_name="transe_hetnet_checkpoint.pt",
            checkpoint_directory=f"{args.save_path}/checkpoints/",
            checkpoint_frequency=0,
        ),
        optimizer="Adagrad",
        loss="NSSA",
        optimizer_kwargs=dict(lr=0.02),
        negative_sampler_kwargs=dict(num_negs_per_pos=61),
        evaluator_kwargs=dict(filtered=True),
        random_seed=args.seed,
    )

    result.save_to_directory(f"{args.save_path}/transe_hetnet")
    print("Pipeline Training Complete")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed used for dataset split and model init.",
    )
    parser.add_argument(
        "--save_path",
        type=str,
        default="../artifacts",
        help="Path to save model checkpoints and pipeline.",
    )

    args = parser.parse_args()
    train(args=args)
