
import pandas as pd
import math
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
class Sizes():
  """Plots data points 'distributions for each histogram's bins.

  Tags each data point accordingly to if it commercial or not, wiht the bin
  name the data point has to fall and the distance from the data point to
  the bin's floor

  Args:

    datafile : it is a csv file wiht one colunm of fruit diameters. It is 
              raw data file extracted fron the caliper
  """

  def __init__(self, dataframe:pd.DataFrame, ISO_LANG="POR"):
    if dataframe.empty:
      dataframe=({'diameter' : [1,2,3,4,5]})
    
    self.df = dataframe
    self.commercial = 0 #minimal diameter defines comercial fruit
    self.bin_width = 5 #Defautl to hold 5 integer sizes inside a bin
    self.max = self.df.max()[0]
    self.min = self.df.min()[0]
    self.mean = self.df.mean()[0]
    
    #Holds the floor of the minimum bin and the ceil of the maximun bin
    self.__floor = 0
    self.__ceil = 0

    #For the commercial data set and its main characterístics
    self.__df_commercial = 0
    self.__max_comercial = 0
    self.__min_comercial = 0
    self.__mean_comercial = 0

    #For the under commercial data set and its main characterístics
    self.__df_under_commercial = 0
    self.__max_under_comercial = 0
    self.__min_under_comercial = 0
    self.__mean_under_comercial = 0



    self.__under_commercial_label = "UNDER"
    self.__commercial_label = "COM"


    self.__num_bins = 0
    self.__bins_names = []
    self.__my_languaje = ISO_LANG

    self.__texts={
        "ENG":{
              "violin_bins_title":"Fruit size distribution inside each box of the histogram",
              "violin_bins_xaxes":"DIameter in millimeters",
              
              "chart_histogram_yaxe":"Number of fruits"
              },


        "ESP":{
              "violin_bins_title":"Distribución del tamaño de la fruta en cada contenedor del histograma",
              "violin_bins_xaxes":"Diámetro en milímetros",
              "chart_histogram_yaxe":"Número de frutas"
              },


        "FRA":{
              "violin_bins_title":"Répartition de la taille des fruits à l'intérieur de chaque case de l'histogramme",
              "violin_bins_xaxes":"Diamètre en millimètres",
              "chart_histogram_yaxe":"Nombre de fruits"
              },


        "POR":{
              "violin_bins_title":"Distribuição do tamanho dos frutos dentro de cada caixa do histograma",
              "violin_bins_xaxes":"Diâmetro em milímetros",
              "chart_histogram_yaxe":"Número de frutas"
              },


        "CAT":{
              "violin_bins_title":"Distribució de la mida del fruit<br>dins de cada caixa de l'histograma",
              "violin_bins_xaxes":"Diàmètre en mil.límetres",
              "chart_histogram_yaxe":"Nombre de fruites"
              }
        }

    self.set_floor()
    self.set_ceil()
    self.set_num_bins()
    self.set_bins_name()


  def set_floor(self):
    """calculates de minimun value from all potential bins intervals."""
    print ("min", self.min)
    self.floor= math.floor(self.min/10) * 10
  
  def set_ceil(self):
    """ calculates de maximun value from all potential bins intervals."""
    self.ceil = math.ceil(self.max/10) * 10

  def set_num_bins(self):
    """ calculates the number of times the bin Width fits in the distance
    between floor and ceil . """
    self.num_bins= (self.ceil - self.floor)//self.bin_width

  def set_comercial (self, diametro:int):
    """ Splits the data set between non-commercial and commercial fruits.
    
    Keyword arguments:
    diametro -- data points less than diametro as non-comercial

    Once diametro is known, the data set is filtered to tag each data point
    as non-comercial or commercial.

    Splits dataframe in two dataframes, no-commercial and commercial data points
    """
    self.commercial = diametro
    self.filter_comercial()
    self.split_df()

  def get_commercial(self):
    """Informs the size threshold for commercial, non commericial sizes"""
    return self.commercial

  def get_mean(self,subset= "all"):
    """return the mean of the data points in a subset.

    Parameters
    ----------
    subset -- String: 'COM' for comercial data points
                      'UNDER for no comercial data point

    """
    if subset == self.__under_commercial_label:
      return self.__mean_under_comercial
    elif subset == self.__commercial_label:
      return self.__mean_comercial
    else:
      return self.mean

  def set_bin_width (self, width):
    # sets bin width
    self.bin_width = width
    # if bind widht changes, so num bins
    self.set_num_bins()
    # so bins names
    self.set_bins_name()
    # retagginf data points mandatory
    self.filter_comercial()

  def get_bin_width(self):
    """Informs actual bin width to for data point classification"""
    return self.bin_width



  def set_bins_name(self):
    """ creates a list of intervals tags ('[45..50[') to name bins.  
    
    1st step: construct a list wiht intervals floor
    2nd step: construct the intervals list
    3rd step: Asign the list to the Class atrribute

    """
    #let's create a list starting in the floor and growing at bin width
    aa=[]
    for i in range(self.floor, self.ceil + self.bin_width, self.bin_width):
      aa.append(i)

    #lets create a list of intervals
    bins=[]
    for elem in range(0, len(aa)-1):
      bin="[" + str(aa[elem]) +".." +str(aa[elem + 1])+"["
      bins.append(bin)
    self.bins_names = bins

    #A solution in only one for sentence can be done

  def distance_to_floor_and_bin_name(self, data_point):
    ''' Get data point's distance to its bin's floor & bin's name

    Parameters
    ----------
    data_point -- float: a fruit measure

    Returns
    -------
    bin_name -- string: with bin name in format [15..18[
    distance -- float: wiht distance from data-point to bin floor

    '''
    #1st figure out the bin number where data point fits
    bin_number = (int(data_point) -self.floor) // self.bin_width
    bin_name   = self.bins_names[bin_number]

    #2nd converts to integer bin's floor. From a bin name [15..18[
    #figures after [ and before first dot] casted to int
    bin_floor  = int(bin_name[1:bin_name.find(".")])
    
    #3rd calculates data point's distance to its bin's floor 
    distance   = data_point - bin_floor

    return (bin_name, distance)
 

  def filter_comercial(self):
    """ Tags data point . 
    
    loops data frame tagging each data point wiht these criteria
    - if it is commercial or non commercial fruit
    - bin name of the bin where fruit measure fails
    - distance from the fruit measure to the floor of the bin.

    """

    my_comercial=[]   #Commercial or non commercial Tags list
    my_bin=[]         #Bin name Tags list
    my_distance=[]     #Data point distance to its bin floor


    for i in range(len(self.df.index)):
      diameter = self.df.iloc[i]['diameter']
      bin_name, distance = self.distance_to_floor_and_bin_name(diameter)
      my_bin.append(bin_name)
      my_distance.append(distance)

      if diameter > self.commercial:
        my_comercial.append(self.__commercial_label)
      else:
        my_comercial.append(self.__under_commercial_label)

    self.df["comercial"] = my_comercial
    self.df["my_bin"] = my_bin
    self.df["distance"] = my_distance

  def split_df(self):
    """ Splits the original data set in two folloign commercial throshold. """

    self.df_commercial =self.df[self.df["comercial"] == self.__commercial_label]
    self.__max_comercial = self.df_commercial.max()[0]
    self.__min_comercial = self.df_commercial.min()[0]
    self.__mean_comercial = self.df_commercial.mean(numeric_only= True)[0]
    self.df_under_commercial =self.df[self.df["comercial"] == self.__under_commercial_label]
    self.__max_under_comercial = self.df_under_commercial.max()[0]
    self.__min_under_comercial = self.df_under_commercial.min()[0]
    self.__mean_under_comercial = self.df_under_commercial.mean(numeric_only= True)[0]

  def chart_scatter_px(self, label=None):
    if label == self.__commercial_label:
      fig = px.scatter(self.df_commercial, 
                       x='diameter', 
                       y='diameter',
                       color='comercial', 
                       range_x=[self.floor, self.ceil],
                       range_y=[self.floor, self.ceil],
                       color_discrete_sequence=[ "green"]
                       )
    elif label == self.__under_commercial_label:
      fig = px.scatter(self.df_under_commercial, 
                       x='diameter', 
                       y='diameter',
                       color='comercial',
                       range_x=[self.floor, self.ceil],
                       range_y=[self.floor, self.ceil],
                       color_discrete_sequence=[ "red"]
                       )
    else:
      fig = px.scatter(self.df, 
                       x='diameter', 
                       y='diameter',
                       color='comercial',
                       range_x=[self.floor, self.ceil],
                       range_y=[self.floor, self.ceil],
                       color_discrete_sequence=[ "green", "red"]
                       )
    return fig

  def __chart_scatter_go(self, label=None):
    if label == self.__commercial_label:
      fig = go.Scatter(x=self.df_commercial["diameter"], 
                       y=self.df_commercial["diameter"],
                       marker_color='rgb(0,255,0)',
                       name="Commercial") 
                       #range_x=[self.floor, self.ceil],
                       #range_y=[self.floor, self.ceil],
                       #color_discrete_sequence=[ "green"] )
    elif label == self.__under_commercial_label:
      fig = go.Scatter(x=self.df_under_commercial["diameter"], 
                       y=self.df_under_commercial["diameter"],
                       marker_color='rgb(255,0,0)',
                       name="industry") 
                       #range_x=[self.floor, self.ceil],
                       #range_y=[self.floor, self.ceil],
                       #color_discrete_sequence=[ "red"])
    else:
      fig = go.Scatter(x=self.df["diameter"], 
                       y=self.df["diameter"],
                       marker_color='rgb(0,0,255)',
                       name="All")
                       #xaxis=dict(x=[self.floor, self.ceil]) )
                       #range_x=[self.floor, self.ceil],
                       #range_y=[self.floor, self.ceil],
                       #color_discrete_sequence=[ "green", "red"])
    #fig.update_layout(xaxis_range=[self.floor, self.ceil]    )
    return fig

  def chart_scatter(self):
    fig = go.Figure()
    fig.add_trace(self.__chart_scatter_go())
    fig.add_trace(self.__chart_scatter_go('UNDER'))
    fig.add_trace(self.__chart_scatter_go('COM'))
    print("promedio ",self.get_mean())
    fig.add_annotation(x=self.get_mean(), y=self.get_mean(),
                text= f'Full mean = {round(self.get_mean(),2)}',
                font=dict(color = 'Blue'),
                showarrow=True,
                ax=self.get_mean(),
                ay=self.get_mean('UNDER'),
                axref='x',
                ayref='y',
                arrowhead=0)
    fig.add_annotation(x=self.get_mean("UNDER"), y=self.get_mean("UNDER"),
                text= f'Industry mean = {round(self.get_mean("UNDER"),2)}',
                font=dict(color = 'Red'),
                showarrow=True,
                arrowhead=0)
    fig.add_annotation(x=self.get_mean("COM"), y=self.get_mean("COM"),
                text= f'Commercial mean = {round(self.get_mean("COM"),2)}',
                font=dict(color = 'Green'),
                showarrow=True,
                arrowhead=0)

    return fig

  def chart_histogram(self):
    print("Soy histograma que he sido llamado con {} datos".format(self.df.shape))
    if not self.df.empty:
      fig=px.histogram(self.df,
                      x='diameter', 
                      nbins = self.num_bins, 
                      range_x=[self.floor, self.ceil], 
                      category_orders=dict(my_bin=self.bins_names),
                      pattern_shape="comercial",
                      color="comercial"
                      )
      fig.add_vline(x=self.get_mean(self.__commercial_label), 
                    line_dash = 'dash',
                    line_color = 'Green',
                    line_width=1,
                    annotation_text=f'     {round(self.get_mean(self.__commercial_label),2)}',
                    annotation_position ="top")
      fig.add_vline(x=self.get_mean(self.__under_commercial_label), 
                    line_dash = 'dash', 
                    line_color = 'Red',
                    line_width=1,
                    annotation_text=f'     {round(self.get_mean(self.__under_commercial_label),2)}',
                    annotation_position ="top")
      fig.add_vline(x=self.get_mean(), 
                    line_dash = 'dash', 
                    line_color = 'Blue',
                    line_width=0.5,
                    annotation_text=f'{round(self.get_mean(),2)}     ',
                    annotation_position ="top")

      fig.add_annotation(
          text=f'{"Full mean".rjust(16," ")} = {round(self.get_mean(),2)}',
          xref="paper", yref="paper",
          font=dict(color = 'Blue', family = "Courier New"),
          x=0, y=0.99, showarrow=False) 
      fig.add_annotation(
          text=f'{"Commercial mean".rjust(16," ")} = {round(self.get_mean(self.__commercial_label),2)}',
          xref="paper", yref="paper",
          font=dict(color = 'Green', family = "Courier New"),
          x=0, y=0.95, showarrow=False)
      fig.add_annotation(
          text=f'{"Industry mean".rjust(16," ")} = {round(self.get_mean(self.__under_commercial_label),2)}',
          xref="paper", yref="paper",
          font=dict(color = 'Red', family = "Courier New"),
          x=0, y=0.91, showarrow=False)

      fig.add_vrect(x0=0, x1=self.get_commercial(), 
                annotation_text="industry", annotation_position="top",
                fillcolor="red", opacity=0.03, line_width=0)

      fig.update_yaxes(title_text=self.__texts[self.__my_languaje]["chart_histogram_yaxe"])
      fig.update_xaxes(title_text="diametro  en milimetros")
      fig.update_layout(bargap=0.2)
      #fig.update_xaxes(type='category')
    else:
      df = px.data.tips()
      fig = px.histogram(df, x="total_bill")

    return fig

  def chart_facet(self):
    fig=px.scatter(self.df.sort_values('diameter'), 
                   x='diameter', 
                   y='diameter', 
                   color='comercial', 
                   facet_row = 'my_bin', 
                   marginal_x='box', 
                   height=4000)
    return fig

  def chart_violin_bins(self, column="diameter"):
    """ Plots a violin per histogram bin.
    
    Parameters
    ----------
    column -- String: DF's column to use for Y values. accepts diameter or
    distance. it help to aling all violing to bin's floor
    """

    fig = go.Figure()
    color_discrete_map = {'COM': 'rgb(255,0,0)', 'UNDER': 'rgb(0,255,0)'}
    for bin in self.bins_names:
        fig.add_trace(go.Violin(x=self.df['my_bin'][(self.df['my_bin'] == bin)],
                                y=self.df[column][(self.df['my_bin'] == bin)],
                                #color=self.df['comercial'][(self.df['my_bin'] == bin)],
                                pointpos=-0.3, # where to position points
                                legendgroup=bin, 
                                scalegroup=bin, 
                                name=bin,
                                showlegend=False,
                                alignmentgroup=0,
                                side='positive')
                                #color_discrete_map=color_discrete_map)
        )
  
    # update characteristics shared by all traces
    fig.update_traces(meanline_visible=True,
                      box_visible=True,
                      points='all', # show all points
                      #points='suspectedoutliers', # show all points 
                      marker_line_color='rgba(0,0,0,0.5)',
                      marker_line_width=0,  
                      jitter=0.05,  # add some jitter on points for better visibility
                      scalemode='count') #scale violin plot area with total count
    fig.update_layout(
    title_text=self.__texts[self.__my_languaje]["violin_bins_title"],
    violingap=0, violingroupgap=0, violinmode='overlay' )  #here height=1000 can improve
    
    fig.update_xaxes(title_text=self.__texts[self.__my_languaje]["violin_bins_xaxes"])
    return fig