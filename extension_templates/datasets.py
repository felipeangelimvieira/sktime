"""Extension template for datasets."""

from sktime.datasets.forecasting._base import BaseForecastingDataset


class MyForecastingDataset(BaseForecastingDataset):
    """
    Extension template for forecasting datasets.

    # todo: add description of the dataset

    Parameters
    ----------
    parama: str
        Description of parama.
    paramb: str, optional
        Description of paramb.
    paramc: str, optional
        Description of paramc.
    """

    _tags = {
        # Tag: is_univariate - Set to True if the dataset contains a single
        # variable (i.e. the target 'y' has one dimension).
        #  Change to False if multiple variables are present.
        "is_univariate": True,
        # Tag: is_equally_spaced - Set to True if the time intervals between
        # observations are consistent.
        # Modify if the time series data has irregular intervals.
        "is_equally_spaced": True,
        # Tag: has_nans - Set to True if the dataset contains missing values.
        # Change to False if the dataset is complete.
        "has_nans": False,
        # Tag: has_exogenous - Set to True if the dataset includes exogenous
        # (external) variables. Change to False if the dataset only contains
        # endogenous variables.
        "has_exogenous": False,
        # Tag: n_instances - Number of instances in the dataset.
        # Set to the number of rows in the target 'y' dataframe.
        "n_instances": None,
        # Tag: n_instances_train - Number of instances in the training set.
        # Set to the number of rows in the training target 'y_train' dataframe.
        "n_instances_train": 0,
        # Tag: n_instances_test - Number of instances in the test set.
        # Set to the number of rows in the test target 'y_test' dataframe.
        "n_instances_test": 0,
        # Tag: n_timepoints - Number of timepoints in the dataset.
        # Set to the maximum number of timepoints in the dataset.
        # In the case where this dataset contain series of different lengths,
        # set this to the maximum length.
        "n_timepoints": None,
        # Tag: n_timepoints_train - Number of timepoints in the training set.
        # Set to the maximum number of timepoints in the training set.
        # In the case where this dataset contain series of different lengths,
        # set this to the maximum length.
        "n_timepoints_train": None,
        # Tag: n_timepoints_test - Number of timepoints in the test set.
        # Set to the maximum number of timepoints in the test set.
        # In the case where this dataset contain series of different lengths,
        # set this to the maximum length.
        "n_timepoints_test": None,
        # Tag: frequency - Frequency of the time series in the dataset.
        # Set to the frequency of the time series data.
        # If the frequency is not related to a time unit, this can be an
        # integer.
        "frequency": "M",
        # Tag: n_dimensions - Number of dimensions in the dataset.
        # Set to the number of columns in the target 'y' dataframe.
        # This should be consistent with is_univariate tag.
        "n_dimensions": 1,
        # Tag: is_one_panel - Set to True if the dataset contains a single
        #  panel.
        # Change to False if the dataset contains multiple panels.
        "is_one_panel": True,
        # Tag: n_panels - Number of panels in the dataset.
        # Set to the number of unique time series in the dataset.
        # This should be consistent with is_one_panel tag.
        "n_panels": 1,
        # Tag: n_hierarchy_levels - Number of levels in the hierarchy of the
        #  dataset.
        # Set to the number of index levels in the target 'y' dataframe,
        # excluding the time index.
        "n_hierarchy_levels": 0,
        # Tag: is_one_series - Set to True if the dataset contains a single
        # series.
        # Change to False if the dataset contains multiple series.
        # This should be consistent with is_one_panel tag, and is_univariate
        # tag.
        "is_one_series": True,
    }

    def __init__(self, parama, paramb="default", paramc=None):
        # todo: set hyperparameters to self
        self.parama = parama
        self.paramb = paramb
        self.paramc = paramc

        # Intialize the base object
        super().__init__()

        # todo: optional, parameter checking logic (if applicable) should happen
        #  here
        # if writes derived values to self, should *not* overwrite self.parama
        # etc
        # instead, write to self._parama, self._newparam (starting with _)

    def _load(self, *args):
        """
        Load the dataset.

        Receives a tuple of strings that specify what to load.

        Parameters
        ----------
        *args: tuple of strings that specify what to load
            valid strings are "X", "y", "X_test", "y_test", "X_train", "y_train"
            and "cv". "cv" should return a generator that yields
            X_train, y_train, X_test, y_test.
        """

        # todo: add loading logic here
        # check if X, X_train or X_test are requested, and load them accordingly
        # check if y, y_train or y_test are requested, and load them accordingly
        # check if cv is requested, and create a generator that yields

        # The _load should return the requested data in the order specified by args
        # This can be achieved by, for example, creating a dictionary with keys
        # "X", "y", "X_test", "y_test", "X_train", "y_train", "cv" during load
        # and then returning the values in the order specified by args
