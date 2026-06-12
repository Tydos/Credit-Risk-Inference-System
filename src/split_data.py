import logging
from sklearn.model_selection import train_test_split


def split_dataset(dataset, target, test_size1, test_size2, is_stratify, random_state):
    trainset, tempset = train_test_split(
        dataset,
        test_size=test_size1,
        stratify=dataset[target] if is_stratify else None,  # Stratify default is active
        random_state=random_state,
    )

    valset, testset = train_test_split(
        tempset,
        test_size=test_size2,
        stratify=tempset[target] if is_stratify else None,
        random_state=random_state,
    )

    logging.info("Dataset split completed.")
    logging.info(f"Original dataset size: {len(dataset)}")
    logging.info(f"Train set size: {len(trainset)}")
    logging.info(f"Validation set size: {len(valset)}")
    logging.info(f"Test set size: {len(testset)}")
    return trainset, valset, testset
