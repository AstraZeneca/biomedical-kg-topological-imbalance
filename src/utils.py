# -*- coding: utf-8 -*-

import pandas as pd
from pykeen.datasets.base import Dataset
from pykeen.models import Model


def create_type(row) -> str:
    if row["in_training"] is True and row["in_testing"] is False:
        return "train"
    elif row["in_training"] is False and row["in_testing"] is True:
        return "test"
    elif row["in_training"] is False and row["in_testing"] is False:
        return "novel"
    else:
        return "unknown"


def annotate_predicted_df(
    df: pd.DataFrame,
    degs: dict,
    position: str,
) -> pd.DataFrame:
    """Annotate a pykeen predictions dataframe."""

    df["entity_type"] = df[position].str.split("::", expand=True)[0]
    df["triple_type"] = df.apply(lambda row: create_type(row), axis=1)
    df["deg"] = [degs[e] for e in list(df[position].values)]

    return df


def get_predictions_tail(
    q_entity: str,
    q_relation: str,
    data: Dataset,
    model: Model,
    degs: dict,
) -> pd.DataFrame:
    """Make a prediction using a a partial triple (missing tail)."""

    pred_df = model.get_tail_prediction_df(
        q_entity,
        q_relation,
        triples_factory=data.training,
        testing=data.testing.mapped_triples,
    )
    pred_df = annotate_predicted_df(pred_df, degs, "tail_label")

    return pred_df


def get_predictions_head(
    q_entity: str,
    q_relation: str,
    data: Dataset,
    model: Model,
    degs: dict,
) -> pd.DataFrame:
    """Make a prediction using a a partial triple (missing head)."""

    pred_df = model.get_head_prediction_df(
        q_relation,
        q_entity,
        triples_factory=data.training,
        testing=data.testing.mapped_triples,
    )
    pred_df = annotate_predicted_df(pred_df, degs, "head_label")

    return pred_df
