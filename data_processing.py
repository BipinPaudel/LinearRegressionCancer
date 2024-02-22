



def find_constant_columns(dataframe):
    """
    This function takes in a dataframe and returns

    Parameters:
    dataframe


    Returns:
    list: A list of columns that contain a single value
    """
    constant_columns = []
    for column in dataframe.columns:
        # Get unique values in the column
        unique_values = dataframe[column].unique()
        # check if the columns contains only one unique value
        if len(unique_values) == 1:
            constant_columns.append(column)
    return constant_columns



def delete_constant_columns(dataframe, columns_to_delete):
    """
    
    """
    dataframe = dataframe.drop(columns_to_delete, axis=1)
    return dataframe


def find_columns_with_few_values(dataframe, threshold):
    few_values_columns = []
    for column in dataframe.columns:
        unique_value_count = len(dataframe[column].unique())
        if unique_value_count < threshold:
            few_values_columns.append(column)

        return few_values_columns
    

def find_duplicate_rows(dataframe):
    """
    This function takes in a dataframe as input and returns a dataframe
    """
    duplicate_rows = dataframe[dataframe.duplicated()]
    return duplicate_rows

def delete_duplicate_rows(dataframe):
    dataframe = dataframe.drop_duplicates(keep="first")
    return dataframe

def drop_and_fill(dataframe):
    # Get the columns with more than 50% missing  values
    cols_to_drop = dataframe.columns[dataframe.isnull().mean()>0.5]
    #Drop the columns
    dataframe = dataframe.drop(cols_to_drop, axis=1)

    # Fill the remaining missing values with the mean of
    dataframe = dataframe.fillna(dataframe.mean())
    return dataframe
    

