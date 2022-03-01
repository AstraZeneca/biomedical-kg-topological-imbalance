# -*- coding: utf-8 -*-

import pandas as pd

from pykeen.models import Model
from pykeen.datasets.base import Dataset


def create_type(row) -> str:
    if row["in_training"] == True and row["in_testing"] == False:
        return "train"
    elif row["in_training"] == False and row["in_testing"] == True:
        return "test"
    elif row["in_training"] == False and row["in_testing"] == False:
        return "novel"


def annotate_predicted_df(df: pd.DataFrame, degs: dict, position: str) -> pd.DataFrame:
    "Take a pykeen predictions dataframe and annotate with extra information"

    df["entity_type"] = df[position].str.split("::", expand=True)[0]
    df["triple_type"] = df.apply(lambda row: create_type(row), axis=1)
    df["deg"] = [degs[e] for e in list(df[position].values)]

    return df


def get_predictions_tail(
    q_entity: str, q_relation: str, data: Dataset, model: Model, degs: dict
) -> pd.DataFrame:
    "Make a prediction using a a partial triple and return a dataframe of the results"

    pred_df = model.get_tail_prediction_df(
        q_entity,
        q_relation,
        triples_factory=data.training,
        testing=data.testing.mapped_triples,
    )
    pred_df = annotate_predicted_df(pred_df, degs, "tail_label")

    return pred_df


def get_predictions_head(
    q_entity: str, q_relation: str, data: Dataset, model: Model, degs: dict
) -> pd.DataFrame:
    "Make a prediction using a a partial triple and return a dataframe of the results"

    pred_df = model.get_head_prediction_df(
        q_relation,
        q_entity,
        triples_factory=data.training,
        testing=data.testing.mapped_triples,
    )
    pred_df = annotate_predicted_df(pred_df, degs, "head_label")

    return pred_df
