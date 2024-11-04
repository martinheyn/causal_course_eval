# A function to import rdata to Python
def import_rdata(rdata_object_name,listtruefalse,modelname):             
      
      import rpy2.robjects as robjects
      from rpy2.robjects.packages import importr
      import pandas as pd
      
      # Read rdata object
      rdata_object = robjects.globalenv[rdata_object_name]
      # Force it into a pandas frame
      rdata_2_pd = pd.DataFrame.from_records(rdata_object)
      # Transpose the pandas frame (because somehow its 90 degrees turned...)
      pd_out = rdata_2_pd.transpose()
      
      # Read column names from rdata
      if listtruefalse: # Some variable names are within rdata variables
            if isinstance(rdata_object, robjects.ListVector):
                  column_names = list(rdata_object.names)
      else: # Otherwise the names of the rdata variables themselves
            column_names = list(rdata_object.colnames)
      
      # Write column names to pandas dataframe
      pd_out.columns = column_names
      
      # Add column with model name
      pd_out['model'] = modelname
      
      return pd_out

