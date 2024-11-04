# Defines a function for plotting pretty boxplots
def plot_pretty_boxplot(dataframe, data_name, filename, xdown, xup, label, palette):
      
      import seaborn as sns
      import matplotlib.pyplot as plt

      # Initialize the figure
      f, ax = plt.subplots(figsize=(3.5, 1.75))

      # Add in points to show each observation
      # sns.stripplot(data=dataframe, x=data_name, y="model",
      #            size=0.5, color=".3", linewidth=0)
      
      # Plot the parameter values with horizontal boxes
      sns.boxplot(data=dataframe, x=data_name, y="model", 
                whis=[0, 100], width=.3, palette=palette,
        whiskerprops=dict(color="black"),
        boxprops=dict(edgecolor='black'),
        capprops=dict(color="black"),
        medianprops=dict(color="black"))
      
      ax.set_xlim(xdown, xup)
      
      plt.grid("True")
      plt.subplots_adjust(bottom=0.3)
      plt.xlabel(label)
      plt.savefig(filename + '.pdf', format='pdf')